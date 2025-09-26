import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/ad/Projects/prometheus/qa-portfolio-project-1' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_user_country_by_name(self, name, country):
        query = f"UPDATE customers SET country = '{country}' WHERE name = '{name}'"
        self.cursor.execute(query)
        self.connection.commit()
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = """
        SELECT orders.id, customers.name, products.name, products.description, orders.order_date    
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN products ON orders.product_id = products.id
        """
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_table_columns(self, table_name):
        query = f"PRAGMA table_info({table_name});"
        self.cursor.execute(query)  
        record = self.cursor.fetchall()
        return record
    
    def get_all_products(self):
        query = f"SELECT id, name FROM products ORDER BY id"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records  
    
    def get_distinct_values(self, table_name, column_name):
        query = f"SELECT DISTINCT {column_name} FROM {table_name}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def count_rows(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name}"
        self.cursor.execute(query)
        record = self.cursor.fetchone()[0]
        return record
    
    def add_new_column(self, table_name, column_name, column_type):
        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.get_table_columns(table_name)

    def drop_column(self, table_name, column_name):
        query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.get_table_columns(table_name)
    
    def set_price_for_each_product(self, id, name, price):
        query = f"UPDATE products SET price = {price} WHERE id = '{id}' AND name = '{name}'"
        self.cursor.execute(query)
        self.connection.commit()

    def get_product_price_by_name(self, name):
        query = f"SELECT price FROM products WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_price_column_values(self):
        query = "SELECT price FROM products"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def get_max_product_price(self):
        query = "SELECT MAX(price) FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record[0]
    
    def search_by_pattern(self, table_name, column_name, pattern):
        query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '{pattern}'"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def group_by_column(self, table_name, column_name):
        query = f"SELECT {column_name}, COUNT(*) FROM {table_name} GROUP BY {column_name} ORDER BY COUNT(*) DESC"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
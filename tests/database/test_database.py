import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
        
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'
         
@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_new_product_insert():
    db = Database()
    db.insert_product(10, 'капуста', 'квашена', 5)
    new_product_qnt = db.select_product_qnt_by_id(4)

    assert new_product_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

#1-Отримуємо унікальні значення з колонки продуктів і перевіряємо, що їх 5 або більше
@pytest.mark.portfolio_db
def test_list_unique_products():
    db = Database()
    products = db.get_distinct_values('products', 'name')
    print("Unique product names:", products)
    assert len(products) >= 5

#2-Змінюємо країну користувача на іншу і перевіряємо, що зміни відбулися
@pytest.mark.portfolio_db
def test_update_user_country():
    db = Database()
    db.update_user_country_by_name('Sergii', 'USA')
    user = db.get_user_address_by_name('Sergii')
    assert user[0][3] == 'USA'

#3-Отримуємо унікальні значення з колонки країн і перевіряємо, що таких більше 1
@pytest.mark.portfolio_db
def test_list_customers_countries():
    db = Database()
    countries = db.get_distinct_values('customers', 'country')
    print("We have customers from the next countries:", countries)
    print(len(countries))
    assert len(countries) > 1

#4-Отримуємо загальну кількість створених замовлень і перевіряємо, що їх 1 або більше
@pytest.mark.portfolio_db
def test_get_all_orders_count():
    db = Database()
    orders_count = db.count_rows('orders')
    print("General orders count is", orders_count)
    assert orders_count >= 1

#5-Перевіряємо додавання нової колонки 'price' до таблиці продуктів
@pytest.mark.portfolio_db
def test_add_price_column_to_products():
    db = Database()
    columns = db.get_table_columns('products')
    isPriceColumnExist = any(col[1] == 'price' for col in columns)

    if isPriceColumnExist:
        db.drop_column('products', 'price')

    columns = db.add_new_column('products', 'price', 'REAL')

    assert isPriceColumnExist
    print("Updated products table columns:", columns)

#6-Встановлюємо ціну для кожного продукту і перевіряємо, що ціни додалися
@pytest.mark.portfolio_db
def test_set_products_price():
    db = Database()
    products = db.get_all_products()
    print("Products before setting prices:", products)
    price = 5
    for id, name in products:
        db.set_price_for_each_product(id, name, price)
        price += 2

    prices = db.get_price_column_values()
    print("Product prices:", prices)
    assert len(prices) == len(products)

#7-Перевіряємо максимальну ціну продукту
@pytest.mark.portfolio_db
def test_check_max_product_price():
    db = Database()
    max_price = db.get_max_product_price()
    print("Max product price is", max_price)
    assert max_price <= 30

#8-Перевіряємо пошук по шаблону в адресі користувача
@pytest.mark.portfolio_db
def test_search_address_by_pattern():
    db = Database()
    pattern = '%Nezal%'
    users = db.search_by_pattern('customers', 'address', pattern)
    print("Users with 'Nezal' in their address:", users)
    assert len(users) >= 1

#9-Перевіряємо групування продуктів по назві
@pytest.mark.portfolio_db
def test_group_by_product_name():
    db = Database()
    grouped_products = db.group_by_column('products', 'name')
    print("Grouped products by name:", grouped_products)
    for name, count in grouped_products:
        if name == 'солодка вода':
            assert count == 2
        if name == 'хліб':  
            assert count == 2
    else:
        assert count == 1

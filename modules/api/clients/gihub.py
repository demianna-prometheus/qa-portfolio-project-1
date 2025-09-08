import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def get_emojis(self, etag_header: str | None = None):
        headers = {}
        if etag_header:
            headers["If-None-Match"] = etag_header
        
        r = requests.get("https://api.github.com/emojis", headers=headers)
      
        if r.status_code == 200:
            body = r.json()
        else:
            body = None
    
        status = r.status_code
        headers = r.headers

        return body, status, headers
    
    def list_commits(self, owner, repo, params=None):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()
        status_code = r.status_code

        return body, status_code






  
import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
    
 
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.portfolio
def test_list_emojis(github_api):
    body, status, headers = github_api.get_emojis()
    print(body, status, headers)
    assert status == 200
    assert len(body) > 0

@pytest.mark.portfolio
def test_check_smile_emojis(github_api):
    body, status, headers = github_api.get_emojis()
    assert body['smile'] == "https://github.githubassets.com/images/icons/emoji/unicode/1f604.png?v8"


@pytest.mark.portfolio
def test_get_emojis_not_modified(github_api):
    body, status, headers = github_api.get_emojis()
    # Отримуємо ETag з заголовків відповіді
    etag = headers.get("ETag")
    print(f"ETag отримано: {etag}")
    assert etag
    assert status == 200

    # Тепер робимо повторний запит з If-None-Match
    body, status, headers = github_api.get_emojis(etag_header=etag)

    # Очікуємо 304 Not Modified і що тіло відповіді буде None (бо закешовано)
    assert status == 304
    assert body == None    
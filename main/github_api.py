import requests

def fetch_github_commits(repo_owner: str, repo_name: str, access_token: str):
    '''
    Извлечение информации о коммитах с помошью Github API

    Parameters
    ----------
    repo_owner: str
        Владелец репозитория
    repo_name: str
        Название репозитория
    access_token: str
        Персональный токен доступа
    '''
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print("Не удалось получить данные")
        return None
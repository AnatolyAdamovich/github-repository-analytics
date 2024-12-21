import json
import time
import argparse
from confluent_kafka import Producer
from custom_generator import generate_fake_commits
from github_api import fetch_github_commits

KAFKA_SERVER = 'kafka:9092'
KAFKA_TOPIC = 'commits_topic'

producer_config = {
        "bootstrap.servers": KAFKA_SERVER
    }

producer = Producer(producer_config)

def send_data(data: dict,
              topic: str = "commits_topic"):
    """
    Отправка данных (коммитов) в топик Kafka
    """

    data_json = json.dumps(data)
    producer.produce(topic, value=data_json)
    producer.flush()


def main(method: str,
         github_owner: str,
         github_repo: str,
         github_token: str):
    '''
    Kafka Producer
    
    Parameters
    ----------
    method: ('github', 'fake')
        Метод извлечения данных
    github_owner: str
        Владелец репозитория
    github_token: str
        Токен доступа для Github API
    github_repo: str
        Название репозитория
    '''
    # извлечение информации о коммитах
    if method == 'github':
        print("Получение и отправка данных с GitHub в Kafka")
        while True:
            commits = fetch_github_commits(repo_owner=github_owner,
                                           repo_name=github_repo,
                                           access_token=github_token)
        
            for i, commit in enumerate(commits):            
                sha = commit["sha"]
                message = commit["commit"]["message"]
                author = commit["commit"]["author"]["name"]
                date = commit["commit"]["author"]["date"][:10]

                commit_data = {
                    "commit_id": sha,
                    "commit_message": message,
                    "author": author,
                    "commit_date": date
                }
                send_data(data=commit_data,
                          topic=KAFKA_TOPIC)
                time.sleep(5)
                print(f'Отправлен коммит {i}')

    elif method == 'fake':
        print("Генерация и отправка фейковых данных в Kafka")
        while True:
            commits = generate_fake_commits()
            for i, commit in enumerate(commits):
                send_data(data=commit,
                          topic=KAFKA_TOPIC)
                
                time.sleep(5)
                print(f'Отправлен коммит {i}')


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description="Producer для отправки данных")
    parser.add_argument("--source",
                        choices=["fake", "github"], 
                        required=True, 
                        help="Источник данных: 'fake' для генерации фейковых коммитов или 'github' для получения данных с GitHub")
    parser.add_argument("--token",
                        type=str,
                        default=None,
                        help="Access token для GitHub API (требуется, если источник 'github')")
    parser.add_argument("--repo",
                        type=str,
                        default=None,
                        help="Название репозитория для GitHub API (требуется, если источник 'github')")
    parser.add_argument("--owner",
                        type=str,
                        default=None,
                        help="Владелец репозитория для GitHub API (требуется, если источник 'github')")
    args = parser.parse_args()

    main(method=args.source,
         github_token=args.token, 
         github_owner=args.owner,
         github_repo=args.repo)
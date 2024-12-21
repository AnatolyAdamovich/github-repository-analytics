import random  
import uuid  
from datetime import datetime, timedelta  

#def generate_fake_commits(authors, num_commits): start_date = datetime(2024, 12, 1) end_date = datetime(2024, 12, 31) time_between_dates = end_date - start_date days_between_dates = time_between_dates.days random_number_of_days = random.randrange(days_between_dates) commit_date = start_date + timedelta(days=random_number_of_days) commit_date_str = commit_date.strftime("%Y-%m-%d") fake_commit = { "commit_id": commit_id, "commit_message": commit_message, "author": author, "commit_date": commit_date_str } fake_commits.append(fake_commit) return fake_commits  


AUTHORS = ['Ivan M', 'Anatoly A', 'Masha R',
           'Roman F', 'Vladimir L', 'Veronika A',
           'John K', 'Alisa R', 'Alexandr T', 'Fedor S']

def generate_fake_commits(authors=AUTHORS, num_commits=250):
    commits = []

    for i in range(num_commits):
        commit_id = str(uuid.uuid4())
        commit_message = f"Commit message {i+1}"
        author = random.choice(authors)

        start_date = datetime(2024, 12, 1)
        commit_date = start_date + timedelta(random.randrange(30))
        commit_date_str = commit_date.strftime("%Y-%m-%d")
        commit = {
            'commit_id': commit_id,
            'author': author,
            'commit_message': commit_message,
            'commit_date': commit_date_str
        }
        commits.append(commit)
    return commits




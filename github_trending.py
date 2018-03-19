import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    date_ago = (datetime.today()-timedelta(days)).strftime("%Y-%m-%d")
    url = 'https://api.github.com/search/repositories'
    parameters = {
        'q': 'created:>={}'.format(date_ago),
        'sort': 'stars',
        'per_page': top_size
    }
    response = requests.get(url, params=parameters)
    return response.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    url_open_issues = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    open_issues_amount = len(requests.get(url_open_issues).json())
    return open_issues_amount


if __name__ == '__main__':
    top_size = 20
    days = 7
    try:
        repositories = get_trending_repositories(top_size)
        print('\nPopular projects for the last week:\n')
        for repository in repositories:
            open_issues = get_open_issues_amount(
                repository['owner']['login'],
                repository['name']
            )
            print('Name: {}/{}\n'
                  'Open issues: {}\n'
                  'Url: {}\n'.format(
                   repository['owner']['login'],
                   repository['name'],
                   open_issues,
                   repository['url']
                  )
            )
    except requests.exceptions.ConnectionError:
        exit('Сheck your connection')



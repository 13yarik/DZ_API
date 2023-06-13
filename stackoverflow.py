import requests

def get_questions():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1686441600&todate=1686614400&order=desc&sort=activity&tagged=Python&site=stackoverflow'
    response = requests.get(url)
    data = requests.get(url).json()
    return data['items']

questions = get_questions()
# print(questions)

for question in questions:
    print(f'Заголовок вопроса: {question["title"]}\n'
          f'Ссылка на этот вопрос: {question["link"]}\n'
          f'{"-" * 100}')

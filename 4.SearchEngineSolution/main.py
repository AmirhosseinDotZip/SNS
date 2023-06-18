import json


def search_articles(search_term):
    with open('./data/articles.json') as f:
        data = json.load(f)

    results = []
    for article in data['articles']:
        if search_term.lower() in article['title'].lower() or search_term.lower() in article['content'].lower():
            results.append(article)

    return results


search_results = search_articles('Python Data Structures')
print(search_results)

import json
from nltk.tokenize import word_tokenize


def search_articles(search_term):
    with open('./data/articles.json') as f:
        data = json.load(f)

    # Tokenize the search term
    tokens = word_tokenize(search_term.lower())

    results = []
    for article in data['articles']:
        # Tokenize the article title and content
        title_tokens = word_tokenize(article['title'].lower())
        content_tokens = word_tokenize(article['content'].lower())

        # Check if any of the search term tokens are in the article title or content
        if any(token in title_tokens or token in content_tokens for token in tokens):
            # Add a formatted string to the results list
            results.append('Title: {}\n{}\n'.format(
                article['title'], article['content']))

    return results


search_results = search_articles('Data structure in Python')
# Print each search result on a new line
print('\n'.join(search_results))

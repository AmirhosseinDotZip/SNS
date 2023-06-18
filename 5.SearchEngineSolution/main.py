import json
import re
from nltk.tokenize import word_tokenize


def search_articles(search_term):
    with open('./data/articles.json') as f:
        data = json.load(f)

    # Define a regular expression pattern to match data structure related terms in Python
    pattern = r'\b(data ?structures?|list|tuple|dictionary|stack|queue)\b.*\bpython\b'

    # Tokenize the search term
    tokens = word_tokenize(search_term.lower())

    results = []
    for article in data['articles']:
        # Combine the article title and content into a single string for matching
        text = article['title'].lower() + ' ' + article['content'].lower()

        # Check if the regular expression pattern matches the article text
        if re.search(pattern, text):
            # Add a formatted string to the results list
            results.append('Title: {}\n{}\n'.format(
                article['title'], article['content']))

    return results


search_results = search_articles('Data structure in Python')
# Print each search result on a new line
print('\n'.join(search_results))

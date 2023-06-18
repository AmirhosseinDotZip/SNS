import json
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download the necessary NLTK resources
nltk.download('maxent_ne_chunker')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('words')


def search_articles(search_term):
    with open('./data/articles.json') as f:
        data = json.load(f)

    # Tokenize the search term
    tokens = word_tokenize(search_term.lower())

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if not token in stop_words]

    # Perform part-of-speech tagging to identify nouns and proper nouns
    pos_tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in pos_tags if pos.startswith('N')]

    # Use named entity recognition to identify named entities
    named_entities = nltk.chunk.ne_chunk(pos_tags, binary=True)
    named_entities = set(' '.join(i[0] for i in t)
                         for t in named_entities if isinstance(t, nltk.tree.Tree))

    # Combine the identified terms into a regular expression pattern
    pattern = '|'.join(list(named_entities) + list(nouns))
    pattern = r'\b' + pattern + r'\b.*'

    # Create a lemmatizer to normalize the search terms
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    results = []
    for article in data['articles']:
        # Combine the article title and content into a single string for matching
        text = article['title'].lower() + ' ' + article['content'].lower()

        # Normalize the article text using the lemmatizer
        text_tokens = word_tokenize(text)
        text_tokens = [
            token for token in text_tokens if not token in stop_words]
        text_lemmas = [lemmatizer.lemmatize(token) for token in text_tokens]
        normalized_text = ' '.join(text_lemmas)

        # Check if the regular expression pattern matches the article text
        if re.search(pattern, normalized_text):
            # Add a formatted string to the results list
            results.append('Title: {}\n{}\n'.format(
                article['title'], article['content']))

    return results


# search for articles related to the search term
search_results = search_articles('data structures')

# Print the number of search results
print(f"Number of search results: {len(search_results)}\n")

# Print each search result on a new line
print('\n'.join(search_results))

# Article Search

This code searches for articles related to a given search term in the file `articles.json` and returns the matching results. The search is performed on both the title and content of each article, and the results are formatted to include the title and content of each matching article.

## Requirements

- Python 3.x
- NLTK (Natural Language Toolkit) library

To install NLTK, you can use pip:

```pip install nltk```


## How to Use

1. Clone the repository and navigate to the project directory.
2. Open a terminal window and run the following command: 

```python main.py```


3. Enter the search term when prompted. 
4. The program will output the number of matching articles found and display each article's title and content on a new line.

Note: The file `articles.json` should be located in the `data` directory in the project folder. You can modify the file name or path in the code if necessary.

## How it Works

1. Load the JSON file containing the articles into the program.
2. Tokenize the search term using NLTK's `word_tokenize`.
3. Remove stop words from the tokenized search term.
4. Perform part-of-speech tagging with NLTK's `pos_tag` to identify nouns and proper nouns.
5. Use named entity recognition with NLTK's `ne_chunk` to identify named entities.
6. Combine the identified terms into a regular expression pattern and search for matches in the article text.
7. Normalize the article text using a lemmatizer to remove variations in word forms.
8. If a match is found, format the article title and content and add it to the results list.
9. Return the list of search results.

I hope this README file helps you to understand how to use the code effectively and efficiently!

---
Made with ❤️ by Baniminator
import re

# Sample data
data = [
    {"id": 1, "text": "Python is a popular programming language"},
    {"id": 2, "text": "Java is used for building enterprise applications"},
    {"id": 3, "text": "JavaScript is widely used for web development"},
]

# Tokenize the data
tokenized_data = []
for record in data:
    tokens = re.findall(r"\w+", record["text"].lower())
    tokenized_data.append({"id": record["id"], "tokens": tokens})

# Create an inverted index
inverted_index = {}
for record in tokenized_data:
    for token in record["tokens"]:
        if token not in inverted_index:
            inverted_index[token] = []
        inverted_index[token].append(record["id"])

# Query the index
query = "programming language"
query_tokens = re.findall(r"\w+", query.lower())

matching_ids = set(inverted_index[query_tokens[0]])
for token in query_tokens[1:]:
    matching_ids = matching_ids.intersection(set(inverted_index[token]))

results = [record for record in data if record["id"] in matching_ids]
print(results)

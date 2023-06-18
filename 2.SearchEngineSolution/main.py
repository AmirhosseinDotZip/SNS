import re


# Define a function to search for a word or phrase in the documents and return the matching sentences


def search_documents(query, documents):
    # Create an empty list to store the matching sentences
    matches = []
    # Loop through each document
    for doc in documents:
        # Split the document into sentences
        sentences = re.split('[?.!]', doc)
        # Loop through each sentence
        for sentence in sentences:
            # If the query is found in the sentence, add it to the matches list
            if query.lower() in sentence.lower():
                matches.append(sentence.strip())
    # Return the list of matching sentences
    return matches


# Define a list of documents
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A quick brown dog jumps over the lazy cat",
    "The lazy dog sleeps all day",
    "The lazy cat sleeps in the sun",
    "Dogs are man's best friend",
    "I love taking my dog for long walks on the beach",
    "Some dogs have jobs like police work or search and rescue",
    "My dog is always happy to see me when I come home",
    "Dogs come in many different breeds and sizes",
    "Service dogs help people with disabilities navigate the world",
    "I take my dog to the park to play fetch",
    "Dogs can be trained to perform all sorts of useful tasks",
    "The bond between a dog and their owner can be very strong",
    "My dog loves playing with his favorite toy, a squeaky ball",
    "Dog parks are a great place for dogs to socialize and exercise",
    "Adopting a dog can be a rewarding experience",
    "I always make sure to clean up after my dog when we go for walks",
    "Some dogs are prone to health issues like hip dysplasia or allergies",
    "My dog is always by my side no matter what",
    "There are many famous dogs throughout history and pop culture",
    "I make sure to give my dog plenty of exercise and mental stimulation",
    "Dogs communicate with each other through body language and vocalizations",
    "I love snuggling up with my dog on the couch",
    "Dog shows are competitions where dogs are judged on their appearance and behavior",
    "Some dogs are used for hunting or herding livestock",
    "I take my dog to the groomer regularly to keep him looking his best",
    "Dogs have been domesticated for thousands of years",
    "Dog owners should be responsible and ensure their dogs are well-behaved and properly trained",
    "Puppies are adorable but require a lot of time, attention, and training",
    "I love taking my dog on road trips and exploring new places together",
    "Dogs can provide emotional support and assistance to people with mental health conditions",
    "In some cultures, dogs are considered sacred or even worshipped",
    "My dog loves playing tug-of-war with me",
    "Dogs have an incredible sense of hearing and can detect sounds that humans cannot",
    "Dog agility competitions test a dog's ability to navigate obstacles and follow commands",
    "I enjoy cooking homemade treats for my dog",
    "Some dogs are natural swimmers and enjoy activities like dock diving",
    "Dogs have played important roles in human history",
    "I love watching my dog chase after a frisbee",
    "Dogs have been featured in literature throughout history",
    "Dog trainers use positive reinforcement techniques to teach dogs new skills and behaviors",
    "Some dogs are used for therapy purposes and can provide comfort to people in hospitals",
    "I always make sure my dog has plenty of fresh water available",
    "Dogs have been bred for specific purposes like herding or guarding livestock",
    "I take my dog to the vet regularly for check-ups and vaccinations",
    "Dogs can experience a range of emotions like happiness, fear, and sadness",
    "I love snuggling with my dog on a cold winter night",
    "Dogs have been known to save lives by alerting humans to danger",
    "Dog owners should make sure their dogs are up-to-date on their vaccinations and preventatives",
]


# Search for the word "dog" in the documents
matches = search_documents("dog", documents)

# Print the matching sentences
for match in matches:
    print(match)

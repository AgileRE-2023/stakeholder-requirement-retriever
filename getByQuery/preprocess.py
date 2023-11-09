
df = ""



# Function to remove punctuation
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
# Apply the function to the 'text' column
df['job-listings'] = df['job-listings'].apply(remove_punctuation)
df['job-listings'] = df['job-listings'].str.replace('\n', ' ')
df['job-listings'] = df['job-listings'].str.replace(r'\s+', ' ', regex=True)
df['job-listings'] = df['job-listings'].str.replace('●', '')
df['job-listings'] = df['job-listings'].str.replace('’', '')
df['job-listings'] = df['job-listings'].str.replace('–', '')
# Display the modified DataFrame
df.head(5)




# Apply the formatting function to the 'Text' column
text_array = df['job-listings'].tolist()
text_array


import nltk
# nltk.download('punkt')
# Tokenize each sentence and convert words to lowercase
tokenized_sentences = [nltk.word_tokenize(sentence.lower()) for sentence in text_array]
print(tokenized_sentences)


from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
# Create a WordNetLemmatizer object
lemmatizer = WordNetLemmatizer()
lemmatized_words = []
for jobListing in tokenized_sentences:
    # Stem the words
    lemmatized_words.append([lemmatizer.lemmatize(word) for word in jobListing])
print(lemmatized_words)


from nltk.corpus import stopwords

# nltk.download('stopwords')

# Get the English stopwords list
stop_words = set(stopwords.words('english'))

# Remove stopwords from the text
filtered_words = []
for jobListing in lemmatized_words:
    filtered_words.append([word for word in jobListing if word.lower() not in stop_words])

# Join the filtered words back into a sentence
preprocessed_jobListings = []
for jobListing in filtered_words:
    preprocessed_jobListings.append(' '.join(jobListing))

# Join the preprocessed job listings into one full sentence
full_sentence = ' '.join(preprocessed_jobListings)
# print(preprocessed_jobListings)

import re
# Remove numbers using regex
text_without_numbers = re.sub(r'\d+', '', full_sentence)
print(text_without_numbers)




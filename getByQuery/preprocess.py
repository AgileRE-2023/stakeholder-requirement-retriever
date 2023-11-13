import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
def preprocess_data(job_descriptions):
    # Function to remove punctuation
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    # Apply the function to each job description
    job_descriptions = [remove_punctuation(description) for description in job_descriptions]
    
    # Replace newline characters with a space
    job_descriptions = [description.replace('\n', ' ') for description in job_descriptions]

    # Replace consecutive whitespaces with a single space
    job_descriptions = [re.sub(r'\s+', ' ', description, flags=re.UNICODE) for description in job_descriptions]

    # Replace specific characters
    job_descriptions = [description.replace('●', '').replace('’', '').replace('–', '') for description in job_descriptions]

    
    

    # Tokenize each sentence and convert words to lowercase
    tokenized_sentences = [nltk.word_tokenize(description.lower()) for description in job_descriptions]

    # Create a WordNetLemmatizer object
    lemmatizer = WordNetLemmatizer()

    # Lemmatize each word
    lemmatized_words = [[lemmatizer.lemmatize(word) for word in sentence] for sentence in tokenized_sentences]

    # Get the English stopwords list
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from the text
    filtered_words = [[word for word in sentence if word.lower() not in stop_words] for sentence in lemmatized_words]

    # Join the filtered words back into a sentence
    preprocessed_jobListings = [' '.join(sentence) for sentence in filtered_words]

    # Join the preprocessed job listings into one full sentence
    full_sentence = ' '.join(preprocessed_jobListings)

    # Remove numbers using regex
    text_without_numbers = re.sub(r'\d+', '', full_sentence)

    return text_without_numbers


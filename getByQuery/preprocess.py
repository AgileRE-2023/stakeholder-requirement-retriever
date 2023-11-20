import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from deep_translator import GoogleTranslator
import re

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
def translate_array(array):
    translated_array = []

    for text_to_translate in array:
        translated_text = GoogleTranslator(source='auto', target='en').translate(text_to_translate)
        translated_array.append(translated_text)

    return translated_array
def preprocess_data(job_descriptions):
    # Function to remove punctuation
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    # Apply the function to each job description
    job_descriptions = [remove_punctuation(description) for description in job_descriptions]
    
    # Replace newline characters with a space
    job_descriptions = [description.replace('\n', ' ') for description in job_descriptions]

    # Replace consecutive whitespaces with a single space and Remove numbers
    job_descriptions = [re.sub(r'\s+', ' ', re.sub(r'\d', '', description), flags=re.UNICODE) for description in job_descriptions]

    # Replace specific characters
    job_descriptions = [description.replace('●', '').replace('’', '').replace('–', '') for description in job_descriptions]

    # Translate to english
    translated_data = translate_array(job_descriptions)

    # Tokenize each sentence and convert words to lowercase
    tokenized_sentences = [nltk.word_tokenize(description.lower()) for description in translated_data]

    # Create a WordNetLemmatizer object
    lemmatizer = WordNetLemmatizer()

    # Lemmatize each word
    lemmatized_words = [[lemmatizer.lemmatize(word) for word in sentence] for sentence in tokenized_sentences]

    # Get the English stopwords list
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from the text
    preprocessed_separate_docs_tokenized = [[word for word in sentence if word.lower() not in stop_words] for sentence in lemmatized_words]

    # Join the filtered words back into a sentence
    preprocessed_separate_docs = [' '.join(sentence) for sentence in preprocessed_separate_docs_tokenized]

    # Join the preprocessed job listings into one full sentence
    preprocessed_one_sentence = ' '.join(preprocessed_separate_docs)

    return (preprocessed_one_sentence,preprocessed_separate_docs,preprocessed_separate_docs_tokenized)  


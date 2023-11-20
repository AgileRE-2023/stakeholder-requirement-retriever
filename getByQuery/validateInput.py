from deep_translator import GoogleTranslator
import string
import re

def remove_punctuation_and_html(input_string):
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    no_punct = input_string.translate(translator)
    
    # Remove HTML tags
    clean_text = re.sub('<.*?>', '', no_punct)
    
    return clean_text

def validateInput(input):
    clean_input = remove_punctuation_and_html(input)
    # Translate to english
    translated_text = GoogleTranslator(source='auto', target='en').translate(clean_input)
    final_input = translated_text.replace(" ", "+")
    return final_input

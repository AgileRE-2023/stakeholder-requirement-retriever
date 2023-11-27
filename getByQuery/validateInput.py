from deep_translator import GoogleTranslator
import string
import re
from .models import Prodi

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
    # Check if the translated input is in the list of nama_prodi, __iexact is used for a case-insensitive match.
    try:
        prodi_instance = Prodi.objects.get(nama_prodi__iexact=input)
        return final_input, prodi_instance
    except Prodi.DoesNotExist:
        return final_input  # Return final_input only if the input is not in the list of nama_prodi

import nltk
import numpy as np
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def posTagging(data):
        nouns = []
        # Tokenize and collect nouns with specific POS tags
        for sent in sent_tokenize(data):
            wordtokens = word_tokenize(sent)
            pos_tags = nltk.pos_tag(wordtokens)
            
            # Select words with POS tags NN (Singular noun), NNS, NNP, NNPS (Proper and plural noun)
            selected_nouns = [word for word, pos_tag in pos_tags if pos_tag in ['NN', 'NNS', 'NNP', 'NNPS']]
            
            nouns.extend(selected_nouns)
        return nouns


def mainProcess(preprocessed_fulltext, lemmatized_words):
    
    nouns = posTagging(preprocessed_fulltext)

    # Reconstruct the sentence
    filtered_sentence = ' '.join(nouns)

    # Filtering words in each job listing to only include filtered_sentence after POS tagging
    blacklist_words = ['job', 'experience', 'work', 'solution', 'technology', 'information', 'knowledge', 'requirement','understanding', 'working', 'product', 'process', 'ability', 'good', 'skill', 'year', 'learn','need', 'excellent', 'implement','team','project','development','business', 'software', 'system', 'design', 'client','minimum']
    def word_exists_as_whole_word(word, text):
        pattern = r'\b' + re.escape(word) + r'\b'
        return bool(re.search(pattern, text))
    job_listings_per_word_after_pos_tagging = []
    for jobList in lemmatized_words:
        job_listing_after_pos_tagging = []
        for word in jobList:
            if word_exists_as_whole_word(word, filtered_sentence) and word not in blacklist_words:
                job_listing_after_pos_tagging.append(word)
        job_listings_per_word_after_pos_tagging.append(job_listing_after_pos_tagging)

    # Combining words into sentence on each job listing
    job_listings_sentenced_after_pos_tagging = [' '.join(jobList) for jobList in job_listings_per_word_after_pos_tagging]

    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit and transform the documents to compute TF-IDF vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform(job_listings_sentenced_after_pos_tagging)

    # Convert the TF-IDF matrix to a Pandas DataFrame
    df_done = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

    # Calculate the sum of TF-IDF scores for each term across all documents
    term_sum = df_done.sum(axis=0)

    # Create a DataFrame to store the summed TF-IDF scores and their corresponding terms
    term_ranking_df = pd.DataFrame({'Term': term_sum.index, 'Summed_TFIDF': term_sum.values})

    # Sort the terms by their summed TF-IDF scores in descending order
    term_ranking_df = term_ranking_df.sort_values(by='Summed_TFIDF', ascending=False)

    # Select the top n terms
    top_terms = term_ranking_df.head(10)

    # Extract the top terms as a list
    top_terms_list = top_terms['Term'].tolist()

    return top_terms_list

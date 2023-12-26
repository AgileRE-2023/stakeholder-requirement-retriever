import nltk
import numpy as np
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def posTagging(data):
        import spacy

        # Load the spaCy English model
        posTagging = spacy.load("en_core_web_sm")

        # Process the sentence with spaCy pos tagging
        doc = posTagging(data)

        # # Iterate through the tokens and print their text and POS labels
        # for token in doc:
        #     print(f"Token: {token.text}, POS: {token.pos_}")

        # Define POS tags to include (all nouns)
        tags_to_include = ["NOUN","PROPN"]

        # Create a filtered list of tokens only noun
        nouns_in_array = [token.text for token in doc if token.pos_ in tags_to_include]

        # # Reconstruct the sentence 
        # nouns_in_one_sentence = ' '.join(nouns_in_array)

        return nouns_in_array

def first_TF_IDF(job_listings_sentenced_after_pos_tagging):
    # getting the top n nouns (singe-word term)

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

    # Extract the top terms as a list and Select the top n terms
    top_one_word_nouns = term_ranking_df['Term'].tolist()[:20]

    return top_one_word_nouns

def get_two_words_terms(top_one_word_nouns,job_listings_per_word_after_pos_tagging):
    def extract_adjacent_terms(tokenized_sentences, term):
        new_terms = []
        for sentence in tokenized_sentences:
            for i, word in enumerate(sentence):
                if word.lower() == term.lower():
                    # Extract the word before and after the term
                    before_word = sentence[i - 1] if i > 0 else None
                    after_word = sentence[i + 1] if i + 1 < len(sentence) else None

                    # Add the context words to the list
                    if before_word:
                        new_terms.append(f"{before_word} {term}")
                    if after_word:
                        new_terms.append(f"{term} {after_word}")

        return new_terms

    all_new_2_words_terms = []

    # Loop over each term in terms_list
    for term in top_one_word_nouns:
        new_terms = extract_adjacent_terms(job_listings_per_word_after_pos_tagging, term)
        all_new_2_words_terms.extend(new_terms)

    # Remove duplicates
    all_new_2_words_terms = list(set(all_new_2_words_terms))

    return all_new_2_words_terms

def get_three_words_terms(top_one_word_nouns,job_listings_per_word_after_pos_tagging):
    def extract_adjacent_terms(tokenized_sentences, term):
        new_terms = []
        for sentence in tokenized_sentences:
            for i, word in enumerate(sentence):
                if word.lower() == term.lower():
                    # Extract the three words before and after the term
                    before_words = sentence[max(0, i - 2):i]
                    after_words = sentence[i + 1:min(i + 3, len(sentence))]

                    # Add the context words to the list
                    if before_words:
                        new_terms.append(' '.join(before_words + [term]))
                    if after_words:
                        new_terms.append(' '.join([term] + after_words))

        return new_terms

    all_new_3_words_terms = []

    # Loop over each term in terms_list
    for term in top_one_word_nouns:
        new_terms = extract_adjacent_terms(job_listings_per_word_after_pos_tagging, term)
        all_new_3_words_terms.extend(new_terms)

    # Remove duplicates
    all_new_3_words_terms = list(set(all_new_3_words_terms))

    return all_new_3_words_terms

def second_TF_IDF(combine_all_terms,preprocessed_separate_docs):
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np

    # Create the TF-IDF vectorizer with your specified terms and enable n-grams
    vectorizer = TfidfVectorizer(vocabulary=combine_all_terms, ngram_range=(2, 3))

    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(preprocessed_separate_docs)

    # Get the TF-IDF values
    tfidf_values = tfidf_matrix.toarray()

    # Aggregate TF-IDF scores across all documents
    aggregate_tfidf_scores = np.sum(tfidf_values, axis=0)

    # Combine terms with their aggregate TF-IDF scores
    combined_terms_and_scores = list(zip(combine_all_terms, aggregate_tfidf_scores))

    # Sort terms by their TF-IDF scores in descending order
    sorted_terms_and_scores = sorted(combined_terms_and_scores, key=lambda x: x[1], reverse=True)

    # # Print the sorted terms and their corresponding TF-IDF scores
    # for term, score in sorted_terms_and_scores:
    #     print(f"{term}: {score}")

    final_top_terms = []
    final_scores = []
    for term, score in sorted_terms_and_scores:
        final_top_terms.append(term)
        final_scores.append(score)

    return final_top_terms,final_scores


def mainProcess(preprocessed_one_sentence, preprocessed_separate_docs,preprocessed_separate_docs_tokenized):
    
    nouns = posTagging(preprocessed_one_sentence)

    # Reconstruct the sentence
    nouns_in_array = ' '.join(nouns)

    # Filtering words in each job listing to only include nouns_in_array after POS tagging, also without blacklist_words
    blacklist_words = ['job','degree', 'experience', 'work', 'technology', 'information', 'good', 'skill', 'year', 'learn','need', 'excellent','minimum','bachelor','graduate','education','science','engineering','gpa','team','working','knowledge','process','state','university','college', 'undergraduate', 'faculty', 'role', 'student', 'cover', 'school', 'online', 'customer',  'grade', 'child', 'postdoctoral' ]
    def word_exists_as_whole_word(word, text):
        pattern = r'\b' + re.escape(word) + r'\b'
        return bool(re.search(pattern, text))
    job_listings_per_word_after_pos_tagging = []
    for jobList in preprocessed_separate_docs_tokenized:
        job_listing_after_pos_tagging = []
        for word in jobList:
            if word_exists_as_whole_word(word, nouns_in_array) and word not in blacklist_words:
                job_listing_after_pos_tagging.append(word)
        job_listings_per_word_after_pos_tagging.append(job_listing_after_pos_tagging)

    # Combining words into sentence on each job listing
    job_listings_sentenced_after_pos_tagging = [' '.join(jobList) for jobList in job_listings_per_word_after_pos_tagging]

    top_one_word_nouns = first_TF_IDF(job_listings_sentenced_after_pos_tagging)

    two_words_terms = get_two_words_terms(top_one_word_nouns,job_listings_per_word_after_pos_tagging) 
    three_words_terms = get_three_words_terms(top_one_word_nouns,job_listings_per_word_after_pos_tagging)

    combine_all_terms = list(set(two_words_terms + three_words_terms))

    final_top_terms,final_scores = second_TF_IDF(combine_all_terms,preprocessed_separate_docs)

    return final_top_terms[:50],final_scores[:50]

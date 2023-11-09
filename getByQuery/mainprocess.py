data_after_preprocess = ''


# POS tagging
import spacy

# Load the spaCy English model
posTagging = spacy.load("en_core_web_sm")

# Process the sentence with spaCy pos tagging
doc = posTagging(data_after_preprocess)

# Iterate through the tokens and print their text and POS labels
for token in doc:
    print(f"Token: {token.text}, POS: {token.pos_}")

# Define POS tags to include (all nouns)
tags_to_include = ["NOUN","PROPN"]

# Create a filtered list of tokens only noun
filtered_tokens = [token.text for token in doc if token.pos_ in tags_to_include]

# Reconstruct the sentence 
filtered_sentence = ' '.join(filtered_tokens)

# Print the filtered sentence
print(filtered_sentence)



# Filtering words in each job listing to only include filtered_sentence after POS tagging
import re
blacklist_words = ['job','experience','work','solution','technology','information','knowledge','requirement','understanding','working','product','process','ability','good','skill','year','learn','need','excellent','implement']
def word_exists_as_whole_word(word, text):
    pattern = r'\b' + re.escape(word) + r'\b'
    return bool(re.search(pattern, text))
job_listings_perWord_after_posTagging = []
for jobList in lemmatized_words:
    job_listing_after_posTagging = []
    for word in jobList :
        if word_exists_as_whole_word(word, filtered_sentence) and word not in blacklist_words:
            job_listing_after_posTagging.append(word)
    job_listings_perWord_after_posTagging.append(job_listing_after_posTagging)
# print(job_listings_perWord_after_posTagging)

# combining words into sentence on each job listing
job_listings_sentenced_after_posTagging = []
for jobList in job_listings_perWord_after_posTagging:
    job_listings_sentenced_after_posTagging.append(' '.join(jobList))

print(job_listings_sentenced_after_posTagging)




from sklearn.feature_extraction.text import TfidfVectorizer
# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents to compute TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(job_listings_sentenced_after_posTagging)
# Convert the TF-IDF matrix to a Pandas DataFrame
dfDone = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
print(dfDone)   



# Calculate the sum of TF-IDF scores for each term across all documents
term_sum = dfDone.sum(axis=0)

# Create a DataFrame to store the summed TF-IDF scores and their corresponding terms
term_ranking_df = pd.DataFrame({'Term': term_sum.index, 'Summed_TFIDF': term_sum.values})

# Sort the terms by their summed TF-IDF scores in descending order
term_ranking_df = term_ranking_df.sort_values(by='Summed_TFIDF', ascending=False)

# Display the ranked terms
print(term_ranking_df.head(30))


# Combine all values in the 'term_ranking_df.head(20)' into one sentence
top20Requirement = term_ranking_df['Term'].str.cat(sep=' ')

# Print the DataFrame
print(top20Requirement)
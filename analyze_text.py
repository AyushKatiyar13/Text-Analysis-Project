import pandas as pd
from textblob import TextBlob
import nltk
import textstat
import os

# Ensure you have the necessary NLTK data downloaded
nltk.download('punkt')

def get_sentiment_scores(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def get_polarity_subjectivity(text):
    polarity, subjectivity = get_sentiment_scores(text)
    return polarity, subjectivity

def avg_sentence_length(text):
    sentences = nltk.sent_tokenize(text)
    return sum(len(sentence.split()) for sentence in sentences) / len(sentences)

def percentage_complex_words(text):
    words = text.split()
    complex_words = [word for word in words if textstat.syllable_count(word) > 2]
    return (len(complex_words) / len(words)) * 100 if words else 0

def fog_index(text):
    return textstat.gunning_fog(text)

def calculate_avg_words_per_sentence(text):
    sentences = nltk.sent_tokenize(text)
    words = [len(sentence.split()) for sentence in sentences]
    return sum(words) / len(sentences)

def complex_word_count(text):
    return len([word for word in text.split() if textstat.syllable_count(word) > 2])

def word_count(text):
    return len(text.split())

def syllables_per_word(text):
    return textstat.syllable_count(text) / len(text.split())

def personal_pronouns(text):
    pronouns = ['I', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours', 'you', 'your', 'yours', 'he', 'him', 'his', 'she', 'her', 'hers', 'they', 'them', 'their', 'theirs']
    words = text.split()
    return sum(word.lower() in pronouns for word in words)

def avg_word_length(text):
    words = text.split()
    return sum(len(word) for word in words) / len(words)

def analyze_text_files(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                # Compute metrics
                polarity, subjectivity = get_polarity_subjectivity(text)
                avg_sentence_len = avg_sentence_length(text)
                perc_complex_words = percentage_complex_words(text)
                fog_index_score = fog_index(text)
                avg_words_per_sentence_val = calculate_avg_words_per_sentence(text)
                complex_word_count_val = complex_word_count(text)
                word_count_val = word_count(text)
                syllables_per_word_val = syllables_per_word(text)
                personal_pronouns_val = personal_pronouns(text)
                avg_word_len = avg_word_length(text)
                
                # Append to results
                results.append([filename, polarity, subjectivity, avg_sentence_len, perc_complex_words, fog_index_score,
                                avg_words_per_sentence_val, complex_word_count_val, word_count_val, syllables_per_word_val,
                                personal_pronouns_val, avg_word_len])
                
    # Save to CSV
    df = pd.DataFrame(results, columns=['File Name', 'Polarity Score', 'Subjectivity Score', 'Avg Sentence Length',
                                        'Percentage of Complex Words', 'Fog Index', 'Avg Words per Sentence',
                                        'Complex Word Count', 'Word Count', 'Syllables per Word', 'Personal Pronouns',
                                        'Avg Word Length'])
    df.to_csv('output.csv', index=False)

# Call the function with the directory containing text files
analyze_text_files(r'C:\Users\Ankita\OneDrive\Desktop\New folder')

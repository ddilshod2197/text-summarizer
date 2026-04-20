import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
from string import punctuation

nltk.download('punkt')
nltk.download('stopwords')

def text_summarizer(text, summary_length=5):
    # Stop so'zlar ro'yxati
    stop_words = set(stopwords.words('english') + list(punctuation))

    # Tekstni so'zlar va satrlar orasida ajratib olamiz
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)

    # So'zlar uchun koeffitsientlar ro'yxati
    word_freq = defaultdict(int)
    for word in words:
        if word not in stop_words:
            word_freq[word] += 1

    # Satrlar uchun koeffitsientlar ro'yxati
    sent_scores = defaultdict(int)
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sent_scores[i] += word_freq[word]

    # Satrlar orasida eng yuqori koeffitsientga ega satrlarni topamiz
    top_sentences = sorted(sent_scores, key=sent_scores.get, reverse=True)[:summary_length]

    # Eng yuqori koeffitsientga ega satrlarni chiqaramiz
    summary = ' '.join([sentences[i] for i in top_sentences])

    return summary

# Testlash
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(text_summarizer(text))

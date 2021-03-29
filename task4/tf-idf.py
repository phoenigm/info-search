import math

from task2.lemmatisation import get_normal_form_counts, parse_text, sanitize_text, get_normal_form_indexed
from task3.inverted_index import word_in_documents, document_count
texts = word_in_documents()

with open("data/tf_idf.txt", 'w', encoding='utf-8') as f:
    for i in range(document_count):
        text = parse_text(i)
        text = sanitize_text(text)
        normalized_counts = get_normal_form_counts(text)
        all_words_count = len(normalized_counts)

        for word, value in normalized_counts.items():
            tf = value / all_words_count
            idf = math.log10(document_count / len(texts[word]))

            f.write(word + ' ' + str(idf) + ' ' + str(tf * idf) + '\n')

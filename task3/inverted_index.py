from task2.lemmatisation import parse_text, sanitize_text, get_normal_form_indexed
from task3.parser import parse_string

document_count = 104


def word_in_documents():
    dict_texts = dict()
    for i in range(document_count):
        text = parse_text(i)
        text = sanitize_text(text)
        normalized_text = get_normal_form_indexed(text, i)

        for key, value in normalized_text.items():
            if key in dict_texts:
                dict_texts[key].update(value)
            else:
                dict_texts[key] = value
    return dict_texts


if __name__ == "__main__":
    texts = word_in_documents()
    with open("data/inverted_index_snapshot.txt", 'w', encoding='utf-8') as f:
        for key, value in texts.items():
            f.write(key + ' ' + str(sorted(value)) + '\n')

    boolean_search_line = input("Enter boolean search line. Operators: AND, OR, NOT\n")
    result = parse_string(boolean_search_line, texts)
    print(result)

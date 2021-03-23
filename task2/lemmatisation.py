import os
import nltk
import pymorphy2
import re
from lxml import etree
from typing import Final


def parse_text(filename):
    with open("../task1/data/" + str(filename) + ".html", "r", encoding="UTF-8") as html:
        htmlparser = etree.HTMLParser()
        tree = etree.parse(html, htmlparser)
        texts_from_html = tree.xpath('//p[@data-link="text{:productCard.description}"]/text()')
        concatenated_text = str.join('', texts_from_html)
        return concatenated_text


def get_normal_form(tokens):
    normalized_words = dict()
    for token in tokens:
        parsed_word = analyzer.parse(token)
        if parsed_word[0].tag.POS in functors_pos:
            continue
        temp_set = set()
        for candidate in parsed_word:
            temp_set.add(candidate.normal_form)
        normalized_words[token.lower()] = temp_set
    return normalized_words

def get_normal_form_indexed(tokens, indx):
    normalized_words = dict()
    for token in tokens:
        parsed_word = analyzer.parse(token)
        if parsed_word[0].tag.POS in functors_pos:
            continue
        temp_set = set()
        for candidate in parsed_word:
            temp_set.add(candidate.normal_form)
        for normal_form in temp_set:
            normalized_words[normal_form] = {indx}
    return normalized_words

def contains_numeric(string):
    return RE_D.search(string)


def append_to_file(filename, content):
    os.makedirs("data", exist_ok=True)
    with open("data/" + filename, 'a', encoding='utf-8') as f:
        for token in content:
            parsed_word = analyzer.parse(token)
            if parsed_word[0].tag.POS in functors_pos: continue
            f.write(token + '\n')


def sanitize_text(text_to_process):
    text_to_process = text_to_process.replace('.', ' ')
    text_to_process = text_to_process.replace('|', ' ')
    tokens = nltk.word_tokenize(text_to_process)
    return [token for token in tokens if token not in puncto and not contains_numeric(token)]


nltk.download('punkt')
RE_D: Final = re.compile('\d')
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
analyzer = pymorphy2.MorphAnalyzer()
puncto = [',', '.', ':', '?', '«', '»', '-', '(', ')', '!', '\'', '—', ';', '”', '...', '\"', '``', '@', '\'\'',
              '%', '--', '[', ']', '=', '+', '*', '\\', '$', '~', '&']
texts = dict()


for i in range(104):
    text = parse_text(i)
    text = sanitize_text(text)
    append_to_file('Words.txt', text)
    normalized_text = get_normal_form(text)
    texts.update(normalized_text)

with open("data/Lems.txt", 'a', encoding='utf-8') as f:
    for key, value in texts.items():
        f.write(key + ' ' + str.join(' ', value) + '\n')
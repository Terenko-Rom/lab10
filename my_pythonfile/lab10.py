import re
with open('sentences.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    declarative_sentences = re.findall(r'[^\?!.]+[.]', text)
    interrogative_sentences = re.findall(r'[^\?!.]+[?]', text)
    exclamatory_sentences = re.findall(r'[^\?!.]=[!]', text)
    declarative_count = len(declarative_sentences)
    interrogative_count = len(interrogative_sentences)
    exclamatory_count = len(exclamatory_sentences)
    print(f"Кількість слів: {word_count}")
    print(f"Кількість розповідних речень: {declarative_count}")
    print(f"Кількітсь питальних речень: {interrogative_count}")
    print(f"Кількість окличних речень: {exclamatory_count}")
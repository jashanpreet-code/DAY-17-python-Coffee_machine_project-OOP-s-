def extract_first_letter(word):
    word_in_sentence = word.split(' ')
    frist_word = [word[0] for word in word_in_sentence]
    return frist_word


print(extract_first_letter("asdfghj gygj gj gy bjguyg yftflu.b"))
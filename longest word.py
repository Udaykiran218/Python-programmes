def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("UDAY KIRAN IS A PERSON WHO VALUE VALUES"))  # 
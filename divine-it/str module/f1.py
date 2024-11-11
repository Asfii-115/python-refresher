def replace_vowels(text):
    s = str.maketrans('aeiou', '*****')
    return text.translate(s)

print(replace_vowels('hello world'))

def to_leetspeak(text):
    s = str.maketrans('AEIOST','431057')
    return text.translate(s)
print(to_leetspeak('LEET is COOL'))

def remove_punctuation(text):
    x=''
    s = str.maketrans(',!',)
    return text.translate(s)
print(remove_punctuation('Hello, World!'))


# Unicode string with escape sequences
s = "\u0041\u0042\u0043"  # ABC
print(s)

# Direct usage of Unicode characters
emoji = "😄"
print(emoji)

text = "Hello, 世界"
encoded_text = text.encode("utf-8")  # Encoding to UTF-8
print(encoded_text)

decoded_text = encoded_text.decode("utf-8")  # decoding to unicode
print(decoded_text)

# Using Unicode escape sequences
print("\u2764")  # ❤ (Heart)
print("\U0001F600")  # 😀 (Grinning face)
print("\N{GREEK CAPITAL LETTER ALPHA}")  # Α

print(ord("A"))  # 65
print(chr(65))  # A
print(ord("😄"))  # 128516
print(chr(128516))  # 😄

emoji_list = ["😀", "😂", "😎", "🤔", "❤️"]

for emoji in emoji_list:
    print(f"{emoji} - Code Point: {ord(emoji)}")

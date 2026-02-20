def reverse_words_in_sentence(s):
    words = s.split(' ')  # Split by space to preserve word positions
    reversed_words = []
    
    for word in words:
        reversed_words.append(word[::-1])  # Reverse each word
    
    return ' '.join(reversed_words)


# Example usage
print(reverse_words_in_sentence("Hello world"))
# Output: "olleH dlrow"

print(reverse_words_in_sentence("Python is fun"))
# Output: "nohtyP si nuf"

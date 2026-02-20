import string

def count_words(sentence):
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Remove punctuation
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    words = sentence.split()
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count


# Example 1
print(count_words("Hello hello world"))

# Example 2
print(count_words("Hi, Hi!"))

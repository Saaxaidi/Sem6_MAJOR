def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    
    vowel_list = []
    consonant_list = []
    
    for char in text:
        if char.isalpha():   # Check only alphabet characters
            if char in vowels:
                vowel_list.append(char)
            else:
                consonant_list.append(char)
    
    print("Vowels:", vowel_list)
    print("Number of vowels:", len(vowel_list))
    
    print("Consonants:", consonant_list)
    print("Number of consonants:", len(consonant_list))


# Example usage
text = "Hello World"
count_vowels_consonants(text)

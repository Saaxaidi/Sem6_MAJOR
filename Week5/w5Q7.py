def reverse_string(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        left += 1
        right -= 1


# Example usage
s = ['h', 'e', 'l', 'l', 'o']
reverse_string(s)
print(s)  

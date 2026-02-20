def remove_indentation(text):
    lines = text.split('\n')          # Split text into lines
    cleaned_lines = [line.lstrip() for line in lines]  # Remove leading spaces/tabs
    return '\n'.join(cleaned_lines)   # Join lines back together


# Example usage
sample_text = """
        Hello world
            This is Python
        Indentation removed
"""

result = remove_indentation(sample_text)
print(result)

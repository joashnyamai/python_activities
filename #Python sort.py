#Python sort
def sort_by_length(words):
    return sorted(words, key=len)

# Example usage:
words_list = ["apple", "banana", "kiwi", "grapefruit", "pear"]
print(sort_by_length(words_list))  # Output: ['kiwi', 'pear', 'apple', 'banana', 'grapefruit']

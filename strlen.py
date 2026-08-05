
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

if __name__ == "__main__":
    test_str = "programming"
    print(f"Vowels in '{test_str}': {count_vowels(test_str)}")
    print(f"Consonants in '{test_str}': {count_consonants(test_str)}")

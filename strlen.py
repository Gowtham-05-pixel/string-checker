def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_uppercase(s):
    return sum(1 for char in s if char.isupper())

if __name__ == "__main__":
    test_str = "programming"
    print(f"Vowels in '{test_str}': {count_vowels(test_str)}")
    print(f"Uppercase characters in '{test_str}': {count_uppercase(test_str)}")

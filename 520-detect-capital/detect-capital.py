class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_word = word.capitalize()
        if word.isupper() or word.islower():
            return True
        elif word == capital_word:
            return True
        return False
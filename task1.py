from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str) or not pattern:
            raise TypeError(f"Illegal argument for countWordsWithSuffix: pattern = {pattern} must be a string")
        
        result = 0
        for key in self.keys():
            if key.endswith(pattern): 
                result += 1
        return result     

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for hasPrefix: prefix = {prefix} must be a string")
       
        for key in self.keys():
           if key.startswith(prefix):
               return True
        return False
       

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat", "rat"]
    for i, word in enumerate(words):
        trie.put(word, i)


    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 2  # cat
    assert trie.count_words_with_suffix("o") == 0

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(f"Illegal argument for findLongestCommonWord: strings = {strings} must be a list of strings")
        
        for s in strings:
            if not isinstance(s, str):
                raise TypeError(f"Illegal argument for findLongestCommonWord: s = {s} must be a string")
            self.put(s)

        current = self.root
        common_prefix = []

        while current and len(current.children) == 1 and current.value is None:
            char, next_node = next(iter(current.children.items()))
            common_prefix.append(char)
            current = next_node

        return "".join(common_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

class WordDictionary {
private:
    unordered_map<char, WordDictionary*> dict;
    bool isEndOfWord = false;

public:
    WordDictionary() {}

    void addWord(string word) {
        if (word.empty()) {
            isEndOfWord = true;
            return;
        }
        if (!dict.contains(word[0]))
            dict[word[0]] = new WordDictionary();
        dict[word[0]]->addWord(word.substr(1));
    }

    bool search(string word) {
        if (word.empty()) return isEndOfWord;

        char c = word[0];
        string rest = word.substr(1);

        if (c != '.') {
            return dict.contains(c) && dict[c]->search(rest);
        } 
        else {
            for (const auto& [key, node] : dict) {
                if (node->search(rest)) return true;
            }
            return false;
        }
    }
};
class Solution {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        string word = "";
    };

    TrieNode* root = new TrieNode();

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        for (const string& word : words) {
            insert(word);
        }

        vector<string> ans;

        int rows = board.size();
        int cols = board[0].size();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                dfs(board, r, c, root, ans);
            }
        }

        return ans;
    }

private:
    void insert(const string& word) {
        TrieNode* curr = root;

        for (char ch : word) {
            if (!curr->children.count(ch)) {
                curr->children[ch] = new TrieNode();
            }

            curr = curr->children[ch];
        }

        curr->word = word;
    }

    void dfs(vector<vector<char>>& board, int row, int col, TrieNode* node, vector<string>& ans) {
        int rows = board.size();
        int cols = board[0].size();

        if (row < 0 || row >= rows || col < 0 || col >= cols) {
            return;
        }

        char ch = board[row][col];

        if (ch == '#') {
            return;
        }

        if (!node->children.count(ch)) {
            return;
        }

        TrieNode* nextNode = node->children[ch];

        if (!nextNode->word.empty()) {
            ans.push_back(nextNode->word);

            // Prevent duplicate answers.
            nextNode->word = "";
        }

        board[row][col] = '#';

        dfs(board, row + 1, col, nextNode, ans);
        dfs(board, row - 1, col, nextNode, ans);
        dfs(board, row, col + 1, nextNode, ans);
        dfs(board, row, col - 1, nextNode, ans);

        board[row][col] = ch;
    }
};
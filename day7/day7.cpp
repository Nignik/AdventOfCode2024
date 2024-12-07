#include <bits/stdc++.h>
using namespace std;

// Not actually used, but we include for completeness
void LOG(const string &file_name, const string &smth) {
    if (file_name.find("test.in") != string::npos) {
        cout << smth << "\n";
    }
}

vector<vector<string>> load_data(const string &file_name) {
    ifstream f(file_name);
    vector<vector<string>> res;
    if (!f.is_open()) {
        cerr << "Failed to open file: " << file_name << "\n";
        return res;
    }

    string line;
    while (std::getline(f, line)) {
        // Split by ": "
        size_t pos = line.find(": ");
        if (pos == string::npos) continue;
        string left_part = line.substr(0, pos);
        string right_part = line.substr(pos + 2);

        // Use regex to split right_part into tokens of \S+ or \s+
        std::regex re("(\\S+|\\s+)");
        std::sregex_iterator begin(right_part.begin(), right_part.end(), re), end;
        
        vector<string> tokens;
        for (auto it = begin; it != end; ++it) {
            tokens.push_back(it->str());
        }

        // The resulting row is [left_part, tokens...]
        // But in original code, row[0] = target, row[1] = tokens vector
        // We store them as: row = [target, token0, token1, ...]
        // In Python code, row[1] was a list of tokens. We'll emulate similarly:
        // We'll keep row[0] as the target and row[1..end] as the tokens.
        
        vector<string> row;
        row.push_back(left_part);
        // Append all tokens from right_part
        for (auto &t : tokens) {
            row.push_back(t);
        }

        res.push_back(row);
    }
    return res;
}

int get_i(int num, int i) {
    // get_i function: return i-th digit (from right, 0-based) of num in base 3
    string base3;
    if (num == 0) {
        // If num=0, then base3="0"
        base3 = "0";
    } else {
        while (num > 0) {
            int d = num % 3;
            base3.push_back('0' + d);
            num /= 3;
        }
        reverse(base3.begin(), base3.end());
    }
    if ((int)base3.size() - 1 - i >= 0) {
        return base3[(int)base3.size() - 1 - i] - '0';
    } else {
        return 0;
    }
}

long long sol1(const string &file_name) {
    auto data = load_data(file_name);
    long long ans = 0;

    for (auto &row : data) {
        vector<int> spaces;
        for (int i = 1; i < (int)row.size(); i++) {
            if (row[i] == " ") {
                spaces.push_back(i);
            }
        }

        long long target = stoll(row[0]);
        int n_spaces = (int)spaces.size();
        long long limit = (long long)pow(2, n_spaces);

        for (long long i = 0; i < limit; i++) {
            long long res = stoll(row[1]);
            for (int j = 0; j < n_spaces; j++) {
                int space_idx = spaces[j];
                long long next_num = stoll(row[space_idx + 1]);
                if ((i >> j) & 1) {
                    res *= next_num;
                } else {
                    res += next_num;
                }
            }
            if (res == target) {
                ans += res;
                break;
            }
        }
    }

    return ans;
}

long long sol2(const string &file_name) {
    auto data = load_data(file_name);
    long long ans = 0;

    for (auto &row : data) {
        vector<int> spaces;
        for (int i = 1; i < (int)row.size(); i++) {
            if (row[i] == " ") {
                spaces.push_back(i);
            }
        }

        long long target = stoll(row[0]);
        int n_spaces = (int)spaces.size();
        long long limit = (long long)pow(3, n_spaces);

        for (long long i = 0; i < limit; i++) {
            long long res = stoll(row[1]);
            for (int j = 0; j < n_spaces; j++) {
                int op = get_i((int)i, j);
                long long next_num = stoll(row[spaces[j] + 1]);
                if (op == 0) {
                    res *= next_num;
                } else if (op == 1) {
                    res += next_num;
                } else {
                    string new_val = to_string(res) + row[spaces[j] + 1];
                    res = stoll(new_val);
                }
            }
            if (res == target) {
                ans += res;
                break;
            }
        }
    }

    return ans;
}


int main() {
    cout << "Star 1:\n test: " << sol1("test.in") << "\n answer: " << sol1("input.in") << "\n\n";
    cout << "Star 2:\n test: " << sol2("test.in") << "\n answer: " << sol2("input.in") << "\n";

    return 0;
}

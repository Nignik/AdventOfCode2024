#include <bits/stdc++.h>
using namespace std;

static long long A, B, C;

vector<long long> load_data(const string &file_name) {
    ifstream infile(file_name);
    if (!infile.is_open()) {
        cerr << "Could not open file: " << file_name << "\n";
        exit(1);
    }

    string line;
    vector<long long> regs;
    vector<long long> program;
    int line_count = 0;

    std::regex re("\\d+"); // Regex to match one or more digits
    while (std::getline(infile, line)) {
        vector<long long> nums;
        {
            std::smatch match;
            string temp = line;
            while (std::regex_search(temp, match, re)) {
                nums.push_back(std::stoll(match.str()));
                temp = match.suffix().str();
            }
        }

        // First 3 lines: regs
        if (line_count < 3) {
            for (auto &v : nums) regs.push_back(v);
        } else if (line_count > 3) {
            for (auto &v : nums) program.push_back(v);
        }
        line_count++;
    }

    // Combine regs and program into a single vector:
    vector<long long> result;
    result.insert(result.end(), regs.begin(), regs.end());
    result.insert(result.end(), program.begin(), program.end());
    return result;
}

long long sol(const string &file_name) {
    vector<long long> data = load_data(file_name);
    // The first three values are regs:
    A = data[0]; B = data[1]; C = data[2];
    vector<long long> program(data.begin() + 3, data.end());

    cout << "[" << A << ", " << B << ", " << C << "] ";
    cout << "[";
    for (size_t i = 0; i < program.size(); i++) {
        cout << program[i] << (i+1<program.size()? ", ":"");
    }
    cout << "]\n";

    auto combo = [&](long long op) -> long long {
        if (op <= 3) return op;
        else if (op < 7) {
            switch (op - 4) {
                case 0: return A;
                case 1: return B;
                case 2: return C;
            }
        }
        // Should not reach here
        return 0;
    };

    unsigned long long x = 0ULL;
    while (x <= 10000000000ULL) {
        A = (long long)x;
        string res;
        size_t i = 0;
        while (i < program.size()) {
            long long opc = program[i];
            long long op = program[i+1];
            switch (opc) {
                case 0:
                {
                    // Use bit shifts if combo(op) is small and non-negative
                    long long shift = combo(op);
                    if (shift < 0) shift = 0; // just a safety
                    long long div_val = (1LL << shift);
                    A = A / div_val;
                    break;
                }
                case 1:
                    B ^= op;
                    break;
                case 2:
                    B = combo(op) % 8;
                    break;
                case 3:
                    if (A != 0) {
                        i = (size_t)(op - 2);
                    }
                    break;
                case 4:
                    B ^= C;
                    break;
                case 5:
                {
                    long long val = combo(op) % 8;
                    res.push_back((char)('0' + (int)val));
                    break;
                }
                case 6:
                {
                    long long shift = combo(op);
                    if (shift < 0) shift = 0;
                    long long div_val = (1LL << shift);
                    B = A / div_val;
                    break;
                }
                case 7:
                {
                    long long shift = combo(op);
                    if (shift < 0) shift = 0;
                    long long div_val = (1LL << shift);
                    C = A / div_val;
                    break;
                }
                default:
                    break;
            }

            i += 2;
        }

        x += 1;
        if (x % 100000 == 0) {
            cout << x << "\n";
            cout << "res: [";
            for (size_t k = 0; k < res.size(); k++) cout << res[k] << (k+1<res.size()? ", ":"");
            cout << "] program: [";
            for (size_t k = 0; k < program.size(); k++) cout << program[k] << (k+1<program.size()? ", ":"");
            cout << "]\n";
        }

        // Check if res matches program as a list of ints
        if (res.size() == program.size()) {
            bool match = true;
            for (size_t idx = 0; idx < res.size(); idx++) {
                if ((res[idx] - '0') != program[idx]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                break;
            }
        }
    }

    return (long long)x - 1;
}

int main() {
    cout << "Test: " << sol("test.in") << "\n";
    cout << "Answer: " << sol("input.in") << "\n";
    return 0;
}

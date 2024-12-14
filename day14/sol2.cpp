#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <sstream>
#include <regex>
#include <numeric>
#include <cmath>

using namespace std;

struct Vector2i {
    int x, y;

    Vector2i() : x(0), y(0) {}
    Vector2i(int x, int y) : x(x), y(y) {}

    Vector2i operator+(const Vector2i& other) const {
        return Vector2i(x + other.x, y + other.y);
    }

    Vector2i operator*(int scalar) const {
        return Vector2i(x * scalar, y * scalar);
    }

    bool operator==(const Vector2i& other) const {
        return x == other.x && y == other.y;
    }

    Vector2i& operator%=(const Vector2i& dims) {
        x %= dims.x;
        y %= dims.y;
        return *this;
    }

    bool all_less_than(const Vector2i& other) const {
        return x < other.x && y < other.y;
    }

    bool any_greater_than(const Vector2i& other) const {
        return x > other.x || y > other.y;
    }
};

void log(const string& file_name, const string& smth) {
    if (file_name.find("test.in") != string::npos) {
        cout << smth << endl;
    }
}

vector<pair<Vector2i, Vector2i>> load_data(const string& file_name) {
    ifstream file(file_name);
    string line;
    vector<pair<Vector2i, Vector2i>> result;

    regex pattern("-?\\d+");
    while (getline(file, line)) {
        smatch match;
        auto begin = sregex_iterator(line.begin(), line.end(), pattern);
        auto end = sregex_iterator();

        vector<int> numbers;
        for (auto it = begin; it != end; ++it) {
            numbers.push_back(stoi(it->str()));
        }

        Vector2i position(numbers[0], numbers[1]);
        Vector2i velocity(numbers[2], numbers[3]);
        result.emplace_back(position, velocity);
    }

    return result;
}

int get_quadrant(const Vector2i& pos, const Vector2i& dims) {
    array<Vector2i, 4> quads = {
        Vector2i(dims.x / 2, dims.y / 2),
        Vector2i(dims.x, dims.y / 2),
        Vector2i(dims.x / 2, dims.y),
        Vector2i(dims.x, dims.y)
    };

    if (pos.all_less_than(quads[0])) {
        return 0;
    } else if (pos.any_greater_than(quads[0]) && pos.all_less_than(quads[1])) {
        return 1;
    } else if (pos.any_greater_than(quads[0]) && pos.all_less_than(quads[2])) {
        return 2;
    } else if (pos.x > quads[2].x && pos.y > quads[1].y) {
        return 3;
    }

    return -1;
}

void sol1(const string& file_name, const Vector2i& dims) {
    auto robots = load_data(file_name);

    for (int i = 1; i < 40000; ++i) {
        array<int, 4> quad_cnt = {0, 0, 0, 0};
        vector<Vector2i> positions;

        for (const auto& [p, v] : robots) {
            Vector2i pos = p + v * i;
            pos %= dims;
            positions.push_back(pos);

            int quad = get_quadrant(pos, dims);
            if (quad != -1) {
                quad_cnt[quad]++;
            }
        }

        if (file_name.find("input") != string::npos) {
          std::cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! " << i << std::endl;
            for (int r = 0; r < dims.y; ++r) {
                for (int c = 0; c < dims.x; ++c) {
                    int count = count_if(positions.begin(), positions.end(), [&](const Vector2i& pos) {
                        return pos == Vector2i(c, r);
                    });
                    cout << (count > 0 ? "#" : ".") << "";
                }
                cout << endl;
            }
            cout << endl;
        }
    }
}

int main() {
    cout << "Star 1:" << endl;
    cout << "test: ";
    sol1("test.in", Vector2i(11, 7));
    cout << "answer: ";
    sol1("input.in", Vector2i(101, 103));

    return 0;
}

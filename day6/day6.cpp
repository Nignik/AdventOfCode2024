#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <tuple>
#include <set>
#include <array>
#include <algorithm>

using namespace std;

// Directions as constant arrays
const array<pair<int, int>, 4> dirs = {{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};

void LOG(const string& file_name, const string& smth) {
    if (file_name.find("test.in") != string::npos) {
        cout << smth << ' ';
    }
}

tuple<vector<vector<char>>, pair<int, int>> load_data(const string& file_name) {
    ifstream file(file_name);
    vector<vector<char>> grid;
    pair<int, int> spawn = {0, 0};

    if (!file.is_open()) {
        cerr << "Error: Unable to open file " << file_name << endl;
        return {{}, {-1, -1}};
    }

    string line;
    int row = 0;
    while (getline(file, line)) {
        auto idx = line.find('^');
        if (idx != string::npos) {
            spawn = {row, static_cast<int>(idx)};
        }
        grid.push_back(vector<char>(line.begin(), line.end()));
        row++;
    }

    return {grid, spawn};
}

int sol1(const string& file_name) {
    auto [grid, spawn] = load_data(file_name);

    pair<int, int> pos = spawn;
    set<pair<int, int>> visited;
    int dir = 0;

    while (pos.first >= 0 && pos.first < grid.size() && pos.second >= 0 && pos.second < grid[0].size()) {
        if (grid[pos.first][pos.second] == '#') {
            pos = {pos.first - dirs[dir].first, pos.second - dirs[dir].second};
            dir = (dir + 1) % 4;
        }

        visited.insert(pos);
        pos = {pos.first + dirs[dir].first, pos.second + dirs[dir].second};
    }

    return visited.size();
}

bool check(vector<vector<char>>& grid, int r, int c, const pair<int, int>& spawn) {
  grid[r][c] = '#';
  pair<int, int> pos = spawn;
  int dir = 0;
  vector<bool> vis(1000000, false);
  int hash = 0;

  while (true) {
    if (pos.first < 0 || pos.first >= grid.size() || pos.second < 0 || pos.second >= grid[0].size()) {
      grid[r][c] = '*';
      return false;
    }

    if (grid[pos.first][pos.second] == '#') {
      pos = {pos.first - dirs[dir].first, pos.second - dirs[dir].second};
      dir = (dir + 1) % 4;
    }

    hash = (pos.second * grid[0].size() + pos.first) * 4 + dir;
    if (vis[hash]) {
      break;
    }

    vis[hash] = true;
    pos = {pos.first + dirs[dir].first, pos.second + dirs[dir].second};
  }

  grid[r][c] = '*';
  return true;
}

int sol2(const string& file_name) {
    auto [grid, spawn] = load_data(file_name);
    int ans = 0;

    for (size_t r = 0; r < grid.size(); ++r) {
        for (size_t c = 0; c < grid[r].size(); ++c) {
            if (grid[r][c] != '.') continue;

            if (check(grid, r, c, spawn)) {
                ans++;
            }
        }
    }

    return ans;
}

int main() {
    cout << "Star 1:\n"
         << " test: " << sol1("test.in") << "\n"
         << " answer: " << sol1("input.in") << "\n";
    cout << "Star 2:\n"
         << " test: " << sol2("test.in") << "\n"
         << " answer: " << sol2("input.in") << "\n";

    return 0;
}

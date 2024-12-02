#include <bits/stdc++.h>
#include <filesystem>

namespace fs = std::filesystem;

bool check(std::vector<int>& report) {
  bool ok = true, ascending = true, descending = true;
  for (int i = 1; i < report.size(); i++) {
    int diff = report[i] - report[i-1];
    if (diff > 0)
      descending = false;
    if (diff < 0)
      ascending = false;

    if (abs(diff) < 1 || abs(diff) > 3) {
      ok = false;
      break;
    }
  }

  return ok && (ascending || descending);
}

int solve2(std::vector<std::vector<int>> reports) {
  int ans = 0;
  bool isOk = false;

  auto consider = [&](std::vector<int>& report, int i) {
    auto rep = report;
    rep.erase(rep.begin() + i);
    if (check(rep)) {
      isOk = true;
    }
  };

  for (auto& report : reports) {
    consider(report, report.size()-1);
    for (int i = 1; i < report.size(); i++) {
      int diff = report[i] - report[i-1];
      if (abs(diff) < 1 || abs(diff) > 3) {
        consider(report, i-1);
        consider(report, i);
        break;
      }
      
      if (i + 1 < report.size()) {
        if ((diff < 0) != (report[i+1] - report[i] < 0)) {
          consider(report, i-1);
          consider(report, i);
          consider(report, i+1);
          break;
        }
      }
    }

    if (isOk) {
      ans++;
      isOk = false;
    }
  }

  return ans;
}

int main() {
  std::vector<std::vector<int>> reports;
  fs::path input_path = "input.in";
  fs::path test_path = "test.in";

  std::ifstream input;
  std::ifstream test;
  input.open(input_path);
  test.open(test_path);

  std::string line;
  while (std::getline(input, line)) {
    reports.resize(reports.size()+1);
    auto& report = reports.back();
    auto iss = std::istringstream(line);
    int num;
    while (iss >> num)
      report.push_back(num);
  }

  std::cout << "Answer: " << solve2(reports) << std::endl;
}
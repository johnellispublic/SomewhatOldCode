#include <iostream>

int main(int argc, char const *argv[]) {

  int const EOF_ = 5;

  if (argc > 1) {
    std::cout << argv[1];
  }
  else {
    std::cout << "No\nInput";
  }
  std::cout << (char) EOF_;
  return 0;
}

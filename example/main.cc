#include <iostream>

// If compile_commands.json + clangd is correctly configured, this should
// pull in library/math.h, not the system's math.h.
// You will likely need to build this executable before this works.
#include "math.h"

int main() {
  auto s = multiply(1, 2);
  std::cout << s << std::endl;
}

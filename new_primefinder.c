#include <stdio.h>
#include <limits.h>

int validate_number(char *strn){
  for (char *digit = strn; *digit != 0; digit++) {
    if (!('0' <= *digit && *digit <= '9')) {
      return 0;
    }
  }
  return 1;
}

int int_pow(int base, int exp){
  int result = 1;
  for (int i=0; i<exp; i++) {
    result *= base;
  }
  return result;
}

void str_to_int(char *strn, unsigned long int *n) {
  char *endn = strn;
  char *digit;
  int len = 0;
  *n = 0;

  while (*endn != 0) {endn++; len++; }

  digit = endn;

  for (int i = len-1; i >= 0; i--){
    digit--;
    *n += int_pow(10, len-i-1)*(*digit-'0');
  }
}

unsigned long int min(unsigned long int a, unsigned long int b) {
  if (a < b) {
    return a
  }
  else {
    return b
  }
}

int prime_sieve(unsigned long int maxn, unsigned long int primes[], ) {
  char numbers[UINT_MAX];
}

int main(int argc, char const *argv[]) {
  unsigned long int maxn;

  if (argc == 1) {
    printf("Usage: new_primefinder.o <maxn>\n");
  }

  else if (!validate_number(argv[1]))
  {
    printf("%s is not a valid number.\n", argv[1]);
  }

  else {
    str_to_int(argv[1], &maxn);
    printf("maxn: %lu\n", maxn);
  }
  return 0;
}

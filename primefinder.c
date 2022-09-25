#include <math.h>
#include <stdio.h>

void calc_primes(unsigned char *ptr, unsigned char *minptr, unsigned char *maxptr) {
  unsigned char *startptr = ptr;
  long int n = 2;
  ptr += 2;
  do {
    n = ptr - minptr;
    if (*ptr) {
      for (unsigned char* i = ptr; i <= maxptr; i += n) {*i = 0;}
    }
    ptr++;
  } while (n < sqrt(maxptr - minptr));
}

int main(int argc, char const *argv[]) {
  unsigned char primes[1000000000] = {1};
  unsigned char *ptr = primes;
  unsigned char *minptr = ptr;
  unsigned char *maxptr = &primes[sizeof(primes)-1];
  calc_primes(ptr, minptr, maxptr);
  for (int n = 0; n < sizeof(primes); n++) {
    if (primes[n]) {printf("%6d",n);}
  }
  return 0;
}

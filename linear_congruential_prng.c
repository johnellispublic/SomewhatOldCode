#include <stdio.h>

struct IntSortingPair {
  int value;
  int priority;
};

struct MIPSQuad {
  int m;
  int i;
  int p;
  int s;
};

struct MIPSQuadSortingPair {
  struct MIPSQuad value;
  int priority;
};

struct Range {
  int min;
  int max;
};

int get_loop_size(int m, int i, int p, int seed) {
  int loop_length = 0;
  int n = seed;

  do {
    n = (m*n + i) % p;
    loop_length++;
  } while(n != seed && loop_length <= p);

  return loop_length;
};

struct IntSortingPair get_max_loop_size(int m, int i, int p, struct Range srange) {
  struct IntSortingPair max;
  max.priority = -1;
  int length;

  for (int seed = srange.min; seed < srange.max; seed++) {
    length = get_loop_size(m, i, p, seed);
    if (length >= max.priority && length < p) {
      max.value = seed;
      max.priority = length;
    }
  }
  return max;
};

struct MIPSQuadSortingPair get_best_value(struct Range mrange, struct Range irange, struct Range prange, struct Range srange) {
  struct MIPSQuadSortingPair max;
  max.priority = -1;
  struct IntSortingPair loop_size;

  for (int m = mrange.min; m < mrange.max; m++) {
    for (int i = irange.min; i < irange.max; i++) {
      for (int p = prange.min; p < prange.max; p++) {
        loop_size = get_max_loop_size(m, i, p, srange);
        if (loop_size.priority > max.priority) {
          max.value.m = m;
          max.value.i = i;
          max.value.p = p;
          max.value.s = loop_size.value;
          max.priority = loop_size.priority;
        }
        printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
        printf("%03d %03d %03d this=%03d MAX=%03d", m, i, p, loop_size.priority, max.priority);
      }
    }
  }
  return max;
};

int main(int argc, char const *argv[]) {
  struct MIPSQuadSortingPair max;
  struct Range mrange, irange, prange, srange;
  mrange.min = 1; mrange.max = 301;
  irange.min = 1; irange.max = 301;
  prange.min = 250; prange.max = 301;
  srange.min = 99; srange.max = 100;
  max = get_best_value(mrange, irange, prange, srange);
  printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
  printf("m=%d i=%d p=%d s=%d loop=%d \n", max.value.m, max.value.i, max.value.p, max.value.s, max.priority);
  return 0;
};

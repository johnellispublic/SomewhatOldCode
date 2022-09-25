#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define true 1
#define false 0

void add_base(FILE *base, FILE *out) {
  char character;
  do {
    character = fgetc(base);
    if (character == EOF) { break; }
    fprintf(out, "%c", character);
  } while (true);
}

void compile(FILE *in, FILE *out, int *GlobalLoopID) {
  char command;
  int completed = false;
  int LoopID = *GlobalLoopID;
  fprintf(out, ".Loop%d:\n", LoopID);
  ++*GlobalLoopID;

  do {
    command = fgetc(in);
    switch (command) {
      case EOF:
        completed = true;
        break;
      case '+': fprintf(out, "\tcall incr\n"); break;
      case '-': fprintf(out, "\tcall decr\n"); break;
      case '>': fprintf(out, "\tcall ptrinc\n"); break;
      case '<': fprintf(out, "\tcall ptrdec\n"); break;
      case ',': fprintf(out, "\tcall ioin\n"); break;
      case '.': fprintf(out, "\tcall ioout\n"); break;
      case '[': compile(in, out, GlobalLoopID); break;
      case ']':
        fprintf(out, "\ttest ax, ax\n");
        fprintf(out, "\tje .Loop%d\n", LoopID);
        fprintf(out, ".EndLoop%d:\n", LoopID);
        completed = true;
        break;
    };
  } while (!completed);

}


int main(int argc, char const *argv[]) {
  FILE *in;
  FILE *base;
  FILE *out;
  char *basefile = "base.asm";
  int LoopID = 0;

  if (argc <= 2) { return 0; }
  else {
    in = fopen(argv[1], "r");
    base = fopen(basefile, "r");
    out = fopen(argv[2], "w");

    add_base(base, out);
    compile(in, out, &LoopID);
    fprintf(out, "\tret");
  }
  return 0;
}

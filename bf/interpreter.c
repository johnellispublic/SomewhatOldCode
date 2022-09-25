#include <stdio.h>
#include <string.h>
#include <ctype.h>

void escape_char(unsigned char *ch, unsigned char *out, unsigned char default_val) {
  out[0] = '\\';
  switch (*ch) {
    case '\a':
      out[1] = 'a';
      break;
    case '\b':
      out[1] = 'b';
      break;
    case '\e':
      out[1] = 'e';
      break;
    case '\f':
      out[1] = 'f';
      break;
    case '\n':
      out[1] = 'n';
      break;
    case '\r':
      out[1] = 'r';
      break;
    case '\t':
      out[1] = 't';
      break;
    case '\v':
      out[1] = 'v';
      break;

    default:
      out[0] = default_val;
      if (iscntrl(*ch)){
        out[1] = default_val;
      }
      else {
        out[1] = *ch;
      }
      break;
  }
}

int compute(unsigned char **ptr, unsigned char *minptr, unsigned char *maxptr, int line, FILE *in, int verbose){
  int startline = line;
  char command;
  int skip_block = 0;
  int block_lvl = 0;
  int is_default;
  unsigned char escaped_value[2];
  unsigned char escaped_output[2];

  do {
    command = fgetc(in);
    ++line;
    //printf("%d\n", (int) *ptr);

    if (skip_block & block_lvl > 0) {
      switch (command){
        case '[': ++block_lvl; break;
        case ']': --block_lvl; break;
      }
      if (block_lvl == 0) {skip_block = 0;}
    }

    else {
      is_default = 0;
      switch (command) {
        case '+': ++**ptr; break;
        case '-': --**ptr; break;
        case '>': ++*ptr; break;
        case '<': --*ptr; break;
        case '.':
          if (verbose) {printf("------------------------------------------");}
          if (verbose) {escape_char(*ptr, escaped_output, '-'); printf("%2s", escaped_output);}
          else {putchar(**ptr);}
          if (verbose) {printf("------------------------------------------\n");}
          break;

        case ',':
          if (verbose) {printf("------------------------------------------");}
          **ptr = getchar();
          if (verbose) {printf("------------------------------------------\n");}
          break;

        case '[':
          if (**ptr) {
            line = compute(ptr, minptr, maxptr, line, in, verbose);
            fseek(in, line, SEEK_SET);
          }
          else {++block_lvl; skip_block = 1;}
          break;
        case ']':
          if (**ptr) {fseek(in, startline, SEEK_SET); line = startline; }
          else {return line;}
          break;

        default:
          is_default = 1;
          break;
      }

      if (*ptr > maxptr) {*ptr = minptr;}
      if (*ptr < minptr) {*ptr = maxptr;}

      if (! is_default & verbose) {
        escape_char(*ptr, escaped_value, ' ');
        printf("%4u|%3lu >> %02x | %.2s | %c\n",line,*ptr-minptr, **ptr, escaped_value, command);
      }

    }


  } while ( command != EOF);
  return line;
}

int main(int argc, char const *argv[]) {
  unsigned char array[30000] = {0};
  unsigned char *ptr = array;
  unsigned char *minptr = ptr;
  unsigned char *maxptr = &array[sizeof(array)-1];
  FILE *in;
  int verbose = 0;
  int display_memory = 0;

  if (argc == 1)
  { return 0; }
  else
  { in = fopen(argv[argc-1], "r"); }

  for (int i = 1; i<argc-1; i++) {
    if (strcmp(argv[i],"-V") == 0) { verbose = 1; }
    if (strcmp(argv[i],"-s") == 0) { display_memory = 1; }
  }

  compute(&ptr, minptr, maxptr, 0, in, verbose);
  if (display_memory) {
    printf("\n");
    int array_len = sizeof(array) - 1;
    while (array[array_len] == 0 & array_len > 0) { --array_len; }
    for (int i = 0; i <= array_len; i++) { printf("%02x ", array[i]); }
    printf("\n");
  }

  return 0;
}

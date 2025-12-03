#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>

#define SIZE 4096

int main(int argc, char** argv) {
  clock_t begin = clock();
  if (argc < 2) {
    printf("./password <inputfile.txt>\n");
    exit(EXIT_FAILURE);
  }
  int zero_count = 0;
  int dial = 50;
  
  int fd = open(argv[1], O_RDONLY);
  if (!fd) { perror("Open"); return -1; }

  ssize_t bytes;
  char buffer[SIZE];
  int i = 0;
  int digit = 0;
  
  while( (bytes = read(fd, &buffer[i], 1) ) > 0) {
    if (buffer[i] == '\n' || i == SIZE -1) {
      buffer[i+1] = '\0';
      i = 0;
      char string[5];
      snprintf(string, 7, "%c%c%c",buffer[i+1], buffer[i+2], buffer[i+3]);
      digit = atoi(string);
      if (buffer[i] == 'L') digit = -digit;

      dial = ( dial + digit ) % 100;
      if (dial < 0) dial = 100 + dial;
      if (dial == 0) 
				zero_count+=1;
    } else i++;
  }
  close(fd);
  
  printf("Il numero di zero e' %d \n", zero_count);
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time running: %f \n", time_spent);
  return 0;
}

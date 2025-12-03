#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>

#define SIZE 4096

long long checkRepeat(char* number) {
  int len = strlen(number);

  if (len % 2 != 0) {
    return 0;
  }
  
  char cpy1[15], cpy2[15];
  strncpy(cpy1, number, len/2);
  cpy1[len/2] = '\0';
  strncpy(cpy2, number + (len/2), len/2);
  cpy2[len/2] = '\0';

  if (!strcmp(cpy1, cpy2) ) {
    return atoll(number);
  }
  return 0;
}

long long splitIDs(char* str) {
  long long start, end; 
  long long sum = 0;
  char *ptr2;
  char copy[100], string[30];
  strcpy(copy, str);
  
  start = strtoll(copy, &ptr2, 10);
  if (*ptr2 != '-') return 0;
  end = strtoll(ptr2+1, NULL, 10); 
  for (long long i = start; i <= end; i++) {
    snprintf(string, sizeof(string), "%lld", i);
    sum += checkRepeat(string);
  }

  return sum;
}

int main(int argc, char **argv) {
  clock_t begin = clock();
  if (argc < 2) {
    printf("./addInvalidIds <inputfile.txt>\n");
    exit(EXIT_FAILURE);
  }
  long long int sum = 0;
  
  int fd = open(argv[1], O_RDONLY);
  if (!fd) { perror("open"); exit(EXIT_FAILURE);}
  
  ssize_t bytes; 
  char buf[SIZE];
  bytes = read(fd, buf, SIZE);
  
  char *ptr1;
  char* token = strtok_r(buf, ",", &ptr1);
  while(token != NULL)  {
    sum += splitIDs(token);
    token = strtok_r(NULL, ",", &ptr1);
  }
  close(fd);
  char toString[100];
  sprintf(toString, "%ld", sum);

  printf("la somma degli ID invalidi e' %s\n", toString);
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time running: %f \n", time_spent);
  return 0;
}

PROG=hello

CC=gcc
CFLAGS= -g -Wall -O3


SRCS = $(wildcard *.c source/*.c)
OBJS = $(patsubst %c, %o, $(SRCS))


%.o: %c
	$(CC) $(CFLAGS) -o $@ $<


all : $(PROG)

$(PROG): $(OBJS)
	$(CC) -o $@ $^ $(CFLAGS)


clean:
	rm -f *.o $(PROG)

.PHONY: all clean

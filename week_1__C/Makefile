CC = gcc
LDFLAGS = -lcs50

program1: name.c
	$(CC) -o name name.c $(LDFLAGS)

program2: conditionals.c
	$(CC) -o conditionals conditionals.c $(LDFLAGS)

program3: agree.c
	$(CC) -o agree agree.c $(LDFLAGS)

clean:
	rm -f *.o a.out core name conditionals

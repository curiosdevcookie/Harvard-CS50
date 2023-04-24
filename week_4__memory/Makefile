CC = gcc
LDFLAGS = -lcs50

program1: addresses.c
	$(CC) -o addresses addresses.c $(LDFLAGS)

program2: compare.c
	$(CC) -o compare compare.c $(LDFLAGS)

program3: get.c
	$(CC) -o get get.c $(LDFLAGS)

program4: uppercase.c
	$(CC) -o uppercase uppercase.c $(LDFLAGS)

program5: greetings.c
	$(CC) -o greetings greetings.c $(LDFLAGS)

program6: status.c
	$(CC) -o status status.c $(LDFLAGS)

clean:
	rm -f *.o a.out core addresses compare get uppercase greetings status

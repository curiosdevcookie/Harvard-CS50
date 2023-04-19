CC = gcc
LDFLAGS = -lcs50

program1: search.c
	$(CC) -o search search.c $(LDFLAGS)

program2: strings.c
	$(CC) -o strings strings.c $(LDFLAGS)

program3: string.c
	$(CC) -o string string.c $(LDFLAGS)

program4: uppercase.c
	$(CC) -o uppercase uppercase.c $(LDFLAGS)

program5: greetings.c
	$(CC) -o greetings greetings.c $(LDFLAGS)

program6: status.c
	$(CC) -o status status.c $(LDFLAGS)

clean:
	rm -f *.o a.out core search strings string uppercase greetings status

CC = g++
CFLAGS = -Ic:/Program\ Files\ \(x86\)/Jack/includes -Wall -std=c++1z
LDFLAGS= -Lc:/Program\ Files\ \(x86\)/Jack/lib -llibjack

all: example

example : jack_module.o main.o
	$(CC) -o $@ $(CFLAGS) jack_module.o main.o $(LDFLAGS)

.cpp.o:
	$(CC) -c $< $(CFLAGS)

clean:
	rm -f *.o
	rm -f example
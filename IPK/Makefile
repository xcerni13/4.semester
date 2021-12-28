CC=gcc
CFLAGS=-Wextra -std=c99 -Wall -pedantic -D_DEFAULT_SOURCE

ipk-sniffer: ipk_sniffer.o
	$(CC) $(CFLAGS) -o ipk_sniffer ipk_sniffer.o -lpcap

ipk_sniffer.o: ipk_sniffer.c
	$(CC) $(CFLAGS) -c ipk_sniffer.c

clean:
	rm *.o ipk_sniffer
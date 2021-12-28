####################################
        IPK Projekt 2
Zadanie ZETA - SNIFFER PACKETOV
####################################

Autor: Rebeka Černianska, xcerni13

Súbory: ipk-sniffer.c, Makefile, manual.pdf

##########
Všeobecné:
##########

Projekt 2 je implementovaný v jazyku C

#############################
Volanie programu:
#############################

sudo ./ipk-sniffer [-i rozhraní | --interface rozhraní] {-p ­­port} {[--tcp|-t] [--udp|-u] [--arp] [--icmp] } {-n num}

kde
-i eth0 (právě jedno rozhraní, na kterém se bude poslouchat. Nebude-li tento parametr uveden, či bude-li uvedené jen -i bez hodnoty, vypíše se seznam aktivních rozhraní)
-p 23 (bude filtrování paketů na daném rozhraní podle portu; nebude-li tento parametr uveden, uvažují se všechny porty; pokud je parametr uveden, může se daný port vyskytnout jak v source, tak v destination části)
-t nebo --tcp (bude zobrazovat pouze TCP pakety)
-u nebo --udp (bude zobrazovat pouze UDP pakety)
--icmp (bude zobrazovat pouze ICMPv4 a ICMPv6 pakety)
--arp (bude zobrazovat pouze ARP rámce)
Pokud nebudou konkrétní protokoly specifikovány, uvažují se k tisknutí všechny (tj. veškerý obsah, nehledě na protokol)
-n 10 (určuje počet paketů, které se mají zobrazit; pokud není uvedeno, uvažujte zobrazení pouze jednoho paketu)
argumenty mohou být v libovolném pořadí


##################
Jednotlivé súbory:
##################

Modul: ipk-sniffer.c 
zdrojový súbor programu, ktorý obsahuje všetky používané štruktúry, funkcie, a globálne premenné.

Makefile: 
príkaz make preloží moduly a vytvorí spustiteľný súbor
príkaz make clean vymaže aktuálne vytvorený spustiteľný súbor (ak existuje) a objektové súbory

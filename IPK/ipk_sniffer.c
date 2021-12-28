/*
  IPK PROJEKT 2 - packet sniffer
  Rebeka Černianska, xcerni13
  25.4.2021
*/

#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <stdbool.h>
#include <string.h>
#include <pcap.h>
#include <netinet/if_ether.h>
#include <time.h>
#include <netinet/ip_icmp.h>
#include <netinet/tcp.h>


#define MAX 100

static struct option long_options[] =
  {
    {"tcp", no_argument, 0, 't'},
    {"udp", no_argument, 0, 'u'},
    {"icmp", no_argument, 0, 'c'},
    {"arp", no_argument, 0, 'a'},
    {"help", no_argument, 0, 'h'},
    {0,0,0,0}
  };


void my_callback(unsigned char* args, const struct pcap_pkthdr* handle, const u_char *packet)
{
  time_t now;
  time(&now);
  struct tm *p = localtime(&now);
  char buf[100];
  size_t len = strftime(buf, sizeof buf - 1, "%FT%T%z", p);

  printf("%s ", buf);
  unsigned short iphdrlen;

  struct iphdr *iph = (struct iphdr *)( packet  + sizeof(struct ethhdr) );
  iphdrlen = iph->ihl*4;
  struct tcphdr* tcphdr;
  int header_size;
  struct sockaddr_in sour;
  struct sockaddr_in dest;
  switch (iph->protocol)
  {
      case 6: //TCP
            tcphdr = (struct tcphdr*)(packet + iphdrlen + sizeof(struct ethhdr));
            header_size =  sizeof(struct ethhdr) + iphdrlen + tcphdr->doff*4;
            memset(&sour, 0, sizeof(sour));
            sour.sin_addr.s_addr = iph->saddr;

            memset(&dest, 0, sizeof(dest));
            dest.sin_addr.s_addr = iph->daddr;

            printf("%s : %d > ",inet_ntoa(sour.sin_addr), tcphdr->source);
            printf("%s : %d,",inet_ntoa(dest.sin_addr), tcphdr->dest);
            break;
      default:
            exit(1);
  }

  fflush(stdout);
}


int main(int argc, char* argv[])
{
    int c;
    bool tcp = false;
    bool udp = false;
    bool icmp = false;
    bool arp = false;
    char i[MAX] = {'\0', };
    char p[MAX] = {'\0', };
    char n[MAX] = {'\0', };
    char error_buffer[MAX] = {'\0', };
    pcap_t *handle;
    struct bpf_program fp;		// The compiled filter expression
    char filter_exp[MAX] = {'\0', };
    bpf_u_int32 mask;
    bpf_u_int32 net;


    while((c = getopt_long(argc, argv, "i:p:tcn:", long_options, NULL)) != -1)
    {
      switch (c)
        {
            case 't':
                tcp = true;
                break;

            case 'u':
                udp = true;
                break;

            case 'c': //icmpv4/ICMPv6
                icmp = true;
                break;

            case 'a':
                arp = true;
                break;

            case 'h':
                printf ("Packet sniffer help - xcerni13 \n");
                printf ("-i eth0 (právě jedno rozhraní, na kterém se bude poslouchat. Nebude-li tento parametr uveden, či bude-li uvedené jen -i bez hodnoty, vypíše se seznam aktivních rozhraní) \n");
                printf ("-p 23 (bude filtrování paketů na daném rozhraní podle portu; nebude-li tento parametr uveden, uvažují se všechny porty; pokud je parametr uveden, může se daný port vyskytnout jak v source, tak v destination části) \n");
                printf ("-t nebo --tcp (bude zobrazovat pouze TCP pakety) \n");
                printf ("-u nebo --udp (bude zobrazovat pouze UDP pakety) \n");
                printf ("--icmp (bude zobrazovat pouze ICMPv4 a ICMPv6 pakety) \n");
                printf ("--arp (bude zobrazovat pouze ARP rámce) \n");
                printf ("Pokud nebudou konkrétní protokoly specifikovány, uvažují se k tisknutí všechny (tj. veškerý obsah, nehledě na protokol) \n");
                printf ("-n 10 (určuje počet paketů, které se mají zobrazit; pokud není uvedeno, uvažujte zobrazení pouze jednoho paketu) \n");
                printf ("argumenty mohou být v libovolném pořadí \n");
                break;

            case 'i':
                strcpy(i, optarg);
                break;

            case 'p':
                strcpy(p, optarg);
                break;

            case 'n':
                strcpy(n, optarg);
                break;

          default:
              fprintf(stderr, "Error parsing arguments\n");
              return 1;
        }
    }

    for (int i = 0; i < argc; i++)
    {
        for (int j = (i + 1); j < argc; j++)
        {
            if (!strcmp(argv[i], argv[j]))
            {
                fprintf(stderr, "Arguments repeating\n");
                return 1;
            }
        }
    }
    //setting filter
    if (tcp == false && udp == false && icmp == false && arp == false) //not one protocol is specified
    {
        strcpy(filter_exp, "tcp or udp or icmp or arp");
    }
    else
    {
        if (tcp == true)
        {
            strcat(filter_exp, "tcp");
        }
        if (udp == true)
        {
            if (strlen(filter_exp) != 0)
            {
                strcat(filter_exp, " or ");
            }
            strcat(filter_exp, "udp");
        }
        if (icmp == true)
        {
            if (strlen(filter_exp) != 0)
            {
                strcat(filter_exp, " or ");
            }
            strcat(filter_exp, "icmp");
        }
        if (arp == true)
        {
            if (strlen(filter_exp) != 0)
            {
                strcat(filter_exp, " or ");
            }
            strcat(filter_exp, "arp");
        }
    }

    //checking port and adding it to filter
    if (strcmp(p, ""))
    {
        char *check = NULL;
        int port_num = strtol(p, &check, 10);
        if (strcmp(check,""))
        {
            fprintf(stderr, "Incorrect argument data with -p\n");
            return 1;
        }
        if ((port_num < 0) || (port_num > 65535))
        {
            fprintf(stderr, "Port number not within range \n");
            return 1;
        }

        char new_port[MAX] = {'\0', };
        strcpy(new_port, "port ");
        strcat(new_port, p);
        if (strlen(filter_exp) != 0)
        {
            strcat(filter_exp, " ");
        }
        strcat(filter_exp, new_port);
    }

    //opening sniffing session
    if (!strcmp(i, ""))
    {
        pcap_if_t *interfaces, *temp;
        pcap_findalldevs(&interfaces, error_buffer);
        int var = 0;
        for(temp=interfaces; temp; temp=temp->next)
        {
            printf("%d  :  %s\n",var++,temp->name);
        }
        exit(0);
    }
    else
    {
        if (pcap_lookupnet(i, &net, &mask, error_buffer) == -1)
        {
            fprintf(stderr, "Can't get netmask for device %s\n", i);
            net = 0;
            mask = 0;
        }

        handle = pcap_open_live(i, BUFSIZ, 1, 1000, error_buffer);
        if (handle == NULL)
        {
            fprintf(stderr, "Chyba pri otvarani pre sniffing - %s\n", error_buffer);
            exit(1);
        }
    }


    //compiling
    if (pcap_compile(handle, &fp, filter_exp, 0, net) == -1) {
		 fprintf(stderr, "Couldn't parse filter\n");
		 return 1;
	 }
     //setting filter
	 if (pcap_setfilter(handle, &fp) == -1) {
		 fprintf(stderr, "Couldn't install filter\n");
		 return(2);
	 }

     // setting data with -n argument if none are given
     if (!strcmp(n, "")){
         strcpy(n,"1");
     }

    //start sniffing individual packets
    char *check = NULL;
	int n_ok = strtol(n, &check, 10);
    if (strcmp(check, "") || (n_ok < 0))
    {
        fprintf(stderr, "Wrong data with argument -n\n");
        return 1;
    }
    pcap_loop(handle, n_ok, my_callback, NULL);
	pcap_close(handle);

    return 0;

}
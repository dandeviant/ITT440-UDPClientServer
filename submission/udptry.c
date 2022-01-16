// Server side implementation of UDP client-server model
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
   
#define PORT    12000
#define MAXLINE 1024

#define LINE_BUFSIZE 128
   
// Driver code
int main(int argc, char *argv[]) {
    int sockfd;
    char buffer[1024] = {0};
    char *hello = "Hello from server";
    struct sockaddr_in servaddr, cliaddr;
       
    // Creating socket file descriptor
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }
       
    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));
       
    // Filling server information
    servaddr.sin_family    = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);
       
    // Bind the socket with the server address
    if ( bind(sockfd, (const struct sockaddr *)&servaddr, 
            sizeof(servaddr)) < 0 )
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
       
    int len, n;
    char line[1024];
    FILE *pipe;

    len = sizeof(cliaddr);  //len is value/result
   
    n = recvfrom(sockfd, buffer, MAXLINE, 
                MSG_WAITALL, ( struct sockaddr *) &cliaddr,
                &len);


    // Get a pipe where the output from the scripts comes in
    pipe = popen("date", "r");
    if (pipe == NULL) {  // check for errors 
        perror(argv[0]); // report error message 
        return 1;        // return with exit code indicating error
    }
    fgets(line, LINE_BUFSIZE, pipe);
    
    sendto(sockfd, (const char *)line, strlen(line), 
        MSG_CONFIRM, (const struct sockaddr *) &cliaddr,
            len);

    printf("Server date : %s", line);
    printf("\nClient : %s\n", buffer);
    
    
    

    

    
    

       
    return 0;
}

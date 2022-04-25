#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#define SERVER_ADDRESS "192.168.10.10"
#define PORT 4000

char buf_rx[100]; // Recibe la respuesta del servidor

int main(int argc, char **argv) {

    if (argc < 2) {
        printf("Archivo es requerido\n");
        return -1;
    }

    char* filename = argv[1]; // El argumento 1 es el nombre del archivo.
    char buf_tx[100] = ""; // Se almacena la información del archivo.

    int sock_fd;
    struct sockaddr_in serv_address;
    int largo = sizeof serv_address;
    
    // Creación del socket
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        printf("[CLIENTE]: Error al crear socket\n");
        return -1;
    } else {
        printf("[CLIENTE]: Socket creado satisfactoriamente\n");
    }

    memset(&serv_address, 0, sizeof(serv_address));

    serv_address.sin_family = AF_INET;
    serv_address.sin_addr.s_addr = inet_addr(SERVER_ADDRESS);
    serv_address.sin_port = htons(PORT);

    if ( (connect(sock_fd, (struct sockaddr*)&serv_address, sizeof(serv_address))) !=0 ) {
        printf("[CLIENTE]: Error al realizar la conexión con el servidor \n");
        return -1;
    } else {
        printf("[CLIENTE]: Conexión realizada satisfactoriamente \n");

        send(sock_fd,filename,strlen(filename),0);

        FILE*fp;
        fp = fopen(filename,"rb");

        if (!fp) {
            return -1;
        }
        largo;
        memset(buf_tx,0,sizeof buf_tx);

        while ((largo = fread(buf_tx,1,10,fp))!=0) {
            send(sock_fd,buf_tx,largo,0);
        }

        // Recibir respuesta del servidor
        read(sock_fd, buf_rx, sizeof(buf_rx)); // Mensaje que transmite el servidor
        printf("[CLIENTE]: Recibido => %s \n", buf_rx);

        fclose(fp);
        // Cerrar el socket
        close(sock_fd);
    }

}

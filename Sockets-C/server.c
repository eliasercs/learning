#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
/* Sockets */
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

/* Parámetros del servidor */
#define SERV_PORT 4000
#define SERV_HOST_ADDRESS "192.168.10.10"
#define BACKLOG 5

int main() {
    
    int socket_fd, conn_fd;
    unsigned int largo;
    struct sockaddr_in servidor, cliente;

    int largo_rx, largo_tx = 0;

    char buff_tx[100] = "[SERVIDOR]: El archivo ha sido transferido con éxito\n";
    char buff_rx[100];
    char filename[100];

    // Creación del socket
    socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_fd == -1) {
        printf("[SERVIDOR]: Falló la creación del socket.\n");
        return -1;
    } else {
        printf("[SERVIDOR]: Socket creado satisfactoriamente.\n");
    }

    // Inicializar con 0 cada uno de los bytes de la estructura de formato de dirección para el servidor
    memset(&servidor, 0, sizeof(servidor));

    // Asignación de campos
    servidor.sin_family = AF_INET;
    servidor.sin_addr.s_addr = inet_addr(SERV_HOST_ADDRESS);
    servidor.sin_port = htons(SERV_PORT);

    // Asignar una dirección IP y puerto al socket
    if( (bind(socket_fd, (struct sockaddr*)&servidor, sizeof(servidor))) != 0 ){
        printf("[SERVIDOR]: Asignación del socket ha fallado.\n");
        return -1;
    } else {
        printf("[SERVIDOR]: Socket asignado satisfactoriamente.\n");
    }

    // Escuchar peticiones entrantes
    if ( (listen(socket_fd, BACKLOG)) != 0 ) {
        printf("[SERVIDOR]: Falló al escuchar cliente\n");
        return -1;
    } else {
        printf("[SERVIDOR]: Escuchando en el puerto %d \n", ntohs(servidor.sin_port));
    }

    largo = sizeof(cliente);

    while(1){
        conn_fd = accept(socket_fd, (struct sockaddr *)&cliente, &largo);
        if (conn_fd < 0) {
            printf("[SERVIDOR]: Conexión rechazada \n");
            return -1;
        } else {
            while (1) {
                //Leer datos del cliente
                read(conn_fd, filename, sizeof(filename));
                largo_rx = read(conn_fd, buff_rx, sizeof(buff_rx));

                if (largo_rx == -1) {
                    printf("[SERVIDOR]: Error de lectura \n");
                } else if (largo_rx == 0) {
                    printf("[SERVIDOR]: Conexión con el cliente cerrada \n");
                    close(conn_fd);
                    break;
                } else {
                    write(conn_fd, buff_tx, strlen(buff_tx));
                    printf("%s",buff_tx);
                    FILE*fp = fopen(filename,"wb");
                    if (!fp) {
                        return -1;
                    }
                    // Escribir información en el archivo
                    if (largo_rx>0) {
                        fwrite(buff_rx,1,largo_rx,fp);
                    }
                    fclose(fp);
                }
            }
            
        }
    }
    
}
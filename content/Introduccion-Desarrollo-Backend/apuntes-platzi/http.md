# El lenguaje que habla Internet: HTTP

Hypertext Transfer Protocol o protocolo de transferencia de hipertexto. Es un conjunto de reglas para comunicar dos partes:

- Cliente: Dispositivos al alcance de nuestra mano.
- Servidor: Computadora encendida las 24 horas del día que contiene la aplicación que se va a visualizar en nuestro cliente.

Las transferencias se realizan a través de peticiones por parte del cliente (request) y respuestas por parte del servidor (response).

Cabeceras (headers): pequeñas piezas de información útiles entre el cliente y el servidor.

Método: es la forma en que se realiza la petición.

Códigos de estado: 

- 1xx: Mensaje informativo
- 2xx: Éxito
- 3xx: Redirección
- 4xx: Error del cliente
- 5xx: Error del servidor
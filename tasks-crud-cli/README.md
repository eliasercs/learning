
### Sobre este proyecto

> Este proyecto simula un CRUD de tareas mediante una aplicación a través de la interfaz de línea de comandos.

### Instalación de dependencias

```js
> npm install
```

### Dependencias utilizadas

* [Colors](https://www.npmjs.com/package/colors)
Permite cambiar los colores de los mensajes por consola.

```js
> npm install colors
```

* [Inquirer](https://www.npmjs.com/package/inquirer)
Módulo para elaborar aplicaciones CLI basadas en opciones.

```js
> npm install inquirer
```

* [uuid](https://www.npmjs.com/package/uuid)
Módulo para generar identificadores únicos y aleatorios.

```js
> npm install uuid
```

### Resultado

* Menú inicial de la aplicación

```js
===================================
            CLI of tasks
===================================

? Select a option (Use arrow keys)
> 1. Create a task
  2. Read assignments
  3. Read completed tasks
  4. Read pending tasks
  5. Complete tasks
  6. Delete a task
  7. Exit
```

* Create a task: Solicita ingresar la descripción de una tarea

```js
===================================
            CLI of tasks
===================================

? Select a option 1. Create a task
? Description:  
```

* Read asignaments: Muestra una lista con todas las tareas pendientes y completadas

```js
===================================
            CLI of tasks
===================================

? Select a option 2. Read assignments
1. Programar una aplicación en Node JS :: Completed
2. Hola Mundo en Java :: Completed
3. Hola :: Pending


? PRESS THE ENTER KEY TO CONTINUE () 
```

* Read completed tasks: Muestra una lista con las tareas completadas

```js
===================================
            CLI of tasks
===================================

? Select a option 3. Read completed tasks
1. Programar una aplicación en Node JS :: completed in: 2021-12-04T20:45:11.250Z
2. Hola Mundo en Java :: completed in: 2021-12-04T20:45:11.250Z


? PRESS THE ENTER KEY TO CONTINUE ()  
```

* Read pending tasks: Muestra una lista con las tareas pendientes

```js
===================================
            CLI of tasks
===================================

? Select a option 4. Read pending tasks
3. Hola


? PRESS THE ENTER KEY TO CONTINUE ()   
```

* Complete tasks: Permite marcar como completada una o varias tareas. Las que están completadas aparecen por defecto como marcadas. Se navega con las teclas de flecha arriba y abajo. Con espacio se selecciona/deselecciona una tarea en específico. Con la tecla "a" se seleccionan todas. Con la tecla "i" se invierte la selección. Con la tecla enter se procesa la información.

```js
===================================
            CLI of tasks
===================================

? Select a option 5. Complete tasks
? Select (Press <space> to select, <a> to toggle all, <i> to invert selection, and <enter> to proceed)
>(*) 1. Programar una aplicación en Node JS
 (*) 2. Hola Mundo en Java
 ( ) 3. Hola
```

* Delete a task: Permite eliminar una tarea en específico. Si se selecciona la opción 0, regresa al menú inicial.

```js
===================================
            CLI of tasks
===================================

? Select a option 6. Delete a task       
? Delete a task (Use arrow keys)
> 0. Back
  1. Programar una aplicación en Node JS 
  2. Hola Mundo en Java
  3. Hola
```
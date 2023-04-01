# Home Bakery (Panadería) en Django
Proyecto Final desarrollado en Django para la entrega final del Curso de Python
## Descripción
Este proyecto consiste en una aplicación web para administrar una panadería. Permite que **registremos perfiles de usuarios** (incluyendo el Login y Logout) ,**productos** y  **realizar pedidos con productos**. Además, cuenta con una **función de búsqueda** para **encontrar productos** específicos.
## Uso
Para iniciar el servidor web, debes iniciar el servidor local provisto en Django:
```
python manage.py runserver
```
Esto creara un servidor en la dirección `http://localhost:8000/`, que sirve para ingresar a la aplicación web.
En nuestro caso debemos ingresar ademas a la ruta `http://localhost:8000/HomeBakery` para posicionarnos en el inicio o Home de nuestra página.

### Aplicación web
En la página de inicio tenemos una barra de navegación en la que podemos ir a los diferentes sitios dentro de la aplicación web.
A fin de probar la aplicación, recomendamos que primero nos registremos como usuarios haciendo click en el boton "Registrarse" para luego crear diferentes productos y pedidos:

 1. **Registrar un Usuario o Perfil:** Nos dirigimos a la barra de navegación, en el botón de "Registrarse",alli podremos registrarnos en el sistema para luego hacer el inicio de sesión.
 2. **Iniciar sesión:** Nos dirigimos a la barra de navegación, en el botón de "Iniciar Sesión" para poder hacer nuestro inicio con el usuario creado anteriormente.
 3. **Registrar un Producto:** En la barra de navegación, nos dirigimos hacia "Productos", alli podemos añadir un producto nuevo haciendo click en el botón "Crear nuevo producto" para luego rellenanar un formulario con los datos y al hacer click en el botón "Añadir Producto" podremos guardar nuestro producto. Para acceder a la lista de los productos ya guardados debemos hacer click en el botón "Accede a la lista". También podemos acceder a la lista de los productos creados por nuestro perfil, haciendo click en el avatar de nuestro perfil, lo que despliega un menú con diferentes opciones, y luego haciendo click en el botón "Mis Productos"
 4. **Registrar un Pedido:** En la barra de navegación, nos dirigimos hacia "Hacer un Pedido" o desde el incio tenemos un botón "Pedir Ahora" para añadir un pedido nuevo rellenando el formulario y haciendo click en el botón "Añadir Pedido". Podemos acceder a la lista de los pedidos realizados, haciendo click en el avatar de nuestro perfil, lo que despliega un menú con diferentes opciones, y luego haciendo click en el botón "Mis Pedidos"

Se ha integrado tambien una **función de búsqueda de productos** en la **barra de navegación** en donde escribimos el producto que queremos buscar y luego se hace click en el botón. Esto nos **arroja una lista de resultados** o **nos indica si no se encontró coincidencias** en los productos.
 
### Uso de las herramientas de Administrador de Django
Para hacer uso del panel de administracion provisto por Django, lo hacemos accediendo a la ruta `http://127.0.0.1:8000/admin/`. Para ingresar al admin debemos crear un usuario con los permisos para acceder a todas las funcionalidades de la siguiente manera:
Abrimos una terminal y escribimos el siguiente comando:
```
python manage.py createsuperuser
```
Se nos pedirá un `Username` (usuario), `Email address` (correo electrónico) y un `Password` (contraseña). Si el usuario se crea con éxito, la terminal nos arroja el mensaje `Superuser created successfully.`
En nuesto caso, utilizamos los siguientes datos:
* `Username`: admin
* `Email address`: admin@gmail.com
* `Password`: 1324

## Autor
[César Luciano Angeleri](https://www.linkedin.com/in/cesar-luciano-angeleri/)
## Tecnologías utilizadas
* Django
* Python
* HTML
* CSS
* Bootstrap

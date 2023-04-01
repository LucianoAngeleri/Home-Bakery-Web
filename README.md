# Home Bakery (Panadería) en Django
Proyecto Final desarrollado en Django para la entrega final del Curso de Python
## Descripción
Este proyecto consiste en una aplicación web para administrar una panadería. Permite que **registremos perfiles de usuarios** (pudiendo hacer el Login y Logout del usuario) , **productos** y  **realizar pedidos con  productos**. Además, cuenta con una **función de búsqueda** para **encontrar productos** específicos y tambien contiene un **formulario de contacto o mensajes** que **se envían al administrador**.
## Uso de la aplicación
------------
### Inicio del servidor y acceso al Inicio
Para iniciar el servidor web, debes iniciar el servidor local provisto en Django:
```
python manage.py runserver
```
Esto correrá un servidor en la dirección `http://localhost:8000/`, que sirve para ingresar a la aplicación web.
En nuestro caso debemos ingresar ademas a la ruta `http://localhost:8000/HomeBakery` para posicionarnos en el inicio o Home de nuestra página.

### Funcionalidades de la aplicación web y secciones
En la página de inicio tenemos una **barra de navegación** en la que podemos navegar por los **diferentes sitios dentro de la aplicación web**. En la **parte inferior** de la página se encuentra el **footer** con algunos iconos, botones y links interactivos que nos **redirigen a otras secciones de la web** y a webs externas como **redes sociales**.
A fin de probar la aplicación con los **permisos** correspondientes en todas las secciones, recomendamos que nos registremos como **usuarios**, haciendo click en el boton "Registrarse", y tambien es importante crear un `superusuario(admin)`. Algunas de las **funcionalidades** que se pueden probar son:

 1. **Registrar un Usuario:** Nos dirigimos a la barra de navegación, en el botón de "Registrarse",alli podremos **registrarnos en el sistema** para luego hacer el inicio de sesión.
 2. **Iniciar sesión:** Nos dirigimos a la barra de navegación, en el botón de "Iniciar Sesión" para poder **hacer nuestro inicio con el usuario creado anteriormente**(tambien se puede ingresar como administrador o `admin` si se creo desde la terminal).
 3. **Creación y Actualizacion de Perfiles:** Cada **usuario** creado puede **crearse un perfil de "Cliente"**, mediante el **menú desplegable** que disponemos en el **avatar** que se encuentra en la **esquina superior derecha** de la **barra de navegación**, en la opcion de "Crear Perfil". En la creación puede añadir información como `nombre`, `apellido`, `foto de perfil o avatar`, entre otros. Una vez creado un perfil, se pueden **modificar** los datos del perfil en cuestión de la misma manera, en "Actualizar Perfil".
 4. **Registrar un Producto:** En la barra de navegación, nos dirigimos hacia "Productos", alli podemos **añadir un producto nuevo** haciendo click en el botón "Crear nuevo producto" para luego rellenanar un formulario con los datos y al hacer click en el botón "Añadir Producto" podremos guardar nuestro producto. Para acceder a la lista de los productos ya guardados debemos hacer click en el botón "Accede a la lista". **Al crear un producto se asocia nuestro perfil**, por lo que podemos **obtener una lista de nuestros productos creados**, haciendo click en el **avatar de nuestro perfil**, lo que **despliega un menú con diferentes opciones**, y luego haciendo click en el botón "Mis Productos"
 5. **Registrar un Pedido:** En la barra de navegación, nos dirigimos hacia "Hacer un Pedido" o desde el incio tenemos un botón "Pedir Ahora" para **añadir un pedido nuevo** rellenando el formulario y haciendo click en el botón "Añadir Pedido". Al igual que la seccion de productos, **cada perfil tiene asociado un pedido**. Podemos** acceder a la lista de los pedidos** realizados, haciendo click en el **avatar de nuestro perfil**, lo que **despliega un menú con diferentes opciones**, y luego haciendo click en el botón "Mis Pedidos"
 6. **Detalle, modificación y eliminación:** Tanto los **Pedidos** como los **Productos** creados, **sólo pueden ser modificados y eliminados por el usuario que los creó** con los botones ("Actualizar", "Eliminar") que se muestran en la tarjeta de **Pedido** y **Producto**. **Para ver mas detalles** de los **Pedidos** y **Productos**, tenemos un boton de "Detalles" que **muestra toda la información disponible de ese producto** en particular.
 7. **Mensaje de contacto:** En el **footer o pie de página**, nos dirigimos al link de "Contacto" que **nos lleva a un formulario de contacto para enviar un mensaje al administrador**. Sólo el administrador o `superusers` **serán capaz de ver los mensajes enviados** a traves del **menú disponible al clickear el avatar**, en la opcion de "Mis Mensajes". Tambien dispone de un botón para "Eliminar" los mensajes recibidos.
 8. **Búsqueda:** Se ha integrado tambien una **función de búsqueda de productos** en la **barra de navegación** en donde escribimos el producto que queremos buscar y luego se hace click en el botón. Esto nos **arroja una lista de resultados** o **nos indica si no se encontraron coincidencias** en los productos.
 
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

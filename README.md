# Home Bakery (Panadería) en Django
Proyecto inicial desarrollado en Django para la tercera Pre-Entrega del Curso de Python
## Descripción
Este proyecto consiste en una aplicación web para administrar una panadería. Permite **registrar clientes** ,**productos** y  **realizar pedidos**. Además, cuenta con una **función de búsqueda** para **encontrar productos** específicos.
## Uso
Para iniciar el servidor web, debes iniciar el servidor local provisto en Django:
```
python manage.py runserver
```
Esto creara un servidor en la dirección `http://localhost:8000/`, que sirve para ingresar a la aplicación web.
En nuestro caso debemos ingresar ademas a la ruta `http://localhost:8000/HomeBakery` para posicionarnos en el inicio de nuestra página.

### Aplicación web
En la página de inicio tenemos una barra de navegación en la que podemos ir a los diferentes sitios dentro de la aplicación web.
A fin de probar la aplicación, recomendamos registrar en la base de datos clientes, productos y pedidos en el siguiente orden:

 1. **Registrar un Cliente:** Nos dirigimos a la barra de navegación, en el link de "Clientes", alli podemos acceder a la lista de los clientes registrados (haciendo click en el botón "Accede a la lista") o podemos añadir un cliente nuevo rellenando el formulario y haciendo click en el botón "Añadir Cliente"
 2. **Registrar un Producto:** En la barra de navegación, nos dirigimos hacia "Productos", alli podemos acceder a la lista de los productos ya guardados (haciendo click en el botón "Accede a la lista") o podemos añadir un producto nuevo rellenando el formulario y haciendo click en el botón "Añadir Producto"
 3. **Registrar un Pedido:** En la barra de navegación, nos dirigimos hacia "Pedidos" o desde el incio tenemos un botón "Pedir Ahora", alli podemos acceder a la lista de los pedidos realizados (haciendo click en el botón "Accede a la lista") o podemos añadir un pedido nuevo rellenando el formulario y haciendo click en el botón "Añadir Pedido".
 **Nota: actualmente el registro de Pedidos contiene un error debido a que el modelo creado contiene una relación Muchos a Muchos (Un pedido puede tener varios productos y un producto puede estar en varios pedidos).A futuro se corregirá este error y se implementara el uso de Foreign Keys respecto a los modelos de Pedido y Produtos. De todas maneras, el registro se realiza y queda guardado.* 

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
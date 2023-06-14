# PromptsMenu

un programa que guarda los prompts utilizados en StableDiffusion

Aquí tienes una documentación básica para tu programa:

# Documentación: Prompt Manager
El Prompt Manager es una aplicación de gestión de promts que te permite ver, editar, agregar y eliminar promts de manera fácil y conveniente. 

## Descripción del programa
El programa está desarrollado en Python y utiliza la biblioteca PyQt5 para la interfaz gráfica de usuario. Proporciona una interfaz intuitiva que muestra una lista de promts disponibles y permite al usuario seleccionar, editar, agregar o eliminar promts según sea necesario.

## Funcionalidades principales

### 1. Visualización de promts disponibles
- Al iniciar el programa, se muestra una lista de promts disponibles en la parte izquierda de la interfaz.
- El usuario puede hacer clic en un prompt de la lista para ver su contenido en los campos "Prompt" y "Negative Prompt" en la parte derecha de la interfaz.

### 2. Edición de promts
- El usuario puede seleccionar un prompt de la lista y hacer clic en el botón "Editar" para abrir un cuadro de diálogo de edición.
- El cuadro de diálogo de edición muestra el nombre, el prompt y el negative prompt del prompt seleccionado.
- El usuario puede modificar el contenido del prompt y del negative prompt en el cuadro de diálogo y guardar los cambios haciendo clic en el botón "Guardar".
- Después de guardar los cambios, el prompt modificado se actualizará en la lista y en los campos correspondientes de la interfaz principal.

### 3. Agregar nuevos promts
- El usuario puede hacer clic en el botón "Agregar" para abrir un cuadro de diálogo de agregar.
- El cuadro de diálogo de agregar permite al usuario ingresar un nombre, un prompt y un negative prompt para el nuevo prompt.
- El usuario puede guardar el nuevo prompt haciendo clic en el botón "Guardar".
- Después de guardar el nuevo prompt, se agregará a la lista de promts y estará disponible para su visualización y edición.

### 4. Eliminación de promts
- El usuario puede seleccionar un prompt de la lista y hacer clic en el botón "Eliminar" para eliminarlo.
- Se mostrará una ventana de confirmación para asegurarse de que el usuario realmente desea eliminar el prompt seleccionado.
- Si el usuario confirma la eliminación, el prompt se eliminará de la lista y ya no estará disponible.

### 5. Copiar promts al portapapeles
- El programa proporciona botones "Copiar Prompt" y "Copiar Negative Prompt" que permiten al usuario copiar el contenido del prompt y del negative prompt al portapapeles, respectivamente.
- Esto facilita la copia del contenido y su uso en otras aplicaciones.

## Cómo funciona el programa
1. Al ejecutar el programa, se carga una lista de promts desde un archivo CSV. El archivo CSV contiene los nombres, los promts y los negative promts de los promts disponibles.
2. La lista de promts se muestra en la parte izquierda de la interfaz.
3. Cuando el usuario selecciona un prompt de la lista, su contenido se muestra en los campos "Prompt" y "Negative Prompt" en la parte derecha de la interfaz.
4. El usuario puede realizar diversas acciones como editar, agregar y eliminar promts utilizando los botones correspondientes.
5. Al editar un prompt, se abre un cuadro de diálogo de edición que permite al usuario modificar el contenido del prompt y del negative prompt. Los cambios se guardan y se

 reflejan en la lista y en los campos correspondientes.
6. Al agregar un nuevo prompt, se abre un cuadro de diálogo de agregar donde el usuario puede ingresar un nombre, un prompt y un negative prompt para el nuevo prompt. El nuevo prompt se guarda y se agrega a la lista.
7. Al eliminar un prompt, se muestra una ventana de confirmación para asegurarse de que el usuario desea eliminar el prompt seleccionado. Si se confirma la eliminación, el prompt se elimina de la lista.
8. El programa también proporciona botones para copiar el contenido del prompt y del negative prompt al portapapeles, lo que facilita su uso en otras aplicaciones.

Espero que esta documentación te ayude a entender cómo funciona el programa Prompt Manager y cómo utilizar sus diferentes funcionalidades.

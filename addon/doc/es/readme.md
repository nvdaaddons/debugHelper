# Ayudante de depuración #

* Autor: Luke Davis
* Descargar [versión estable][1]

El propósito de este complemento es facilitar las tareas de depuración en
NVDA. Se añadirán nuevas funciones basadas en las sugerencias de los
usuarios. Todos los correos o [incidencias de
GitHub](https://github.com/XLTechie/debugHelper) con comentarios e ideas de
funciones nuevas son bienvenidos.

## Atajos de teclado

* NVDA+shift+f1: inserta una línea de marca en el registro de NVDA.

## Explicación y uso

Cuando pulses el atajo de teclado, el complemento insertará una línea como
la siguiente en el registro de NVDA (en el nivel Info):

```
-- Marca 1 --
```

También anunciará: "¡Marca 1 grabada!"

Si pulsas el atajo de teclado de nuevo, obtendrás:

```
-- Marca 2 --
```

y se verbalizará "¡Marca 2 grabada!".

Digamos por ejemplo que quieres realizar una serie de tareas que generan
errores extensos en el registro de NVDA. Vas a publicar las partes
relevantes de tu registro en una lista de correo o en el [sistema de
incidencias de NVDA en GitHub](https://github.com/nvaccess/nvda/issues). Sin
embargo, no quieres navegar por el registro entero para buscar el contenido
relevante. Por tanto usas este complemento para insertar la marca 1, justo
antes de hacer eso que causa el primer error. Si sabes que algo más generará
más errores o de diferente tipo, insertas otra marca para separar el error
anterior del nuevo, de tal forma que puedas decir "esto es lo que estaba
haciendo en la marca 3, cuando ocurrieron algunos errores". Otro ejemplo:
mientras usas una aplicación, algo ocurre y provoca un error (tal vez oyes
el sonido de error de Windows). Quieres regresar y buscar ese error más
tarde, pero no quieres dejar de trabajar y guardas el registro justo
ahora. Así que usas este complemento otra vez para insertar una marca en tu
registro. En esta ocasión la marca aparecerá después de los errores en tu
registro, en vez de antes. Pero no importa, las marcas te ayudarán a separar
las secciones importantes de tu registro.

Las líneas de marca mostradas más arriba se pueden buscar fácilmente con el
comando Buscar de un editor de texto como el bloc de notas o
Notepad++. Además, por defecto hay una línea en blanco que se inserta antes
de cada marca. Se pueden poner también líneas en blanco después de la
marca. Las líneas en blanco pueden ser útiles si usas el visualizador del
registro de NVDA u otro editor de texto y deseas usar las flechas para subir
y bajar rápidamente por el registro y encontrar una marca concreta. Es fácil
interceptar las palabras "En blanco" cuando se verbaliza un fragmento de
texto según te mueves rápidamente por el registro. Si te mueves muy rápido,
podrías necesitar más de una línea en blanco. Puedes ajustarlas en las
opciones.

Nota: el contador de marcas sobrevivirá a la recarga de plugins
(NVDA+ctrl+f3), pero se restablecerá a 1 si reinicias NVDA.

## Configuración:

En la sección de Opciones de las preferencias de NVDA, encontrarás una
categoría "Ayudante de depuración". En el diálogo de opciones puedes cambiar
el número de líneas en blanco insertadas antes y después de cada línea de
marca. Por defecto hay una línea antes y 0 después, aunque puedes elegir
entre 0 y 10 líneas para ambos. Bajo la categoría Herramientas del panel
Gestos de entrada de NVDA, puedes cambiar NVDA+shift+f1 por la combinación
de teclas que elijas.

## Registro de cambios

* Versión 1.0.2 (28-08-2019)

    - Traducciones y limpieza de código.

* Versión 1.0.1 (26-08-2019)

    - Versión con correcciones menores para corregir un probable problema de
      instalación en ciertas versiones de Windows.

* Versión 1.0 (22-08-2019)

    - Versión inicial. Incluye las siguientes características:

        + Capacidad de generar líneas de marca numeradas en el registro (a
          nivel Info).
        + Capacidad de agregar de 0 a 10 líneas en blanco antes y después de
          cada línea de marca.
        + Configuración mediante el sistema del diálogo de opciones de NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

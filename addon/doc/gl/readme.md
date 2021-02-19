# Debug Helper #

* Autor: Luke Davis
* Descargar [versión estable][1]

O propósito deste complemento é facer máis fácil depurar cousas en NVDA.
Engadiranse novas características con base nas suxestións dos
usuarios. Todos os emails e [incidencias en
GitHub](https://github.com/XLTechie/debugHelper) con comentarios ou ideas de
características son moi benvidas.

## Orde de Teclas

* NVDA+Shift+F1: Inserta unha liña de marca no rexistro do NVDA.

## Explicación e Uso

Cando premes a orde de teclas, o complemento inserta unha liña como a
seguinte no rexistro do NVDA (no nivel Info):

```
-- Mark 1 --
```

Tamén anunciará: "Logged Mark 1!" (¡Rexistrada Marca 1!)

Se premes a orde de novo, obterás:

```
-- Mark 2 --
```

e falarase "Logged Mark 2!"

Poñamos por caso que estabas a punto de realizar unha serie de tarefas, que
sabes que xeran extenso contido de erro no rexistro de NVDA. Vas a publicar
as porcións relevantes do teu rexistro nunha lista de correo ou [sistema de
incidencias de NVDA en
GitHub](https://github.com/nvaccess/nvda/issues). Porén, non queres explorar
todo o rexistro para buscar o contido relevante. Así que utilizas este
complemento para insertar a marca 1, xusto antes de facer o que causa o
primeiro erro. Se coñeces que algo máis vai xerar máis erros, ou outra
clase, insertas outra marca para separar ése error do anterior, de maneira
que poidas dicir "isto é o que estaba facendo na marca 3, onde ocorreron
algúns erros." Outro exemplo: ao utilizar algunha aplicación,ocorre algo que
causa un erro (quizais oias o son de erro de Windows). Queres volver atrás e
buscar ese erro máis adiante, pero non queres deixar de traballar para
gardar o rexistro no momento. Así que utilizas este complemento de novo,
para insertar unha marca no teu rexistro. Desta volta a marca aparecerá
despois dos erros no teu rexistro, no canto de antes. Mais en calquera caso,
as marcas axudaranche a acotar as seccións importantes do teu rexistro.

As liñas de marca amosadas enriba pódense procurar facilmente co comando
find/procurar nun editor de texto como o bloc de Notas ou Notepad++.
Adicionalmente, por defecto, hai unha liña en branco insertada enriba de
cada marca.  Tamén é posible insertar liñas en branco baixo a marca. As
liñas en branco poden ser útiles se estás a utilizar o visualizador do
rexistro, ou outro editor de texto, e queres utilizar as teclas de frechas
para ler car arriba/abaixo polo rexistro, para procurar unha marca en
particular. É fácil detectar a frase "en branco" de entre a variedade de
texto que se está a falar conforme te moves rapidamente polo rexistro. Se
premes as frechas realmente rápido, poderías precisar máis ca unha liña en
branco, que podes axustar nas opcións.

Nota: O contador de marca sobrevivirá á recarga de complementos
(NVDA+Control+F3), pero comezará de novo en un se reinicias NVDA.

## Configuración:

Na sección Opcións das Preferencias do NVDA; atoparás unha categoría "Debug
Helper". No diálogo de opcións podes cambiar o número de liñas en branco
insertadas antes e despois de cada marca de liña. O predeterminado é unha
liña antes, e cero despois, malia que podes utilizar entre 0 e 10 liñas para
calquera dos dous.  Baixo a categoría Ferramentas do panel Xestos de Entrada
do NVDA, podes trocar NVDA+Shift+F1 por unha secuencia de teclas da túa
escolla.

## Rexistro de trocos

* Versión 1.0.2 (2019-08-28)

    - Tradución e limpeza de código.

* Versión 1.0.1 (2019-08-26)

    - Versión de solución de erros menores para arranxar probablemente un
      problema de instalación en certas versións de Windows.

* Versión 1.0 (2019-08-22)

    - Liberación inicial. Incluíndo as seguintes características:

        + Posibilidade de xerar liñas de marca numeradas no rexistro (no
          nivel info).
        + Posibilidade de engadir 0-10 liñas en branco antes e despois de
          cada liña de marca.
        + Configuración mediante o sistema do diálogo opcións do NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

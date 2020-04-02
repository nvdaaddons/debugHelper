# Auxiliar de Depuração (Debug Helper) #

* Autor: Luke Davis
* Baixar [versão estável][1]

O propósito deste extra é facilitar a depuração do NVDA. Novos recursos
serão adicionados com base nas sugestões do utilizador. Todos os e-mails ou
[problemas/questões devem ser colocados no
GitHub](https://github.com/XLTechie/debugHelper) feedback ou idéias de
recursos são bem-vindos.

## Comandos

* NVDA+Shift+F1: Insere uma linha de marcação no log do NVDA.

## Explicação e uso

Quando pressiona a tecla de comando, o extra insere uma linha como a
seguinte, no log do NVDA (no nível Informações):

``` -- Marcador 1 -- ```

Também falará: "guardado no log Marcador 1!"

Se pressionar a tecla novamente, obterá:

``` -- Marcador 2 -- ```

e "Guardado no log Marcador 2!" será falado.

Digamos, por exemplo, que estava prestes a executar uma série de tarefas que
sabe que vão gerar uma grande quantidade de erros, no log do NVDA. Quer
publicar as partes relevantes do seu log numa lista de discussão ou no
[rastreador de problemas do NVDA no
GitHub](https://github.com/nvaccess/nvda/issues). Mas não deseja percorrer
todo o seu log para encontrar o conteúdo de que precisa. Assim sendo, usa
este extra para inserir o marcador 1, logo antes de executar o que causa o
primeiro erro. Se souber que algo mais irá originar erros adicionais ou um
tipo diferente de falhas, insira outro marcador, para separar esse erro do
anterior, ou então poderá dizer "era isto que eu estava a fazer, inserindo o
marcador 3, onde ocorreram alguns erros." Outro exemplo: ao usar algum
aplicativo, acontece algo que causa um erro (talvez ouça o som do erro do
Windows). necessita encontrar esse erro mais tarde, mas não quer parar de
trabalhar e guardar o log agora. Então usa este extra novamente, para
inserir um marcador no seu log. Desta vez, o marcador aparecerá após os
erros no seu log, e não antes. em conclusão:os marcadores irão ajudá-lo a
dividir as secções importantes do seu registo do NVDA.

As linhas de marcador podem ser facilmente procuradas com o comando
"localizar" num editor de texto como o Bloco de Notas (Notepad) ou o
Notepad++. Além disso, por padrão, será inserida uma linha em branco acima
de cada marcador. Também é possível inserir Linhas em branco após o
marcador. As linhas em branco podem ser úteis se estiver a usar o
visualizador de logs do NVDA ou outro editor de texto e quiser usar as
teclas de seta para ler rapidamente para cima/baixo no log, para encontrar
um marcador específico. É fácil detectar a expressão "em branco"  no meio de
um texto que esteja a ser falado, à medida que se move rapidamente pelo
log. Se a sua leitura for muito rápida, poderá precisar de mais de uma linha
em branco, o que pode ser ajustado nas configurações.

Nota: A contagem de marcadores persistirá depois do  recarregamento de
plug-ins (NVDA+Control+F3), mas será reiniciada se reiniciar o NVDA.

## Configuração:

Na secção "Configurações", nas Preferências do NVDA, encontrará uma
categoria chamada "Auxiliar de Depuração". No diálogo de configurações, pode
alterar o número de linhas em branco inseridas antes e depois de cada linha
de marcador. O padrão é uma linha antes e zero depois, embora possa usar de
0 a 10 linhas para ambos os parâmetros. Na categoria "Definir comandos" pode
alterar o NVDA+Shift+F1 para uma sequência de teclas à sua escolha.

## Alterações

* Versão 1.0.2 (2019-08-28)

    - Tradução e limpeza de código.

* Versão 1.0.1 (2019-08-26)

    - Versão de correção de falha menor para provavelmente corrigir um
      problema de instalação em determinadas versões do Windows.

* Versão 1.0 (2019-08-22)

    - Versão inicial. Incluindo os seguintes recursos:

        + Capacidade de criar linhas de marcadores numeradas no log (no
          nível de informações).
        + Capacidade de adicionar de 0 a 10 linhas em branco antes e depois
          de cada linha de marcador.
        + Configuração através do sistema de diálogo de configurações do
          NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

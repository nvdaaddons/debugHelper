# Ajudante de Depuração (Debug Helper) #

* Autor: Luke Davis
* Baixe a [versão estável][1]

O propósito desse complemento é facilitar a depuração do NVDA. Novos
recursos serão adicionados com base nas sugestões do usuário. Todos os
e-mails ou [problemas/questões no
GitHub](https://github.com/XLTechie/debugHelper) com retroalimentação
(feedback) ou idéias de recursos são bem-vindos.

## Comando por teclas

* NVDA+Shift+F1: Insere uma linha de marca no log do NVDA.

## Explicação e uso

Quando você pressiona a tecla de comando, o complemento insere uma linha
como a seguinte no log do NVDA (no nível Informações):

```
-- Mark 1 --
```

Ele também anunciará: "Gravado no log Marca 1!"

Se você pressionar a tecla novamente, você obterá:

```
-- Mark 2 --
```

e "Gravado no log Marca 2!" será falado.

Digamos, por exemplo, que você estava prestes a executar uma série de
tarefas, que sabe gerar um longo conteúdo de erro no log do NVDA. Você vai
postar as partes relevantes do seu log em uma lista de discussão ou no
[rastreador de problemas do NVDA no
GitHub](https://github.com/nvaccess/nvda/issues). No entanto, não deseja
percorrer todo o seu log para encontrar o conteúdo relevante. Então você usa
esse complemento para inserir a marca 1, logo antes de executar o que causa
o primeiro erro. Se souber que algo mais irá gerar erros adicionais, ou um
tipo diferente, insira outra marca para separar esse erro do anterior, ou
então você poderá dizer "é isso que eu estava fazendo na marca 3, onde
ocorreram alguns erros." Outro exemplo: ao usar algum aplicativo, acontece
algo que causa um erro (talvez você ouça o som do erro do Windows). Você
deseja voltar e encontrar esse erro mais tarde, mas não deseja parar de
trabalhar e salvar o log agora. Então você usa esse complemento novamente
para inserir uma marca no seu log. Desta vez, a marca aparecerá após os
erros no seu log, e não antes. De qualquer forma, as marcas o ajudarão a
restringir as seções importantes do seu log.

As linhas de marca mostradas acima podem ser facilmente pesquisadas com o
comando localizar em um editor de texto como o Bloco de Notas (Notepad) ou o
Notepad++. Além disso, por padrão, há uma linha em branco inserida acima de
cada marca. Linhas em branco também são possíveis após a marca. Linhas em
branco podem ser úteis se você estiver usando o visualizador de logs do NVDA
ou outro editor de texto e quiser usar as teclas de seta para ler
rapidamente para cima/baixo no log, para encontrar uma marca específica. É
fácil escolher a palavra "em branco" de um monte de texto sendo falado à
medida que você se move rapidamente pelo log. Se você for muito rápido,
poderá precisar de mais de uma linha em branco, que pode ser ajustada nas
configurações.

Nota: A contagem de marcas sobreviverá ao recarregamento de plug-ins
(NVDA+Control+F3), mas será reiniciada se você reiniciar o NVDA.

## Configuração:

Na seção Configurações das Preferências do NVDA, você encontrará uma
categoria "Ajudante de Depuração". No diálogo de configurações, pode alterar
o número de linhas em branco inseridas antes e depois de cada linha de
marca. O padrão é uma linha antes e zero depois, embora você possa usar de 0
a 10 linhas para ambos. Sob a categoria Ferramentas do painel Definir
comandos do NVDA, pode alterar o NVDA+Shift+F1 para uma sequência de teclas
de sua escolha.

## Registro de alterações (Changelog)

* Versão 1.0.2 (2019-08-28)

    - Tradução e limpeza de código.

* Versão 1.0.1 (2019-08-26)

    - Versão de correção de falha menor para provavelmente corrigir um
      problema de instalação em determinadas versões do Windows.

* Versão 1.0 (2019-08-22)

    - Versão inicial. Incluindo os seguintes recursos:

        + Capacidade de gerar linhas de marcas numeradas no log (no nível de
          informações).
        + Capacidade de adicionar de 0-10 linhas em branco antes e depois de
          cada linha de marca.
        + Configuração através do sistema de diálogo de configurações do
          NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

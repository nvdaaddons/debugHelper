# Debug-Helfer #

* Autor: Luke Davis
* [Stabile Version herunterladen][1]

Der Zweck dieser Erweiterung ist es, das Debugging in NVDA zu erleichtern.
Neue Funktionen werden auf der Grundlage von Benutzervorschlägen
hinzugefügt. Alle E-Mails oder [GitHub
issues](https://github.com/XLTechie/debugHelper) mit Feedback oder
Feature-Ideen sind herzlich willkommen.

## Tastenbefehl

* NVDA+Umschalt+F1: Fügt eine Markierungslinie in das NVDA-Protokoll ein.

## Erläuterung und Verwendung

Wenn Sie die Tastenkombination drücken, fügt die Erweiterung eine Zeile wie
die Folgende in das NVDA-Protokoll (auf der Ebene Info) ein:

```
``` -- Mark 1 --
```

Es meldet dann: "Logged Mark 1!"

Wenn Sie die Tastenkombination erneut drücken, erhalten Sie:

```
``` -- Mark 2 --
```

und "Logged Mark 2!" wird mitgeteilt.

Nehmen wir zum Beispiel an, dass Sie im Begriff waren, eine Reihe von
Aufgaben durchzuführen, von denen Sie wissen, dass sie lange Fehlerinhalte
im NVDA-Protokoll erzeugen. Sie werden die relevanten Teile Ihres Protokolls
an eine Mailingliste oder den [NVDA GitHub Issue Tracker
https://github.com/nvaccess/nvda/issues] senden. Sie möchten jedoch nicht
Ihr gesamtes Protokoll durchsuchen, um den relevanten Inhalt zu finden. Sie
verwenden also diese Erweiterung, um die Markierung 1 einzufügen, kurz bevor
Sie die Sache tun, die den ersten Fehler verursacht. Wenn Sie wissen, dass
etwas anderes weitere Fehler erzeugt oder eine andere Art, fügen Sie eine
andere Markierung ein, um diesen Fehler von dem vorherigen zu trennen, oder
so können Sie sagen: "Das ist es, was ich bei Markierung 3 getan habe, wo
einige Fehler aufgetreten sind". Ein weiteres Beispiel: Bei der Verwendung
einer Anwendung passiert etwas, das einen Fehler verursacht (vielleicht
hören Sie den Windows-Fehlerton). Sie wollen zurückgehen und diesen Fehler
später finden, aber Sie wollen nicht aufhören zu arbeiten und das Protokoll
sofort speichern. Sie verwenden diese Erweiterung also wieder, um eine
Markierung in Ihr Protokoll einzufügen. Diesmal erscheint die Markierung
nach den Fehlern in Ihrem Protokoll, nicht vorher. Aber so oder so, die
Markierungen werden Ihnen helfen, die wichtigen Abschnitte Ihres Protokolls
einzugrenzen.

Die oben gezeigten Markierungslinien können mit dem Befehl Suchen in einem
Text-Editor wie Notepad oder Notepad++ einfach gesucht werden. Zusätzlich
wird standardmäßig über jeder Markierung eine Leerzeile
eingefügt. Leerzeilen sind auch nach der Markierung möglich. Sie können
hilfreich sein, wenn Sie den NVDA-Protokollbetrachter oder einen anderen
Text-Editor verwenden und die Pfeiltasten verwenden möchten, um schnell auf
bzw. ab durch das Protokoll zu lesen und eine bestimmte Markierung zu
finden. Es ist einfach, das Wort "leer" aus einem Haufen gesprochener Texte
auszuwählen, während Sie sich schnell durch das Protokoll bewegen. Wenn Sie
wirklich schnell die Pfeiltasten benutzen, benötigen Sie möglicherweise mehr
als eine Leerzeile, die Sie in den Einstellungen anpassen können.

Hinweis: Die Markierungsanzahl überlebt das Neuladen der Plugins
(NVDA+Strg+F3), beginnt aber wieder bei eins, wenn Sie NVDA neu starten.

## Konfiguration:

Im Abschnitt Einstellungen der NVDA-Einstellungen finden Sie eine Kategorie
"Debug Helper". Im Einstellungsdialog können Sie die Anzahl der vor und nach
jeder Markierungszeile eingefügten Leerzeilen ändern. Der Standard ist eine
Zeile vor und nach der anderen, obwohl Sie für beide Zeilen 0 bis 10 Zeilen
verwenden können. In der Kategorie Extras des NVDA-Menüs "Eingaben..."
können Sie NVDA+Umschalt+F1 in eine Tastenfolge Ihrer Wahl ändern.

## Änderungsprotokoll

* Version 1.0.2 (28.08.2019)

    - Übersetzung und Code-Bereinigung.

* Version 1.0.1 (26.08.2019)

    - Kleine Bugfix-Version, um wahrscheinlich ein Installationsproblem
      unter bestimmten Windows-Versionen zu beheben.

* Version 1.0 (22.08.2019)

    - Erste Veröffentlichung. Inklusive folgender Funktionen:

        + Möglichkeit, nummerierte Markierungslinien im Protokoll zu
          erzeugen (auf Informationsebene).
        + Möglichkeit, 0 bis 10 Leerzeilen vor und nach jeder
          Markierungslinie hinzuzufügen.
        + Konfiguration über das Dialogsystem der NVDA-Einstellungen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

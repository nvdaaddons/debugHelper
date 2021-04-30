# Debug Helper #

* Autore: Luke Davis
* Scarica [la versione stabile][1].

Lo scopo di questo addon è quello di semplificare il processo di debugging
in NVDA. Verranno aggiunte nuove funzionalità in base alle richieste degli
utenti. Qualsiasi problema o idea può essere segnalata tramite posta
elettronica oppure tramite [GitHub
issues](https://github.com/XLTechie/debugHelper).

## Comando principale

* NVDA + Maiusc + F1: inserisce una linea di marcatura nel log NVDA.

## Spiegazioni e utilizzo

Quando si utilizza il comando principale NVDA+Shift+F1, NVDA inserisce una
riga simile alla seguente nel log, al livello Info:

```
``` -- Mark 1 -- 
```

Verrà anche annunciato: "inserito nel log Mark 1!"

Se si preme il tasto nuovamente, si otterrà:

```
``` -- Mark 2 -- 
```

e la sintesi vocale dirà: "inserito nel log Mark 2!".

Diciamo, ad esempio, che stiate eseguendo una serie di operazioni che
producono messaggi di errore lunghi nel log di NVDA. Vorreste postare le
parti più importanti del log in una mailing list o nell'[NVDA GitHub issue
tracker](https://github.com/nvaccess/nvda/issues), ma non vorreste leggervi
tutto il log per individuare le parti suddette. Utilizzate questo add-on per
inserire la prima marcatura, subito prima di compiere la prima operazione
che causa il primo errore. Se sapete che qualche altra operazione genererà
ulteriori errori o comunque messaggi di interesse, inserite questa marcatura
per separare questi errori dai precedenti, o per dire "Ecco cosa stavo
facendo al mark 3, dove si sono verificati alcuni errori". Un altro esempio:
mentre utilizzate un'applicazione, accade qualcosa che causa un errore
(probabilmente sentite il suono di errore di Windows). Vorreste tornare
indietro e trovare quell'errore più tardi, ma non volete interrompere il
lavoro e salvare il log proprio ora. Utilizzate nuovamente questo add-on per
inserire una marcatura nel log. Questa volta la marcatura apparirà dopo gli
errori nel log, anziché prima. In entrambi i casi, comunque, le marcature vi
aiuteranno a delimitare le parti importanti del vostro log.

Le linee di demarcazione sopra mostrate possono essere facilmente cercate
con il comando "trova" in un editor di testi, come Notepad or
Notepad++. Inoltre, per default, viene inserita una linea vuota sopra ogni
marcatura. E' anche possibile inserire linee vuote dopo la marcatura
stessa. Le linee vuote possono essere utili se si sta utilizzando il
visualizzatore di log di NVDA o un altro editor di testi e si vogliono
utilizzare i tasti freccia per scorrere velocemente il log, per trovare una
certa marcatura. E' facile discernere la parola "vuoto" in mezzo a tante
altre parole che la sintesi vocale recita quando ci si muove rapidamente
attraverso il log. Se vi spostate molto velocemente, potreste aver bisogno
di più righe vuote; potete settare questo parametro nelle impostazioni.

Nota: il conteggio delle marcature non viene perso quando i plugins vengono
ricaricati (NVDA+Control+F3), ma riparte da 1 se si riavvia NVDA.

## Configurazione:

Nella sezione Impostazioni delle preferenze di NVDA, troverete la categoria
"Debug Helper". Nella relativa finestra potete modificare il numero di linee
vuote inserite prima e dopo ogni linea di marcatura. Il default è una linea
prima e zero dopo, ma potete inserire valori da 0 a 10. Nella categoria
Strumenti della finestra Gesti e Tasti di Immissione di NVDA, potete
sostituire NVDA+Shift+F1 con un'altra combinazione di tasti a vostra scelta.

## Changelog

* Novità nella versione 1.0.2 (28-08-2019)

    - Pulizia del codice e della traduzione.

* Novità nella versione 1.0.1 (26-08-2019)

    - Correzione di bug minori per (probabilmente) correggere un problema di
      installazione su alcune versioni di Windows.

* Novità nella versione 1.0 (22-08-2019)

    - Versione iniziale, che comprende le seguenti caratteristiche:

        + Capacità di generare linee di marcatura numerate nel log (al
          livello info).
        + Capacità di aggiungere da 0 a 10 linee vuote prima e dopo ogni
          linea di marcatura.
        + Configurazione attraverso le impostazioni di NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

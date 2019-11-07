# Fejlfindingshjælper #

* Forfatter: Luke Davis
* Download [stabil version][1]

Formålet med denne tilføjelse er at gøre fejlfinding i NVDA lettere.  Nye
funktioner vil blive tilføjet baseret på brugerforslag. Alle e-mails eller
[GitHub Issues](https:/github.com/xltechie/debughelper) med feedback eller
ideer er meget velkomne.

## Tastaturkommando

* NVDA+Shift+F1:Indsætter en Mark-linje i NVDA-loggen.

## Forklaring og brug

Når du trykker på Kommandotasten, indsætter tilføjelsesprogrammet en linje
som følgende i NVDA-loggen (på infoniveau):

``` -- Mark 1 -- ```

NVDA vil også annoncere: "Logger Mark 1!"

Hvis du trykker på tasten igen:

``` -- Mark 2 -- ```

og "Logger Mark 2!" vil blive oplyst.

Lad os sige, at du var ved at udføre en række opgaver, som du ved generere
mange fejl i NVDA-loggen. Du skal sende de relevante dele af din log til en
mailingliste eller til [NVDA GitHub Issue
tracker](https:/github.com/nvaccess/NVDA/Issues). Du ønsker ikke at læse
gennem hele din log for at finde det relevante indhold, så du bruger denne
tilføjelse til at indsætte Mark 1, lige før du gør de ting, der forårsager
den første fejl. Hvis du ved noget andet vil generere yderligere fejl,
indsætter du et andet mærke for at adskille denne fejl fra den foregående,
eller så du kan sige "Dette er hvad jeg gjorde ved Mark 3, hvor nogle fejl
opstod." Et andet eksempel: Mens du bruger et program, sker der noget, som
forårsager en fejl (måske hører du lyden der afspilles ved Windows-fejl). Du
ønsker at gå tilbage og finde den fejl senere, men du ønsker ikke at stoppe
med at arbejde og gemme loggen lige nu. Så du bruger denne tilføjelse igen,
så du kan indsætte et mærke i din log. Denne gang vises mærket efter fejlene
i din log, i stedet for før. Men uanset hvad, vil mærkerne hjælpe dig med at
indsnævre de vigtige sektioner i din log.

De afmærkede linjer som vist ovenfor kan nemt søges efter ved at bruge et
tekstredigeringsprogram som eksempelvis notesblokken eller
Notepad++. Derudover er der som standard indsat en tom linje ovenfor hvert
mærke. Blanke linjer kan også fremkomme efter mærket. Blanke linjer kan være
nyttige, hvis du bruger NVDA'S logviser eller et andet
tekstredigeringsværktøj, og ønsker at bruge piletasterne til hurtigt at læse
op/ned gennem loggen for at finde et bestemt mærke. Det er nemt at høre
ordet "blank" under en hurtig gennemgang af en større mængde tekst, der
udtales eftersom du hurtigt bevæger dig gennem loggen. Hvis du bruger
piletasterne ret hurtigt, får du måske brug for flere blanke linjer. Du kan
tilpasse dette i indstillingerne.

Bemærk: Tælleren der anvendes til mærker bevares efter genindlæsning af
plugins (NVDA+Control+F3), men men bevares ikke, hvis du genstarter NVDA.

## Konfiguration:

I afsnittet Indstillinger i NVDA-indstillingerne finder du kategorien
"Fejlfindingshjælper". I indstillingsdialogen kan du ændre antallet af
blanke linjer, som indsættes før og efter hver Mark-linje. Standarden er én
linje før, og nul efter, selvom du kan bruge 0 til 10 linjer for begge
muligheder.  Under menuen "Værktøjer" i NVDA-panelet "Inputbevægelser" kan
du ændre NVDA+Shift+F1 til en tastesekvens efter eget valg.

## Ændringslog

* Version 1.0.2 (2019-08-28)

    - Oversættelse og kodeoprydning.

* Version 1.0.1 (2019-08-26)

    - Mindre fejlrettelser der forhåbentligt løser et installationsproblem i
      visse versioner af Windows.

* Version 1.0 (2019-08-22)

    - Første udgivelse. Herunder følgende funktioner:

        + Mulighed for at generere nummererede Mark-linjer i loggen (på
          infoniveau).
        + Mulighed for at tilføje 0-10 blanke linjer før og efter hver
          Mark-linje.
        + Konfiguration via NVDA-indstillingsdialog.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

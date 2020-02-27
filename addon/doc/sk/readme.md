# Pomocník pre ladenie #

* Autor: Luke Davis
* Stiahnuť [stabilnú verziu][1]

Cieľom doplnku je uľahčiť vývoj NVDA a diagnostiku chýb. Ak máte nápady na
nové funkcie, napíšte mi e-mail, veľmi rád ich zaradím. Akceptujem tiež
[Hlásenia chýb a návrhy na GitHub](https://github.com/XLTechie/debugHelper).

## Klávesové skratky

* NVDA+shift+F1: Vloží do logu NVDA značku.

## Využitie

Po stlačení klávesovej skratky sa do logu NVDA zapíše značka v tomto tvare:

``` -- Značka1 -- ```

NVDA takisto oznámi zapísanie značky 1.

Po opätovnom stlačení skratky sa do logu zapíše:

``` -- Značka 2 -- ```

NVDA oznámi zapísanie značky 2.

Predstavme si nasledujúcu situáciu: Viete, že určité správanie  spôsobuje
chybu v NVDA a táto chyba sa zapíše dlhým záznamom do logu NVDA. Záznam
chcete poslať do mailinglistu, alebo ako report do [NVDA GitHub issue
trackera](https://github.com/nvaccess/nvda/issues). Nechcete ale prehľadávať
celý log, aby ste našli príslušnú časť. Preto najprv pomocou klávesovej
skratky vložíte značku a potom vykonáte činnosti, ktoré spôsobujú zamrznutie
a pád NVDA. Ak viete, že chcete zaznamenať ďalšie chyby, môžete vložiť
ďalšie značky. Takto viete určiť, čo ste robili pri vkladaní napríklad
tretej značky. Iná situácia môže nastať, keď používate nejakú aplikáciu a
znenazdajky dôjde k chybe. Nechcete prerušiť prácu, súčasne si ale chcete
miesto poznačiť. Preto pomocou klávesovej skratky vložíte značku, ktorú
neskôr viete v logu vyhľadať. Chybu budete potom hľadať smerom od značky
nahor.

Značky môžete  rýchlo vyhľadať pomocou poznámkového bloku alebo napríklad
Notepad++. Pred každou značkou doplnok automaticky vloží prázdny
riadok. Toto je užitočné pri rýchlom prezeraní záznamu. Aj pri rýchlom
stláčaní šípky dokážete rozpoznať slovo "prázdny". Môžete tiež nastaviť, aby
sa pred značku vložilo viac prázdnych riadkov.

Upozorňujem, že znovu načítanie doplnkov NVDA nemá vplyv na číslovanie
značiek. Značky sa číslujú od 1 po reštarte NVDA.

## Nastavenie

V nastaveniach NVDA po nainštalovaní doplnku pribudne vetva "Pomoc pri
ladení". Tu môžete nastaviť, koľko prázdnych riadkov chcete vložiť pred a za
značku. Pred značku sa predvolene vkladá jeden prázdny riadok, za značku sa
nevkladajú žiadne prázdne riadky. V oboh prípadoch môžete vložiť maximálne
10 riadkov. Klávesovú skratku na vloženie značky môžete nastaviť v dialógu
klávesové skratky, hľadajte vetvu nástroje.

## Zmeny

* Verzia 1.0.2 (2019-08-28)

    - Pridané preklady a upravený kód.

* Verzia 1.0.1 (2019-08-26)

    - Drobné úpravy a opravené problémy s inštaláciou na niektorých verziách
      Windows.

* Verzia 1.0 (2019-08-22)

    - Prvotné vydanie. Dostupné sú tieto možnosti:

        + Pridávanie značiek do logu NVDA (od úrovne ifo).
        + Možnosť pridať pred a po značke až do desať prázdnych riadkov.
        + Nastavenie cez strom nastavení NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

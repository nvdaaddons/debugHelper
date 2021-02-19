# Pomoćnik za uklanjanje grešaka (Debug Helper) #

* Autor: Luke Davis
* Preuzmi [stabilnu verziju][1]

Svrha ovog dodatka je olakšavanje ispravljanja grešaka u NVDA čitaču. Nove
funkcije će se dodavati ovisno o korisničkim prijedlozima. Sve e-poruke ili
[GitHub problemi] (https://github.com/XLTechie/debugHelper) s povratnim
informacijama ili idejama o funkcijama su dobrodošli.

## Tipkovnički prečac

* NVDA+šift+F1: Umetni redak s oznakom u NVDA log zapisu.

## Objašnjenje i primjena

Kad pritisneš tipkovnički prečac, dodatak ubacuje sljedeći redak u NVDA log
zapis (na razini informacija):

```
-- Mark 1 --
```

Najavit će i: „Oznaka 1 zapisana!”

Ako ponovo pritisneš prečac, dobit ćeš:

```
-- Mark 2 --
```

i izgovorit će se „Oznaka 2 zapisana!”

Recimo na primjer da si želio obaviti niz zadataka, za koje znaš da
generiraju dugački log zapis o grešci. Relevantne dijelove log zapisa ćeš
objaviti na mailing listi ili u [NVDA GitHub sustavu za praćenje grešaka]
(https://github.com/nvaccess/nvda/isissue). Međutim ne želiš tražiti cijeli
log zapis, kako bi se pronašao odgovarajući sadržaj. U tom slučaju koristi
ovaj dodatak za umetanje oznake 1, neposredno prije nego što odradiš radnju
koja uzrokuje prvu grešku. Ako znaš da će nešto drugo stvoriti daljnje
greške ili neku drugu vrstu greške, umetni drugu oznaku za odvajanje te
greške od prethodne ili kako bi mogao reći „to je ono, što sam radio kod
oznake 3, gdje su se dogodile neke pogreške”. Drugi primjer: Tijekom
korištenja neke aplikacije, događa se nešto što uzrokuje grešku (možda čuješ
zvuk greške Windows sustava). Želiš se vratiti i pronaći tu grešku kasnije,
ali ne želiš sada prestati raditi i spremiti zapisnik. Tada ponovo
upotrijebi ovaj dodatak za umetanje oznake u svoj log zapis. Ovaj put će se
oznaka pojaviti nakon grešaka u tvom log zapisu, umjesto prije njih. No kako
god bilo, oznake će ti pomoći zažeti važne dijelove tvog log zapisa.

Gore prikazani označeni redci mogu se lako pretražiti pomoću naredbe za
traženje u uređivaču teksta, kao što su Notepad ili Notepad++. Pored toga,
iznad svake oznake je umetnut prazan redak. Moguće je postaviti prazne retke
i nakon oznake. Prazni redci mogu biti korisni, ako koristiš NVDA preglednik
log zapisa ili neki drugi uređivač teksta i ako želiš koristiti strelice za
brzo čitanje prema gore ili dolje kroz log zapis za pronalaženje određene
oznake. Riječ „prazno” je jednostavno odabrati iz gomile teksta koji se
izgovara dok se brzo krećeš kroz log zapis. Ako koristiš strelicu stvarno
brzo, možda ćeš trebati više od jednog praznog retka, što možeš prilagoditi
u postavkama.

Napomena: Ponovno učitavanje dodataka (NVDA+kontrol+F3) neće utjecati na
brojenje oznaka, ali će započeti s brojem jedan, ako se NVDA ponovo pokrene.

## Konfiguracija:

U odjeljku za postavke u NVDA postavkama pronaći ćeš kategoriju „Pomoćnik za
uklanjanje grešaka”. U dijaloškom okviru postavki možeš promijeniti broj
praznih redaka umetnutih prije i nakon svakog označenog retka. Standardno se
koristi je jedan redak prije, a nijedan redak poslije, iako možeš koristiti
0 do 10 redaka za prije ili za poslije. Pod kategorijom Alati u NVDA ploči
Ulazne geste, možeš promijeniti NVDA+šift+F1 u tipkovnički prečac po
vlastitom izboru.

## Promjene

* Verzija 1.0.2 (2019-08-28)

    - Prijevod i ispravljanje programskog koda.

* Verzija 1.0.1 (2019-08-26)

    - Verzija s manjim ispravcima, koji vjerojatno ispravljaju problem s
      instalacijom na određenim verzijama Windows sustava.

* Verzija 1.0 (2019-08-22)

    - Prvo izdanje. Uključuje sljedeće funkcije:

        + Mogućnost generiranja numerirano označenih redaka u log zapisu (na
          razini informacija).
        + Mogućnost dodavanja 0 do 10 praznih redaka prije i nakon svakog
          retka s oznakom.
        + Konfiguracija putem NVDA dijaloškog sustava za postavke.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper

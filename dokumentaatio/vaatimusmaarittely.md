# Vaatimusmäärittely

## PROJEKTI LYHYESTI:
- Ohjelman tuotos olisi järkevän näköinen linna/tyrmä/luola
- Tyrmän huoneet koostuisivat esimerkkihuoneista, joita käyttäjä voisi muokata halutessaan - tehty
- Tyrmän huoneet asettautuisivat järkevästi ruudukkoon - tehty (huoneet asetetaan satunnaisesti)
- Tyrmän huoneet yhdistyisivät toisiinsa käytävillä (a* algoritmi?) - tehty (polut ovat minimi-toiminnalisia)
- Projekti olisi toteutettu ruudukossa jossa merkit kuvaavat seiniä, laittoita ja ovia - tehty

## Toiminta käytännössä:
- Käyttäjälle ohjelma jakautuu kahteen pää-näkymään; tyrmän määrittelyyn ja tyrmän generoimiseen
- Tyrmän määrittelyssä käyttäjä voi määrittää halutun: koon, huoneiden määrän, huoneiden "tyypit" 
- Tyrmän generoimisen aikana käyttäjä näkisi reaaliajassa tyrmän luomisprosessin ja voisi toistaa prosessin - tehty (tyrmän voi uudelleenluora painamalla r näppäintä, luomisprosessi tapahtuu välittömästi)
- Tyrmien generoimisen aikana käyttäjä voisi tallentaa tyrmän tekstitiedostona - tehty (tiedostoja voi nyt tallentaa halutessaan local/saves folderiin)

## Visuaalinen esimerkki:
- Inspiraationa toimii Rogue-pelin tasosysteemi, kuva alla:

![Rogue manual](https://github.com/GlobalYam/AarninOlioSimulaattori-Python/blob/main/dokumentaatio/Rogue_Instruction_Manual_©_1985_EPYX_Inc.png)


## Näkymä ja käyttöliittymä
- Tekstipohjainen, Ruudukon solujen sisällöt kuvataan ASCII-merkeillä - tehty (väreillä, ei ASCII)
- Esimerkkihuoneet voivat määrittää tekstitiedostossa. - tehty (halutessaan tiedostoja voi muokata ja lisätä)

## Käyttäjät
- EI erityistä tarvetta käyttäjälle

## Jatkokehitys-Ideoita
- Tyrmä-Seikkailu olisi kolmas näkymä jossa käyttäjä voisi päättää tutkia tyrmää ohjaamalla pelaajahahmoa
- Tyrmä-Seikkailussa voisi löytää portaikkoja alemmille tasoille
- Tyrmä-Seikkailussa voisi olla myös vastustajia ja aarteita
- Näkymät ja käyttöliittymät voisivat myös olla graaffisia
- Generaatioprosessit voisivat olla monimutkaisempia

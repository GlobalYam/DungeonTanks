# Tämä on oppaan alku

# Näppäinkomennot:
'R' - luo uusi kerros

'D' - lisää kerroksen huoneisiin polkuja

'F' - siirry kokonäytön tilaan ja takaisin

'S' - Tallentaa tämänhetkisen kerroksen

'L' - lataa tallennettuja kerroksia järjestyksessä

'U' - Manuaalisesti päivittää näytön 

'P' - Tulostaa tämänhetkisen kerroksen terminaaliin 

'Q' - poistu sovelluksesta

## Huone/Kerros tiedostot:

Huoneet ovat tallennettu merkkijonomuodossa, jossa rivien leveyden tulee säilyä samana.
OIKEIN:
```
###D###
#.....#
#.....#
D.....D
#.....#
#.....#
###D###
```

VÄÄRIN:
```
###D###
#.....#
#.....#
D...D
#.....#
#.....#
###D###
```

OIKEIN:
```
###D###
#.....#
#.....#
=D...D=
#.....#
#.....#
###D###
```

Kyseistä ongelmaa ei kohdata ohjelmaa käyttäessä, ellei käyttäjä halua itse määrittää huonepohjia manuaalisesti.


## Merkkien käyttö ja tarkoitus:
'#'  PERSONAL WALL - Oikea fyysinen seinä, aina jonkin huoneen tai kerroksen oma

'='  WALL AURA     - Fyysisen seinän "aura," tämä asetetaan antaakseen huoneille tilaa

'-'  VOID          - Tyhjyys, johon voi asettaa uutta tavaraa

'.'  FLOOR         - Lattia, huoneen sisällä, ei saa koskea VOID palaa!

':'  PATH          - Polku, pala polkua joka johdattaa huoneesta toiseen.

'D'  DOOR          - Ovi, joka johtaa ulos huoneesta, tai korvataan seinällä.

'S'  STAIRS        - Portaikko jonka suunta määritetään generoinnin jälkeen, tai korvataan lattialla.

'^'  STAIRS UP     - Portaikko joka vie korkeammalle kerrokselle, sijoittuu aloitushuoneeseen

'v'  STAIRS DOWN   - Portaikko joka vie alemmalle kerrokselle, sijoittuu lopetushuoneeseen.
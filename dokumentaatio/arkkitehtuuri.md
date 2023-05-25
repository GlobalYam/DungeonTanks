# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

Projektin arkkitehtuuri on varsin yksinkertainen, sillä projekti on vielä alussa.

Ruudukkomanageri on projektin sydän ja hoitaa lähes kaiken relevantin logiikan.

Polkumanageri vastaa huoneita yhdistävien polkujen luomisesta, ja vastaa aina ruudukkomanagerille.

Näyttömanageri hoitaa annetun ruudukon piirtämisen näytölle. Tätä varten sille annetaan Ruudukkomanagerin tiedot luettaviksi.

Näppäimistömanageri pystyy vaikuttamaan ruudukkomanageriin ja näyttömanagerin fullscreen muuttujaan. Pystyy myös sulkemaan sovelluksen.

## Luokkadiagrammi

```mermaid
 classDiagram
      InputManager "1" --> "1" ScreenManager
      InputManager "1" --> "1" GridManager
      ScreenManager "1" --> "1" GridManager
      GridManager "1" --> "1"  PathManager
      class GridManager{
          Grid
      }
      class ScreenManager{
          screen_width
          screen_height
      }
      class InputManager{
          Input_events
          GridManager
          ScreenManager
      }
      class PathManager{
          GridManager
      }
```

## Toiminta kaavio

Seuraava kaavio kuvaa suurimman osan ohjelman toiminnallisuudesta, Ohjelman osat kommunikoivat toistensa kanssa nputManageri luokan ohjeiden mukaan.
Käyttäjä ohjaa ohjelmaa näppäinkomennoilla jotka löytyvät ohjetiedostosta, jossa niihin ja niiden toimintaan voi perehtyä: 
[Ohje](https://github.com/GlobalYam/AarninOlioSimulaattori-Python/blob/main/dokumentaatio/guide.md)


```mermaid
sequenceDiagram
  actor User
  participant run_propgram
  participant InputManager
  participant GridManager
  participant ScreenManager
  participant PathManager
  participant process_data
  participant save_folder
  
  
  
  User->>run_propgram: Ohjelma aloitetaan
  run_propgram->>GridManager: create grid with size (70, 40)
  GridManager->>run_propgram: grid created with size (70, 40)

  run_propgram->>ScreenManager: create screen with resolution half of native resolution
  ScreenManager->>run_propgram: the created surface with resolution half of native resolution

  run_propgram->>InputManager: create input handler
  InputManager->>run_propgram: input handler
  
  
  User->>InputManager: press button "R"
  InputManager->>GridManager: create grid with size (70, 40)
  GridManager->>run_propgram: grid created with size (70, 40)

  run_propgram->>ScreenManager: screen updated
  ScreenManager->>run_propgram: draw to screen


  User->>InputManager: press button "D"
  InputManager->>GridManager: Connect doors
  GridManager->>PathManager: Connect doors on given grid: (my grid)
  PathManager->>GridManager: Connected doors

  GridManager->>run_propgram: grid updated with doors

  run_propgram->>ScreenManager: screen updated
  ScreenManager->>run_propgram: draw to screen


  User->>InputManager: press button "S"
  InputManager->>GridManager: Save floor
  GridManager->>process_data: Save given grid: (my grid) to file path (save_folder)
  process_data->>save_folder: Save data of grid in text doors
  save_folder->>process_data: Data saved!

  User->>InputManager: press button "L"
  InputManager->>GridManager: Load floor
  GridManager->>process_data: Load next file in file path (save_folder)
  process_data->>save_folder: Load data of file in folder
  save_folder->>process_data: Data Loaded!
  process_data->>GridManager: Grid updated!

  GridManager->>run_propgram: grid updated as loaded file

  run_propgram->>ScreenManager: screen updated
  ScreenManager->>run_propgram: draw to screen

  User->>InputManager: press button "Q"
  InputManager->>run_propgram: exit program.
  
```
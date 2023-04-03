## Scan-Tailor-Tool
Scan Tailor Tool er et værktøj til afskilling af dobbeltsidet pdf´er. 
Værktøjet består af tre dele. pdf2jgp, Scan Tailor og images2jgp


pdf2jgp's source code findes i dette repository

Scan Tailor´s source code findes her: https://github.com/scantailor/scantailor (bemærk at Scan Tailor vedligeholdelse er udgået)

images2jgp's source code findes i repository "smart-client"


### GUI klient - pdf2jgp
En lille Gooey-baseret klient til at omdanne hvert enkel side i en pdf til en jgp file.


### Releases
Pyinstaller virker med følgende kald:

`poetry run pyinstaller --onefile --windowed --name pdf2jgp .\scantailor_tool\pdf2jgp.py`

Kaldet genererer en enkelt pdf2jgp.exe fil, som ikke åbner et konsolvindue.

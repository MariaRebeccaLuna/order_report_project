# Order Report Project - README

## Om projektet:
Det här projektet är en refaktorering av ett befintligt Python-program som arbetar med orderdata från encsv-fil.
Programmet läser in orderdata, kontrollerar att nödvändiga kolumner finns, bearbetar data och skapar sammanställningar för:
- Total försäljning
- Antal ordrar
- Antal returer
- Försäljning per produktkategori
- Försäljning per region

Rapporterna sparas som csv-filer i mappen "output".
Projektet har förbättrats med tydligare projektstruktur, felhantering, logging, dataclass och automatiska tester med "pytest".

## Projektets nya struktur:
order_report_project/
- data 
    - orders.csv
- order_report
    - __init__.py
    - config.py
    - loading.py
    - processing.py
    - reporting.py
    - validation.py
- output
    - category_report.csv
    - overview.csv
    - region_report.csv
- tests
    - test_validation.py
    - test_processing.py
- code_review.md
- main.py
- order_report_original.py
- README.md

## Vad gör alla moduler?
- "main.py" är programmets startpunkt och samordnar de olika delarna.
- "config.py" innehåller projektets konfiguration och sökvägar.
- "loading.py" läser in all orderdata från csv-filen.
- "validation.py" kontrollerar att obligatoriska kolumner finns.
- "processing.py" städar och bearbetar data samt beräknar ordervärden.
- "reporting.py" skapar och sparar rapporterna.
- "tests/" innehåller de automatiska testerna.
- "code_review.md" beskriver problem i orginalkoden, förklarar varför det är problem och de genomförda förbättringarna.

## Installation:
Projektet använder Python och Python-biblioteken: pandas och pytest. Detta måste installeras om de inte redan är det.
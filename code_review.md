# Code Review - Order Report Project

## Syfte:
Syftet med code review är att identifiera problem i den ursprungliga koden och beskriva hur koden har förbättrats. Målet har varit att göra programmet mer strukturerat, lättare att förstå, testa och underhålla.

## 1. All kod låg i en fil

### Problem:
Den ursprungliga koden innehöll flera olika delar av programmet i samma fil. T.ex inläsning av data, bearbetning, beräkningar och skapande av rapporter.

### Varför är detta ett problem?
När mycket kod ligger i samma fil blir programmet svårare att läsa och ändra. Det blir också svårare att hitta var en viss funktion finns.

### Förbättring som har gjorts:
Koden har delats upp i flera moduler, där varje modul ansvarar för var sin uppgift:
- "loading.py" läser in all data.
- "validation.py" kontrollerar all data.
- "processing.py" bearbetar och beräknar all data.
- "reporting.py" skapar och sparar rapporter.
- "config.py" innehåller projektets konfiguration.

---

## 2. Otydligt ansvar mellan olika delar

### Problem:
I den ursprungliga lösningen var flera olika uppgifter blandade med varandra.

### Varför är detta ett problem?
Om samma del av programmet båda ska läsa data, kontrollera data och skapa rapporter blir koden svårare att förstå och underhålla/göra ändringar.

### Förbättring som har gjorts:
Programmet har delats upp i funktioner med tydliga ansvarsområden.

---

## 3. Begränsad felhantering

### Problem:
Programmet hade inte tillräckligt tydliga kontroller för om data eller filer saknades.

### Varför är detta ett problem?
Om en fil saknas eller om obligatoriska kolumner saknas kan programmet annars krascha senare med ett mindre tydligt fel.

### Förbättring som har gjorts:
Kontroller har lagts till i "loading.py" och i "validation.py".

--- 

## 4. Ingen automatisk testing

### Problem:
Den ursprungliga lösningen hade inga automatiska tester.

### Varför är detta ett problem?
Det blir svårare att kontrollera att beräkningarna fungerar efter att koden har ändrats.

### Förbättring som har gjorts:
Tester med "pytest" har lagts till.
Det testar bl.a att: ordervärdet beräknas korrekt, rabatt beräknas korrekt och att ett fel uppstår när de obligatoriska kolumnerna saknas.

--- 

## 5. Kör informationen hanteras inte konsekvent

### Problem:
Information om programmets körning hanterades tidigare med "print()".

### Varför är detta ett problem?
"print()" är inte lika användbart som logging när man vill följa vad som händer i programmet.

### Förbättring som har gjort:
Logging har lagts till och logger används i modulerna.

## 6. Konfigurationen var inte samlad

### Problem:
Sökvägarna till data och output behövdes hanteras separat.

### Varför är detta ett problem?
Om flera delar av programmet behöver samma sökvägar kan det bli svårare att ändra konfigurationen.

### Förbättring som har gjorts:
En "dataclass" som heter "ReportConfig" skapades. Den gör konfigurationen mer samlad och tydlig.

## Sammanfattning av hela projektet:
Efter refaktoreringen är projektet uppdelat i tydligare moduler med stöd för felhantering, logging och en dataclass. Programmet skapar samma fyra rapporter som originalet: `overview.csv`, `sales_by_category.csv`, `sales_by_region.csv` och `returns_by_category.csv`. Rapporterna innehåller information om försäljning, antal ordrar, returer och returgrad enligt respektive rapports syfte. Automatiska tester med pytest används för att kontrollera delar av programmets funktionalitet. Den nya strukturen gör koden enklare att förstå, testa, ändra och vidareutveckla.

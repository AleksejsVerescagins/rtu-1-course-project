# Projekta uzdevums
Šī programma ir izstrādāta, lai automātiski dzēstu vecākus failus no norādītās mapes, paliekot tikai jaunākajiem failiem. Programmu var izmantot, piemēram, lai regulāri attīrītu lejupielāžu mapes no veciem failiem un saglabātu tikai noderīgo saturu.

# Izmantotās Python bibliotēkas
**os**: Šī bibliotēka nodrošina operētājsistēmas funkcionalitāti, ļaujot piekļūt failu sistēmai, pārvaldīt failus un mapes.

**time**: Šī bibliotēka piedāvā funkcijas, kas saistītas ar laiku. Šajā gadījumā tā tiek izmantota, lai iegūtu pašreizējo laiku un salīdzinātu to ar failu modificēšanas laikiem.

# Programmatūras izmantošanas metodes
Mainīgais **download_folder**: Norādiet pilnu ceļu uz mapi, kuru vēlaties attīrīt no vecajiem failiem. Piemēram, *download_folder = "C:/Users/Main/Downloads"*.

Funkcija **remove_old_files**: Funkcija tiek izsaukta, padodot mapes ceļu un, pēc nepieciešamības, dienu slieksni, kuras laikā failiem jābūt, lai netiktu dzēsti. Piemēram, *remove_old_files(download_folder, days_threshold=7)* nozīmēs, ka tiks dzēsti visi faili, kuri ir vecāki par 7 dienām.

# Darbība
Skripts pārbauda visus failus norādītajā direktorijā un dzēš tos, kuri ir vecāki par iestatīto laika sliekšņa vērtību. Informācija par dzēstajiem failiem tiks izvadīta konsolē.

# Lietošana
Norādiet direktoriju: Ievietojiet jūsu vēlamā direktorija ceļu skripta galvenajā funkcijā:
*download_folder = "C:/Users/Main/Downloads"*

Iestatiet dienu sliekšņus (pēc noklusējuma 1 nedēļa): Jūs varat pielāgot, cik veciem failiem jābūt, mainot dienu sliekšņa vērtību:
Pēc noklusējuma, faili, kuri ir vecāki par 1 nedēļu, tiks dzēsti
*remove_old_files(download_folder, days_threshold=7)*

Lai palaistu skriptu, izpildiet to ar Python interpretatoru.
*python your_script_name.py*

<sub>Piezīme: Pirms skripta izmantošanas pārliecinieties, ka saprotat, kā tas darbojas, un veiciet nepieciešamos pielāgojumus, lai izvairītos no nevēlamām datu zaudēšanām.</sub>

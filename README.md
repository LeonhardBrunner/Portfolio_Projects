# [Friendly AI Agent]

> [Die Streamlit-WebApp soll Dokumente unterschiedlicher Clienten (Unternehmen, Kanzleien, ...) hochladen und in einer Datenbank speichern können. Danach wertet ein AI Agent z.B. Kennzahlen einer Rechnung aus und nutzt diese Kennzahlen für z.B. vorgeschlagene Optimierungen. Die gewonnenen Daten und KPIs sollen anschließend visualisiert werden. Der AI Agent ist dabei als separates Modul geplant, sodass man jederzeit und plattformübergreifend mit dem Agent interagieren kann.]

**Status:** 🚧 In Arbeit · Letzte Aktualisierung: [21.10.2026]

> ⚠️ **Hinweis zu den Daten:** Alle Beispieldokumente in diesem Repository sind frei erfunden. Es werden keine echten Rechnungen, Mandanten- oder Personendaten verwendet.

---

## Inhaltsverzeichnis

1. [Ziel und Motivation](#1-ziel-und-motivation)
2. [Funktionsumfang und Status](#2-funktionsumfang-und-status)
3. [Module](#3-module)
4. [Technologien](#4-technologien)
5. [Installation und Start](#5-installation-und-start)
6. [Datenschutz und Sicherheit](#6-datenschutz-und-sicherheit)
7. [Roadmap](#7-roadmap)
8. [Lizenz und Kontakt](#8-lizenz-und-kontakt)

---

## 1. Ziel und Motivation

[

Lernziel: KI-Anbindung, Datenverarbeitung, Betrieb auf eigener Infrastruktur.

Für wen könnte das Projekt interessant sein?
- Mittelständische Unternehmen, die veraltete Prozesse nutzt.
- Kanzleien.

Was soll das Projekt lösen?
- Manuelles Abtippen/Einscannen von Unterlagen soll wegfallen.
- Der AI Agent soll durch das KPI-Cockpit und die Visualisierung verdeutlichen, wo im Sinne des Kunden optimiert werden kann.]

## 2. Funktionsumfang und Status

| Modul | Beschreibung | Status |
|---|---|---|
| Dokument-Upload | PDF hochladen, Format prüfen, Text und Seitenvorschau anzeigen | ✅ |
| KI-Integration | Felder per Sprachmodell extrahieren | ⬜ |
| Dokumentenabgleich | Typ erkennen (Rechnung, Honorarrechnung, Fristenschreiben), Prüfregeln | ⬜ |
| Datenbank | Dokumente und Felder speichern | ⬜ |
| KPI-Cockpit | Kennzahlen für Unternehmen und Kanzlei | ⬜ |
| Visualisierung | Diagramme und Auswertungen | ⬜ |
| Deployment | Docker, eigener Server, Backup, VPN | ⬜ |

Legende: ✅ fertig · 🚧 in Arbeit · ⬜ geplant

## 3. Module

### 3.1 Dokument-Upload
[In diesem Modul kann man Dokumente (Rechnungen usw.) als fertige PDFs hochladen und anschließend in eine Datenbank speichern. Vorhandene bzw. geplante Prüfungen: Format, Datei beschädigt ja/nein, leer ja/nein. Der Text wird über PDFPlumber extrahiert und
anschließend als Image widergegeben, damit man Seite für Seite blättern kann.]

### 3.2 KI-Integration
[Geplant ist das lokale Llama 3.1 von Ollama. In der Überlegung ist auch, direkt einen funktionstüchtigen AI-Agent daraus zu machen. Modul noch in Arbeit.]

### 3.3 Dokumentenabgleich (Unternehmen und Kanzlei)

| Dokumenttyp | Welt | Wichtige Felder |
|---|---|---|
| Eingangsrechnung | Unternehmen | [Lieferant, Nummer, Datum, Netto, Steuer, Brutto, Fälligkeit] |
| Honorarrechnung | Kanzlei | [Mandant, Aktenzeichen, Zeitraum, Betrag] |
| Fristenschreiben | Kanzlei | [Aktenzeichen, Frist, Gegenstand] |

### 3.4 Datenbank
[Datenbank und genauer Inhalt/Funktion ist noch in Planung.]

### 3.5 KPI-Cockpit
[Modul ist noch in Planung. KPIs müssen sich dabei wesentlich von Unternehmen/Konzernen und z.B. Kanzleien unterscheiden.]

### 3.6 Visualisierung
[Modul ist noch in Planung. Visualisierungen sollen verdeutlichen, wo Optimierungen anfallen.]

### 3.7 Deployment
[Modul ist noch in Planung. Deployment via. eigenem Homeserver/Docker.]

## 4. Technologien

| Bereich | Werkzeug | Zweck |
|---|---|---|
| Sprache | Python [3.14.7] | Grundlage |
| Oberfläche | Streamlit [Latest] | Web-App |
| PDF | pdfplumber | Text- und Bildextraktion |
| KI | Ollama, [Llama 3.1] | lokale Extraktion |
| Datenbank | SQLite | Speicherung |
| Deployment | Docker | Containerisierung |

## 5. Installation und Start

**Voraussetzungen:** Python [Version], Ollama mit Modell Llama 3.1

1. Repository klonen: `git clone https://github.com/LeonhardBrunner/Portfolio_Projects`
2. Virtuelle Umgebung anlegen und aktivieren
3. Abhängigkeiten installieren: `pip install -r requirements.txt` (Wird noch eingefügt)
4. App starten: `streamlit run Home.py`

## 6. Datenschutz und Sicherheit

- Nur erfundene Testdaten im Repository.
- Zugangsdaten ausschließlich in der lokalen `.env`, nicht im Code.
- Lokales Modell: Dokumente verlassen den Rechner nicht.
- Hinweis: Für echte Mandanten- oder Personendaten sind zusätzliche Maßnahmen (Berufsgeheimnis, DSGVO, Zugriffskonzept) nötig, die dieses Lernprojekt nicht abdeckt.

## 7. Roadmap

- [x] Projektstruktur, Git, `.env` und `.gitignore`
- [x] Upload mit Format- und Fehlerprüfung
- [x] Textextraktion und Seitenvorschau
- [ ] Felder per KI extrahieren
- [ ] Prüfregeln und manuelle Korrektur
- [ ] Speicherung in SQLite
- [ ] Dokumenttyp erkennen (Unternehmen / Kanzlei)
- [ ] KPI-Cockpit
- [ ] Visualisierung
- [ ] Docker und Deployment
- [ ] Homeserver mit VPN, Backup und Monitoring
- [ ] [Optional: Agent für Vorsortierung oder Fragen an die Daten]

## 8. Kontakt

[Leonhard Brunner] · [GitHub: https://github.com/LeonhardBrunner] · [LinkedIn: https://www.linkedin.com/in/leonhard-brunner-24b720397/]

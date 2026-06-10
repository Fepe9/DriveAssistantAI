# Drive Assistant AI

Drive Assistant AI è un progetto personale che combina **Google Drive**, **Python** e **Claude AI** per organizzare automaticamente i file presenti nella root del proprio Drive.

L'obiettivo è ridurre il tempo speso a riordinare manualmente documenti, appunti, PDF e materiale scolastico, lasciando all'AI il compito di proporre una destinazione corretta e a Python il compito di eseguire realmente gli spostamenti.

---

# Funzionalità

## Analisi del Drive

Il sistema analizza i file presenti nella root di Google Drive e genera un report.

## Classificazione tramite AI

Claude analizza il report e propone:

* destinazione
* motivazione
* livello di confidenza

per ogni file.

## Spostamento automatico

Uno script Python:

* legge il piano generato da Claude
* mostra le proposte
* permette di scegliere quali file spostare
* crea automaticamente eventuali cartelle mancanti
* aggiorna la mappa delle cartelle
* sposta realmente i file su Google Drive

---

# Come funziona

```text
Google Drive
      ↓
export_drive.py
      ↓
drive_report.txt
      ↓
Claude Skill
      ↓
plan.json
      ↓
execute_plan.py
      ↓
Google Drive organizzato
```

---

# Requisiti

* Python 3.10+
* Account Google
* Google Drive API abilitata
* Claude con accesso alle Skills

---

# Installazione

Clonare il repository:

```bash
git clone https://github.com/TUO_USERNAME/DriveAssistantAI.git

cd DriveAssistantAI
```

Installare le dipendenze:

```bash
pip install google-api-python-client google-auth google-auth-oauthlib
```

---

# Configurazione Google Drive API

## 1. Creare un progetto Google Cloud

Aprire:

https://console.cloud.google.com/

Creare un nuovo progetto.

---

## 2. Abilitare Google Drive API

API e servizi → Libreria

Cercare:

Google Drive API

e abilitarla.

---

## 3. Creare credenziali OAuth

API e servizi → Credenziali

Crea credenziali → ID client OAuth

Tipo applicazione:

Desktop App

Scaricare il file JSON.

Rinominarlo oppure lasciarlo con il nome originale e copiarlo nella cartella del progetto.

---

## 4. Generare token.pickle

Eseguire uno script che utilizza OAuth.

Al primo avvio si aprirà il browser.

Effettuare il login con l'account Google da utilizzare.

Verrà creato automaticamente:

token.pickle

Questo file NON deve essere pubblicato su GitHub.

---

# Configurazione Claude

Creare una Skill chiamata:

Drive Assistant AI

Descrizione:

Assistente per l'organizzazione intelligente di Google Drive.

L'obiettivo della skill è analizzare report del Drive, classificare i file e proporre una struttura ordinata senza eseguire modifiche direttamente.

---

# Utilizzo quotidiano

## 1. Generare il report

Aprire il terminale nella cartella del progetto:

```bash
python export_drive.py
```

Verrà aggiornato:

```text
drive_report.txt
```

---

## 2. Aprire Claude

Creare una nuova chat.

Attivare la Skill:

```text
/drive-assistant-ai
```

Inviare:

```text
Analizza il file drive_report.txt allegato.

Per ogni file proponi:

- destinazione
- motivazione
- confidenza %

NON eseguire modifiche.

Rispondi esclusivamente in JSON valido.
```

Allegare:

```text
drive_report.txt
```

---

## 3. Salvare il piano

Claude genererà un JSON.

Salvare la risposta in:

```text
plan.json
```

---

## 4. Eseguire il piano

Nel terminale:

```bash
python execute_plan.py
```

Comparirà la lista dei file proposti.

Esempio:

```text
1. Appunti TPSIT
→ 4DS/TPSIT/Teoria

2. Leopardi
→ 4DS/Italiano/Teoria
```

---

## 5. Scegliere i file

Inserire i numeri dei file da spostare:

```text
1 2 5
```

---

## 6. Confermare eventuali nuove cartelle

Se una cartella non esiste:

```text
Cartella non trovata:
4DS/Italiano/Teoria

Crearla? (s/n)
```

Rispondendo:

```text
s
```

lo script:

* crea la cartella
* aggiorna folders.json
* sposta il file

---

# Struttura del progetto

```text
DriveAssistantAI
│
├── execute_plan.py
├── export_drive.py
├── folders.json
├── folders_backup.json
├── plan.json
├── drive_report.txt
│
├── token.pickle
├── client_secret_xxxxx.json
│
└── archive/
```

---

# Sicurezza

Aggiungere a `.gitignore`:

```text
token.pickle
client_secret*.json
```

per evitare di pubblicare credenziali private.

---

# Roadmap

## V2 (attuale)

* Analisi Drive
* Classificazione AI
* Creazione cartelle
* Spostamento automatico

## Idee future

* Gestione duplicati
* Rinomina intelligente dei file
* Analisi del contenuto dei documenti
* Organizzazione automatica dei file condivisi
* Dashboard web
* Modalità completamente automatica

---

# Licenza

Progetto personale open source creato a scopo educativo e organizzativo.

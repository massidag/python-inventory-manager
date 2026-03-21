# python-inventory-manager
Semplice tool in Python per la gestione logica di un inventario. Sviluppato durante il percorso IBM.

# 📦 Inventory Logic Tool (v1.0)

Questo progetto nasce come esercizio pratico durante il mio percorso di certificazione **IBM Data Analyst**. 
L'obiettivo è simulare la gestione delle giacenze di un magazzino tramite script Python.

### 🛠️ Tecniche utilizzate:
- Definizione di funzioni (`def`) e valori di ritorno (`return`).
- Gestione dei flussi con cicli `while`.
- Interattività tramite input utente.

### 📈 Roadmap (Prossime Release):
- **v1.1:** Esportazione del report in formato `.txt`.
- **v2.0:** Visualizzazione dati con grafici (Matplotlib).

- ### 🚀 Novità Versione 1.1 (Persistenza Dati)
In questo aggiornamento ho introdotto la gestione dell'**Output su File**:
- Utilizzo dell'istruzione `with open()` per garantire la corretta chiusura delle risorse.
- Formattazione dinamica delle stringhe per creare un report leggibile esternamente.
- Gestione della persistenza: i risultati della simulazione vengono ora salvati permanentemente.

- ### 🗄️ Versione 1.2: Database Integration

- Implementazione di SQLite per l'archiviazione strutturata.

- Utilizzo di query SQL per l'inserimento dei dati (INSERT INTO).

- Gestione della connessione e dei commit per l'integrità dei dati.

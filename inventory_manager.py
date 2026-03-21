import sqlite3
import os

# --- 1. SETUP PERCORSI ---
cartella = os.path.dirname(__file__)
db_path = os.path.join(cartella, "magazzino.db")

# --- 2. CONNESSIONE E CREAZIONE TABELLA ---
# Ci connettiamo al file. Se non esiste, Python lo crea.
conn = sqlite3.connect(db_path)
cursor = conn.cursor() # Il cursore serve per "scrivere" i comandi SQL

# Creiamo una tabella chiamata 'simulazione' con 3 colonne
cursor.execute('''CREATE TABLE IF NOT EXISTS simulazione 
                  (mese INTEGER, rimanenza INTEGER, stato TEXT)''')
conn.commit()

# --- 3. LOGICA DI CALCOLO ---
stock = int(input("Stock iniziale: "))
prelievo = int(input("Prelievo mensile: "))
attuale = stock
mese = 0

print("\nSimulazione in corso... Scrittura su Database SQL.")

while attuale > 0:
    mese += 1
    attuale -= prelievo
    rimanenza = max(0, attuale)
    status = "OK" if rimanenza > (stock * 0.2) else "LIVELLO BASSO"
    
    # --- 4. INSERIMENTO DATI IN SQL ---
    # Usiamo i '?' come segnaposto per la sicurezza dei dati
    cursor.execute("INSERT INTO simulazione VALUES (?, ?, ?)", 
                   (mese, rimanenza, status))
    
    print(f"Mese {mese}: Dati inviati al DB.")
    if mese == 24: break

# --- 5. SALVATAGGIO FINALE ---
conn.commit() # Conferma tutte le operazioni di scrittura
conn.close()  # Chiude la connessione
print("\n--- Operazione completata. Database 'magazzino.db' aggiornato. ---")

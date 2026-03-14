def calcola_scorte_residue(quantita_iniziale, prelievo_mensile):
    return quantita_iniziale - prelievo_mensile

# --- RICHIESTA DATI ALL'UTENTE ---
print("--- Configurazione Magazzino ---")
stock_iniziale = int(input("Inserisci lo stock totale disponibile: "))
media_prelievi = int(input("Quanti pezzi vengono usati ogni mese? "))

mese = 0
stock_attuale = stock_iniziale

print("\nAvvio Simulazione...")
print("-" * 25)

while stock_attuale > 0:
    mese += 1
    stock_attuale = calcola_scorte_residue(stock_attuale, media_prelievi)
    
    status = "Livello Basso" if stock_attuale < (stock_iniziale * 0.2) else "OK"
    
    print(f"Mese {mese}: Stock residuo {max(0, stock_attuale)} | Stato: {status}")
    
    if mese == 24: # Estendiamo a 2 anni la simulazione
        break
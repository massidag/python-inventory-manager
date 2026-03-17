def calcola_scorte_residue(quantita_iniziale, prelievo_mensile):
    return quantita_iniziale - prelievo_mensile

# --- INPUT ---
stock_iniziale = int(input("Stock iniziale: "))
media_prelievi = int(input("Prelievo mensile: "))

stock_attuale = stock_iniziale
mese = 0

# --- LOGICA E SCRITTURA SU FILE ---
with open("report_inventario.txt", "w") as file:
    file.write("REPORT ANALISI MAGAZZINO\n" + "="*25 + "\n")
    
    while stock_attuale > 0:
        mese += 1
        stock_attuale = calcola_scorte_residue(stock_attuale, media_prelievi)
        
        riga = f"Mese {mese}: Rimanenza {max(0, stock_attuale)}\n"
        print(riga.strip())
        file.write(riga)
        
        if mese == 24: break

print("\n--- Operazione completata. File generato. ---")

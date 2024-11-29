import tkinter as tk
from tkinter import messagebox

# Fonction pour calculer le prix
def calculer_prix():
    try:
        # Récupérer les entrées utilisateur
        cout_matieres = float(entry_cout_matieres.get())
        temps_fabrication = float(entry_temps_fabrication.get())
        tarif_horaire = float(entry_tarif_horaire.get())
        frais_fixes = float(entry_frais_fixes.get())
        marge_beneficiaire = float(entry_marge_beneficiaire.get())
        
        # Calculer le coût total
        cout_fabrication = temps_fabrication * tarif_horaire
        cout_total = cout_matieres + cout_fabrication + frais_fixes
        
        # Calculer la marge bénéficiaire
        prix_vente = cout_total * (1 + marge_beneficiaire / 100)
        
        # Afficher le prix de vente
        label_prix_vente.config(text=f"Prix de vente: {prix_vente:.2f} €")
    
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculateur de prix de vente de bijoux")

# Création des labels et champs de texte pour les entrées
label_cout_matieres = tk.Label(fenetre, text="Coût des matières premières (€):")
label_cout_matieres.grid(row=0, column=0, padx=10, pady=5)
entry_cout_matieres = tk.Entry(fenetre)
entry_cout_matieres.grid(row=0, column=1, padx=10, pady=5)

label_temps_fabrication = tk.Label(fenetre, text="Temps de fabrication (heures):")
label_temps_fabrication.grid(row=1, column=0, padx=10, pady=5)
entry_temps_fabrication = tk.Entry(fenetre)
entry_temps_fabrication.grid(row=1, column=1, padx=10, pady=5)

label_tarif_horaire = tk.Label(fenetre, text="Tarif horaire (€):")
label_tarif_horaire.grid(row=2, column=0, padx=10, pady=5)
entry_tarif_horaire = tk.Entry(fenetre)
entry_tarif_horaire.grid(row=2, column=1, padx=10, pady=5)

label_frais_fixes = tk.Label(fenetre, text="Frais fixes (€):")
label_frais_fixes.grid(row=3, column=0, padx=10, pady=5)
entry_frais_fixes = tk.Entry(fenetre)
entry_frais_fixes.grid(row=3, column=1, padx=10, pady=5)

label_marge_beneficiaire = tk.Label(fenetre, text="Marge bénéficiaire (%):")
label_marge_beneficiaire.grid(row=4, column=0, padx=10, pady=5)
entry_marge_beneficiaire = tk.Entry(fenetre)
entry_marge_beneficiaire.grid(row=4, column=1, padx=10, pady=5)

# Bouton pour effectuer le calcul
button_calculer = tk.Button(fenetre, text="Calculer", command=calculer_prix)
button_calculer.grid(row=5, column=0, columnspan=2, pady=10)

# Label pour afficher le prix de vente
label_prix_vente = tk.Label(fenetre, text="Prix de vente: ")
label_prix_vente.grid(row=6, column=0, columnspan=2, pady=5)

# Lancer l'application
fenetre.mainloop()
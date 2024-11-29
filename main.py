# main.py
import tkinter as tk
from bijoux import ouvrir_mes_bijoux
from fournisseurs import ouvrir_mes_fournisseurs

# Création de la fenêtre principale
root = tk.Tk()
root.title("Logiciel Bijoux")
root.geometry("400x300")  # Taille de la fenêtre principale

# Titre de l'application
label_titre = tk.Label(root, text="Bienvenue dans le logiciel de gestion des bijoux", font=("Arial", 14))
label_titre.pack(pady=20)

# Bouton pour ouvrir la page "Mes Bijoux"
button_bijoux = tk.Button(root, text="Mes Bijoux", width=20, height=2, command=lambda: ouvrir_mes_bijoux(root))
button_bijoux.pack(pady=10)

# Bouton pour ouvrir la page "Mes Fournisseurs"
button_fournisseurs = tk.Button(root, text="Mes Fournisseurs", width=20, height=2, command=lambda: ouvrir_mes_fournisseurs(root))
button_fournisseurs.pack(pady=10)

# Lancer la boucle principale Tkinter
root.mainloop()
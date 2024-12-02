import tkinter as tk
from tkinter import ttk
from bijoux import ouvrir_onglet_bijoux
from fournisseurs import ouvrir_onglet_fournisseurs

root = tk.Tk()
root.title("Logiciel Bijoux")

root.attributes('-fullscreen', True)

label_titre = tk.Label(root, text="Bienvenue dans le logiciel de gestion des bijoux", font=("Arial", 14))
label_titre.pack(pady=20)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True, fill="both")

frame_bijoux = tk.Frame(notebook)
frame_fournisseurs = tk.Frame(notebook)

notebook.add(frame_bijoux, text="Mes Bijoux")
notebook.add(frame_fournisseurs, text="Mes Fournisseurs")

ouvrir_onglet_bijoux(frame_bijoux)
ouvrir_onglet_fournisseurs(frame_fournisseurs)

root.mainloop()
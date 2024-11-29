# bijoux.py
import tkinter as tk

def ouvrir_mes_bijoux(root):
    # Création de la nouvelle fenêtre pour "Mes Bijoux"
    bijoux_window = tk.Toplevel(root)
    bijoux_window.title("Mes Bijoux")
    bijoux_window.geometry("300x200")  # Taille de la fenêtre
    label = tk.Label(bijoux_window, text="Bienvenue dans Mes Bijoux")
    label.pack(pady=20)

    # Vous pouvez ajouter d'autres widgets pour gérer les bijoux ici
    # Par exemple, une liste de bijoux, un formulaire, etc.
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

# Fonction pour ouvrir la page "Mes Fournisseurs"
def ouvrir_mes_fournisseurs(root):
    # Création de la nouvelle fenêtre pour "Mes Fournisseurs"
    fournisseurs_window = tk.Toplevel(root)
    fournisseurs_window.title("Mes Fournisseurs")
    fournisseurs_window.geometry("300x200")  # Taille de la fenêtre

    # Label pour le titre
    label = tk.Label(fournisseurs_window, text="Bienvenue dans Mes Fournisseurs")
    label.pack(pady=20)

    # Bouton "Ajouter un fournisseur"
    button_ajouter_fournisseur = tk.Button(fournisseurs_window, text="Ajouter un fournisseur", width=20, height=2, command=ouvrir_formulaire_ajout)
    button_ajouter_fournisseur.pack(pady=10)

# Fonction pour ouvrir la fenêtre de formulaire d'ajout d'un fournisseur
def ouvrir_formulaire_ajout():
    # Fenêtre modale pour ajouter un fournisseur
    ajout_window = tk.Toplevel()
    ajout_window.title("Ajouter un fournisseur")
    ajout_window.geometry("400x400")

    # Variables pour les champs
    image_path = tk.StringVar()
    nom_var = tk.StringVar()
    lien_var = tk.StringVar()
    identifiant_var = tk.StringVar()
    motdepasse_var = tk.StringVar()

    # Fonction pour charger une image
    def charger_image():
        try:
            selected_image = filedialog.askopenfilename(title="Choisir une image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
            if selected_image:
                # Vérification si le fichier sélectionné existe et est une image
                if os.path.isfile(selected_image) and selected_image.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path.set(selected_image)  # Stocke le chemin de l'image
                    
                    # Chargement de l'image avec Pillow pour la redimensionner si nécessaire
                    pil_image = Image.open(selected_image)
                    pil_image = pil_image.resize((100, 100), Image.ANTIALIAS)  # Redimensionner pour afficher une image plus petite
                    image_tk = ImageTk.PhotoImage(pil_image)
                    
                    image_label.config(image=image_tk)  # Mettre à jour l'image affichée
                    image_label.image = image_tk  # Garder une référence à l'image pour éviter la collecte de déchets
                    image_label.config(text="Image sélectionnée : " + os.path.basename(selected_image))  # Afficher le nom de l'image
                else:
                    messagebox.showerror("Erreur", "Le fichier sélectionné n'est pas une image valide.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de la sélection de l'image : {e}")

    # Label pour l'image
    image_label = tk.Label(ajout_window, text="Aucune image sélectionnée", width=40, height=10)
    image_label.pack(pady=10)

    # Bouton pour charger l'image
    button_image = tk.Button(ajout_window, text="Charger une image", command=charger_image)
    button_image.pack(pady=5)

    # Champ de saisie pour le nom
    tk.Label(ajout_window, text="Nom du fournisseur :").pack(pady=5)
    entry_nom = tk.Entry(ajout_window, textvariable=nom_var, width=40)
    entry_nom.pack(pady=5)

    # Champ de saisie pour le lien
    tk.Label(ajout_window, text="Lien du fournisseur :").pack(pady=5)
    entry_lien = tk.Entry(ajout_window, textvariable=lien_var, width=40)
    entry_lien.pack(pady=5)

    # Champ de saisie pour l'identifiant
    tk.Label(ajout_window, text="Identifiant :").pack(pady=5)
    entry_identifiant = tk.Entry(ajout_window, textvariable=identifiant_var, width=40)
    entry_identifiant.pack(pady=5)

    # Champ de saisie pour le mot de passe
    tk.Label(ajout_window, text="Mot de passe :").pack(pady=5)
    entry_motdepasse = tk.Entry(ajout_window, textvariable=motdepasse_var, width=40, show="*")
    entry_motdepasse.pack(pady=5)

    # Fonction pour ajouter le fournisseur
    def ajouter_fournisseur():
        # Vérifier si tous les champs sont remplis
        if not nom_var.get() or not lien_var.get() or not identifiant_var.get() or not motdepasse_var.get() or not image_path.get():
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis")
        else:
            # Logique pour ajouter le fournisseur (ici nous afficherons juste un message de confirmation)
            messagebox.showinfo("Succès", "Fournisseur ajouté avec succès")
            ajout_window.destroy()  # Fermer la fenêtre d'ajout

    # Bouton pour ajouter le fournisseur
    button_ajouter = tk.Button(ajout_window, text="Ajouter le fournisseur", width=20, height=2, command=ajouter_fournisseur)
    button_ajouter.pack(pady=20)
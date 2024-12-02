import tkinter as tk
from tkinter import messagebox

def ouvrir_onglet_fournisseurs(frame):
    label_fournisseurs = tk.Label(frame, text="Bienvenue dans l'onglet Mes Fournisseurs", font=("Arial", 12))
    label_fournisseurs.pack(pady=20)

    # Fonction pour ajouter un fournisseur
    def ajouter_fournisseur():
        ajout_window = tk.Toplevel(frame)
        ajout_window.title("Ajouter un fournisseur")
        ajout_window.geometry("300x150")

        label_nom = tk.Label(ajout_window, text="Nom du fournisseur :")
        label_nom.pack(pady=5)
        entry_nom = tk.Entry(ajout_window, width=30)
        entry_nom.pack(pady=5)

        # Fonction pour enregistrer le fournisseur et mettre à jour la liste
        def enregistrer_fournisseur():
            fournisseur_nom = entry_nom.get().strip()
            if fournisseur_nom:
                try:
                    # Enregistrer le nom du fournisseur dans le fichier
                    with open("fournisseurs.txt", "a") as file:
                        file.write(fournisseur_nom + "\n")
                    
                    # Mettre à jour la liste des fournisseurs dans l'interface
                    afficher_fournisseurs()  # Mise à jour de l'affichage
                    messagebox.showinfo("Succès", "Fournisseur ajouté avec succès.")
                    ajout_window.destroy()  # Fermer la fenêtre après ajout
                except Exception as e:
                    messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {e}")
            else:
                messagebox.showerror("Erreur", "Le nom du fournisseur ne peut pas être vide.")

        button_enregistrer = tk.Button(ajout_window, text="Enregistrer", command=enregistrer_fournisseur)
        button_enregistrer.pack(pady=10)

    # Bouton pour ajouter un fournisseur
    button_ajouter_fournisseur = tk.Button(frame, text="Ajouter un fournisseur", width=20, height=2, command=ajouter_fournisseur)
    button_ajouter_fournisseur.pack(pady=10)

    # Fonction pour afficher les fournisseurs dans l'onglet
    def afficher_fournisseurs():
        # Supprimer les anciens labels avant de tout réafficher
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Label) and widget != label_fournisseurs:
                widget.destroy()

        try:
            # Lire les fournisseurs depuis le fichier
            with open("fournisseurs.txt", "r") as file:
                fournisseurs = file.readlines()
                fournisseurs = [f.strip() for f in fournisseurs]

                # Afficher les fournisseurs avec boutons "Editer" et "Supprimer"
                for fournisseur in fournisseurs:
                    frame_fournisseur = tk.Frame(frame)
                    frame_fournisseur.pack(pady=2, fill="x")

                    label_fournisseur = tk.Label(frame_fournisseur, text=fournisseur, font=("Arial", 10))
                    label_fournisseur.pack(side="left", padx=10)

                    # Bouton "Editer"
                    button_editer = tk.Button(frame_fournisseur, text="Editer", command=lambda fournisseur=fournisseur: editer_fournisseur(fournisseur))
                    button_editer.pack(side="left", padx=5)

                    # Bouton "Supprimer"
                    button_supprimer = tk.Button(frame_fournisseur, text="Supprimer", command=lambda fournisseur=fournisseur: supprimer_fournisseur(fournisseur))
                    button_supprimer.pack(side="left", padx=5)
        except FileNotFoundError:
            pass  # Si le fichier n'existe pas encore, aucun fournisseur n'est affiché

    # Fonction pour modifier le fournisseur
    def editer_fournisseur(fournisseur):
        edit_window = tk.Toplevel(frame)
        edit_window.title("Editer fournisseur")
        edit_window.geometry("300x150")

        label_nom = tk.Label(edit_window, text="Nom du fournisseur :")
        label_nom.pack(pady=5)
        entry_nom = tk.Entry(edit_window, width=30)
        entry_nom.insert(0, fournisseur)  # Afficher le nom actuel
        entry_nom.pack(pady=5)

        # Fonction pour enregistrer le nouveau nom
        def enregistrer_modifications():
            nouveau_nom = entry_nom.get().strip()
            if nouveau_nom and nouveau_nom != fournisseur:
                try:
                    with open("fournisseurs.txt", "r") as file:
                        fournisseurs = file.readlines()
                    # Supprimer le fournisseur original et ajouter le modifié
                    with open("fournisseurs.txt", "w") as file:
                        for f in fournisseurs:
                            if f.strip() != fournisseur:
                                file.write(f)
                        file.write(nouveau_nom + "\n")
                    # Mettre à jour l'affichage
                    afficher_fournisseurs()
                    messagebox.showinfo("Succès", "Fournisseur modifié avec succès.")
                    edit_window.destroy()  # Fermer la fenêtre
                except Exception as e:
                    messagebox.showerror("Erreur", f"Erreur lors de la modification : {e}")
            else:
                messagebox.showerror("Erreur", "Le nom ne peut pas être vide ou identique.")

        button_enregistrer = tk.Button(edit_window, text="Enregistrer", command=enregistrer_modifications)
        button_enregistrer.pack(pady=10)

    # Fonction pour supprimer un fournisseur
    def supprimer_fournisseur(fournisseur):
        try:
            with open("fournisseurs.txt", "r") as file:
                fournisseurs = file.readlines()
            # Supprimer le fournisseur
            with open("fournisseurs.txt", "w") as file:
                for f in fournisseurs:
                    if f.strip() != fournisseur:
                        file.write(f)
            # Mettre à jour l'affichage
            afficher_fournisseurs()
            messagebox.showinfo("Succès", "Fournisseur supprimé avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression : {e}")

    # Initialiser l'affichage des fournisseurs au démarrage
    afficher_fournisseurs()
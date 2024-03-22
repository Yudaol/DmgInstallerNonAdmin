import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import re

def open_dmg_and_copy_app():
    # Demander à l'utilisateur de sélectionner un fichier DMG
    dmg_file_path = filedialog.askopenfilename(title="Sélectionner un fichier DMG", filetypes=(("DMG files", "*.dmg"), ("All files", "*.*")))

    # Vérifier si un fichier a été sélectionné
    if dmg_file_path:
        # Créer le dossier /Users/L'users/Applications s'il n'existe pas
        applications_folder_path = os.path.expanduser("~/Applications")
        if not os.path.exists(applications_folder_path):
            os.makedirs(applications_folder_path)
        
        # Montage du fichier DMG
        mount_output = subprocess.check_output(["hdiutil", "attach", "-nomount", dmg_file_path]).decode("utf-8")
        match = re.search(r"(/dev/disk\S+)\s*(.*)$", mount_output)
        if match:
            mounted_volume_path = match.group(1)
            subprocess.run(["hdiutil", "mount", mounted_volume_path])

            # Récupération du nom complet du volume monté
            volume_info_output = subprocess.check_output(["diskutil", "info", "-plist", mounted_volume_path]).decode("utf-8")
            match = re.search(r"<key>VolumeName</key>\s*<string>(.*?)</string>", volume_info_output)
            if match:
                selected_volume = match.group(1)

                # Vérifier si le volume sélectionné existe
                if selected_volume:
                    print("Volume monté:", selected_volume)

                    # Continuez votre traitement ici
                    # Recherche du fichier .app dans le volume monté
                    app_found = False
                    for root, dirs, files in os.walk(os.path.join("/Volumes", selected_volume)):
                        for dir in dirs:
                            if dir.endswith(".app"):
                                app_found = True
                                app_path = os.path.join(root, dir)
                                # Copie du dossier .app dans le dossier Applications
                                subprocess.run(["cp", "-R", app_path, applications_folder_path])
                                print("Extraction terminée avec succès.")
                                break
                        if app_found:
                            break
                    if not app_found:
                        print("Aucun fichier .app trouvé dans le volume monté.")
                    
                    # Démontage du volume
                    subprocess.run(["hdiutil", "detach", mounted_volume_path])
                else:
                    print("Impossible de récupérer le nom du volume monté.")
            else:
                print("Impossible de récupérer le nom du volume monté.")
        else:
            print("Impossible de monter le volume.")
    else:
        print("Aucun fichier sélectionné.")

# Appeler la fonction pour ouvrir le fichier DMG et copier le .app
open_dmg_and_copy_app()

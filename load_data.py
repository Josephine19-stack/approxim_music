import os
import csv
import hashlib
from mido import MidiFile,  KeySignatureError
# oublie pas  le : %pip install mido

MIDI_EXTENSIONS = [".mid", ".midi", ".MID", ".MIDI"]
def get_midi_files(files):
    midi_files = []
    for file_name in files:
        # Check if it is a midi file
        _, extension = os.path.splitext(file_name)
        if extension in MIDI_EXTENSIONS:
            midi_files.append(file_name)

    return midi_files

def validate_midi_file(file_path):
    """
    Vérifie si le fichier MIDI contient des valeurs acceptables.
    Ignore les fichiers qui lèvent des exceptions de type KeySignatureError ou similaires.

    :param file_path: Chemin vers le fichier MIDI.
    :return: True si le fichier est valide, False sinon.
    """
    try:
        MidiFile(file_path)  # Tentative de chargement
        return True
    except (KeySignatureError, ValueError) as e:
        print(f"Fichier ignoré : {file_path} - Erreur : {e}")
        return False
    

def extract_midi_features_with_order(file_path):
    """
    Extracts ordered notes from a MIDI file with pitch, duration, and velocity.

    :param file_path: Path to the MIDI file.
    :return: A dictionary with note index as the key and a dictionary of note features as the value.
    """
    partition = [] # = partition  Quadruplets (type, p, v, time)
    midi = MidiFile(file_path)
    time_elapsed = 0
    note_on_times = {}
    note_index = 0

  
    for msg in midi:
        time_elapsed += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            note_on_times[msg.note] = (time_elapsed, msg.velocity)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            if msg.note in note_on_times:
                start_time, velocity = note_on_times[msg.note]
                duration = time_elapsed - start_time
                partition.append((msg.note,duration,velocity,start_time)) #pitch, duration, velocity , time
                note_index += 1
                del note_on_times[msg.note]

    return partition

def adl_load_dataset_to_csv(adl_path, output_csv):
    """
    Parcourt le répertoire ADL pour charger les fichiers MIDI,
    extrait les informations importantes et les sauvegarde dans un fichier CSV.

    :param adl_path: Chemin vers le répertoire contenant le dataset ADL.
    :param output_csv: Chemin vers le fichier CSV de sortie.
    """
    data_rows = []

    # Parcourir les fichiers dans le chemin donné
    for dirpath, _, files in os.walk(adl_path):
        if not files:
            continue
        
        # Extraire les informations de genre, sous-genre et artiste
        path_parts = dirpath.split(os.sep)
        if len(path_parts) < 3:
            continue

        genre = path_parts[-3]
        subgenre = path_parts[-2]
        artist = path_parts[-1]
        
        # Charger les fichiers MIDI
        for filename in get_midi_files(files):
            file_path = os.path.join(dirpath, filename)
            
            if not validate_midi_file(file_path):
                continue 
            
            with open(file_path, "rb") as midi_file:
                file_hash = hashlib.md5(midi_file.read()).hexdigest()
    
            # Extraire les données musicales du fichier MIDI
            notes_features = extract_midi_features_with_order(file_path)
            data_rows.append({
                    "Genre": genre,
                    "Subgenre": subgenre,
                    "Artist": artist,
                    "FileHash": file_hash,
                    "Notes": notes_features
                })

    # Écriture des informations dans un fichier CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Genre", "Subgenre", "Artist", "FilePath", "FileHash", "Notes"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_rows)

    print(f"Données sauvegardées dans {output_csv}")  
    
    
if __name__ == "__main__":

    midi_directory = "adl-piano-midi"
    output_directory = "music_metrics.csv"

    # Charger les données et les exporter
    adl_load_dataset_to_csv(midi_directory, output_directory)
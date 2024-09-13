import os
import random
import subprocess
import multiprocessing

def install_tqdm():
    try:
        subprocess.check_call(["python", "-m", "pip", "install", "tqdm"])
    except subprocess.CalledProcessError:
        try:
            subprocess.check_call(["python3", "-m", "pip", "install", "tqdm"])
        except subprocess.CalledProcessError:
            raise RuntimeError("Impossible d'installer 'tqdm'. Veuillez l'installer manuellement.")

try:
    from tqdm import tqdm
except ImportError:
    print("La bibliothèque 'tqdm' n'est pas installée. Installation en cours...")
    install_tqdm()
    from tqdm import tqdm

def generate_mifare_key():
    return ''.join([f'{random.randint(0, 255):02X}' for _ in range(6)])

def worker_generate_keys(num_keys, progress_queue):
    local_keys = set()
    while len(local_keys) < num_keys:
        key = generate_mifare_key()
        if key not in local_keys:
            local_keys.add(key)
            progress_queue.put(key)  

def generate_unique_keys_to_file(filename, num_keys, num_processes):
    keys_per_process = num_keys // num_processes
    extra_keys = num_keys % num_processes

    progress_queue = multiprocessing.Queue()

    temp_filename = filename + '.tmp'

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    processes = []
    generated_keys = 0

    try:
        for i in range(num_processes):
            process_keys = keys_per_process + (1 if i < extra_keys else 0)
            p = multiprocessing.Process(target=worker_generate_keys, args=(process_keys, progress_queue))
            processes.append(p)
            p.start()

        unique_keys = set()

        with open(temp_filename, 'w') as f:
            with tqdm(total=num_keys, desc="Génération des clés MIFARE", unit="clé") as pbar:
                while len(unique_keys) < num_keys:
                    key = progress_queue.get()
                    if key not in unique_keys:
                        unique_keys.add(key)
                        f.write(key + '\n')
                        generated_keys += 1
                    pbar.update(1)

        for p in processes:
            p.join()

        os.rename(temp_filename, filename)

    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        if os.path.exists(temp_filename):
            os.rename(temp_filename, filename)
        file_size = os.path.getsize(filename) / (1024 ** 3)
        print("")
        print(f"{generated_keys} clés MIFARE uniques ont été générées et stockées dans {filename}.")
        print(f"Taille du fichier : {file_size:.2f} Go")
        print("")
        raise

def main():
    filename = 'mifare.keys'

    if os.path.exists(filename):
        os.remove(filename)

    print("")
    print("Toutes les bibliothèques sont bien installées. Démarrage en cours...")

    print("")
    print("")
    print("Generateur de clé Mifare by stanthblt")
    print("")
    print("https://github.com/stanthblt")
    print("")
    print("")

    num_keys = int(input("Nombre de clé à générer: "))
    num_processes = multiprocessing.cpu_count()
    print("")

    generate_unique_keys_to_file(filename, num_keys, num_processes)

    file_size = os.path.getsize(filename) / (1024 ** 3)
    print("")
    print(f"{num_keys} clés MIFARE uniques ont été générées et stockées dans {filename}.")
    print(f"Taille du fichier : {file_size:.2f} Go")
    print("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur. Fermeture en cours...")
        print("")
        print("")
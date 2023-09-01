import os
import threading
import subprocess

def run_test(file_path, result_dir):
    # Exécute le test unitaire
    try:
        result_log = os.path.join(result_dir, f"{os.path.basename(file_path)}.log")
        result_txt = os.path.join(result_dir, "resultat.txt")

        # Exécution du test et enregistrement des sorties
        with open(result_log, "w") as log_file:
            subprocess.run(["python", file_path], stdout=log_file, stderr=subprocess.STDOUT)

        # Analyse des résultats et écriture dans le fichier resultat.txt
        with open(result_log, "r") as log_file, open(result_txt, "a") as result_file:
            log_content = log_file.read()
            result_file.write("="*30 + f"\nTest: {os.path.basename(file_path)}\n" + "="*30 + "\n")
            result_file.write(log_content)
            result_file.write("="*60 + "\n")

    except Exception as e:
        print(f"Error running test {file_path}: {e}")

def main():
    test_dir = "test_unitaire"
    result_dir = "Resultat_Test"

    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    threads = []

    # Parcours des fichiers .py dans le répertoire test_unitaire
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                thread = threading.Thread(target=run_test, args=(file_path, result_dir))
                threads.append(thread)
                thread.start()

    # Attendre la fin de tous les threads
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

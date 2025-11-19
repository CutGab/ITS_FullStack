# Esercizio 1
# Crea un context manager usando una classe

# Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

# Esempio di funzionamento:

# Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

# with FileManager('example.txt', 'w') as f:

#     f.write('Hello, world!')

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("Resource Acquired.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print("Resource Released.")

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")

        return False
    
path = r"C:\Users\utente\Desktop\ITS_2\Python\Lezione_15\Es_1\example.txt"

with FileManager(path, 'w') as f:
    f.write('Hello, world!')

with FileManager(path, 'r') as f:
    content = f.read()
    print("File content:", content)
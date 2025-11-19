# Esercizio 2
# Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

# with Timer():

#     time.sleep(1)

# time elapsed: 1.00000

# in questo esempio il tempo passato non sarà mai uguale a 1

import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        elapsed = end_time - self.start_time
        print(f"Time elapsed: {elapsed:.5f} seconds")

with Timer():

    time.sleep(1)
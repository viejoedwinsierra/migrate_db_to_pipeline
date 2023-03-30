import pandas as pd
import numpy as np

def run():
     opencsv()


def opencsv():
    df = pd.DataFrame(pd.read_csv ( 'directorios.csv', sep = ';'))
    dir = np.array((df.iloc[:, 3]))
    print(np.where(dir ))
    print(df)

def lookup_key_words():
    pass

def write_out():
    pass

if __name__ == "__main__" :
    run()
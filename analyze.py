import pandas as pd
import numpy as np

# Aumenta il numero di righe e colonne
pd.set_option('display.max_rows', 100)  # Mostra fino a 100 righe

def clean_data(data):
    df = pd.DataFrame(data)
    df.replace(["Assente", "Ritirato", ""], np.nan, inplace=True)
    df.replace("30 e lode", 30, inplace=True)
    df = df.dropna()
    df = df.replace({',': '.'}, regex=True)
    df = df.apply(pd.to_numeric, errors='coerce')
    df.loc[df.isna().any(axis=1)] = np.nan
    df = df.reset_index(drop=True)
    return df

def promoted(df):
    return df["Esito"].count()

def failed(df):
    return df["Esito"].isna().sum()

def pass_rate(df):
    return [
        float(np.round(promoted(df) * 100 / len(df), 2)),
        float(np.round(failed(df) * 100 / len(df), 2))
    ]

def mean(df, header):
    return df[header].mean()
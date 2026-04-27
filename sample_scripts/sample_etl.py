import pandas as pd

def run_pipeline(path):
    df = pd.read_csv(path)
    df = df.dropna()
    return df

import zipfile
import pandas as pd
import os


def unzip_data(files):
    '''
    Returns unzipped files in input directory
    input: list of zip files
    output: unzipped files in input directory
    '''
    for file in files:
        with zipfile.ZipFile(file, "r") as z:
            z.extractall("input")


unzip_data(["learning-equality-curriculum-recommendations.zip"])


def convert_to_parquet(files):
    '''
    Converts csv files to parquet
    input: list of csv files
    output: parquet files in input directory
    '''
    for file in files:
        df = pd.read_csv(file)
        df.to_parquet(file.replace(".csv", ".parquet"))
        os.remove(file)


convert_to_parquet(["input/content.csv",
                    "input/correlations.csv", "input/topics.csv"])

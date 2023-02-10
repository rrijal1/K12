# unzip data
import zipfile

# function to unzip data
# Takes list of files to unzip
def unzip_data(files):
    for file in files:
        with zipfile.ZipFile(file,"r") as z:
            z.extractall("input")

# unzip data
unzip_data(["learning-equality-curriculum-recommendations.zip"])



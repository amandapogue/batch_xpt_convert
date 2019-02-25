import glob, os 
import xport
import pandas as pd

# This bit of code makes a new folder for the modified files
os.makedirs(os.getcwd() + "/csv")

# This tells the program to convert all of the files in the folder of the type .xpt   
for infile in glob.glob("*.XPT"):
    file, ext = os.path.splitext(infile)
    with open(infile, 'rb') as f:
    	df = xport.to_dataframe(f)
    	filename = os.getcwd() + "/csv/" + file + '.csv.gz'
    	df.to_csv(filename, index=False, compression='gzip')
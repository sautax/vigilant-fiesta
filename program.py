import os
import pickle
import urllib.request
directory = "temp"
file = directory+"/repo.dat"


if not os.path.exists(directory):
    os.makedirs(directory)


urllib.request.urlretrieve('https://github.com/sautax/vigilant-fiesta/blob/master/repo.dat?raw=true',file)

with open(file,"rb") as f:
    array = pickle.load(f)

print(array)

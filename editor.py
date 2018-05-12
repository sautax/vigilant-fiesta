import pickle

array = []





with open('repo.dat', 'wb') as fp:
    pickle.dump(array, fp)

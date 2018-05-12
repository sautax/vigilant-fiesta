import pickle

array = [['title',['sub1',"action(url)"],['sub2','action']],[]]





with open('repo.dat', 'wb') as fp:
    pickle.dump(array, fp)

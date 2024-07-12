import pickle

data = ['parthadmin', 'bank']

with open("main/files/cred.dat", "wb") as cred:
    pickle.dump(data, cred)

import pickle

file='svc.pickle'
file2=open(file,'rb')
poses=pickle.load(file2)
file2.close()

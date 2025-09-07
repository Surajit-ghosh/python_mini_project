# import pickle
# list=[10,20,30,40]
# file=open("txt.txt","wb")
# pickle.dump(list,file)
# file.close()
import pickle
f=open("txt.txt","rb")
l=pickle.load(f)
print(l)

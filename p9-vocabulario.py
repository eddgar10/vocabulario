import os
from nltk.tokenize import word_tokenize

global Voc

class Vocabulario:
    def __init__(self,nombre,dir,dir1):
        self.Vocabulario=[]
        self.VocR=[]
        self.VN=0
        self.filterm=5#filtro para eliminar los mas bajos
        self.filterM=50#numero de datos mejores
        self.VocD(nombre,dir)
        self.VocD(nombre,dir1)
        self.Eli()
        self.Ordena()
        #print(self.Vocabulario)
        #print(self.VocR)



    def VocD(self,nombre,dir):
        for doc in os.listdir(dir):
            nuevo1=open("./"+dir+"/"+doc,"r")
            cadena=nuevo1.readline()
            resul=word_tokenize(cadena)

            while(len(resul)>0):
                Palabra=resul[0]
                if(self.Vocabulario.count(Palabra)==0):
                    self.Vocabulario.append(Palabra)
                    self.VocR.append(1)
                    resul.pop(0)
                posiC=self.Vocabulario.index(Palabra)
#                for i in range(-1,len(resul)-1):
                i=0
                while(i<len(resul)):
                    if(resul[i]==Palabra):
                        self.VocR[posiC]+=1
                        resul.pop(i)
                        i-=1
                    i+=1

    def Eli(self):
        nuevo1=open("Eliminados.txt","w") # <5	#        nuevo1=open("./Eliminados.txt","w") # <5
        i=0
        while(i<len(self.Vocabulario)):
            if(self.filterm>self.VocR[i]):
                nuevo1.write(self.Vocabulario[i]+","+str(self.VocR[i])+"\n")
                self.Vocabulario.pop(i)
                self.VocR.pop(i)
                i-=1
            i+=1;
        nuevo1.close()

    
    def Ordena(self):
        nuevo1=open("Mejores.txt","w")	#        nuevo1=open("./Mejores.txt","w")
        nuevo2=open("Voc.txt","w")		#        nuevo2=open("./Voc.txt","w")
        tam=len(self.Vocabulario)-1
        for i in range(1,tam):
            for j in range(0,tam-1):
                if(self.VocR[i]>self.VocR[j]):
                    A=self.VocR[i]
                    A1=self.Vocabulario[i]
                    self.VocR[i]=self.VocR[j]
                    self.Vocabulario[i]=self.Vocabulario[j]
                    self.VocR[j]=A
                    self.Vocabulario[j]=A1
        
        if(self.filterM<len(self.Vocabulario)):
            tam=self.filterM

        for i in range(0,tam):
            nuevo1.write(self.Vocabulario[i] + "\n")	#             nuevo1.write(self.Vocabulario[i]+","+str(self.VocR[i])+"\n")

        for i in range(0,len(self.Vocabulario)):
            nuevo2.write(self.Vocabulario[i] + "\n")	 #            nuevo2.write(self.Vocabulario[i]+","+str(self.VocR[i])+"\n")

        nuevo1.write("Vocabulario total"+str(len(self.Vocabulario)))

        nuevo1.close()
        nuevo2.close()



        
  
A=Vocabulario("dedw","./txt_sentoken-limpio/pos","./txt_sentoken-limpio/neg")

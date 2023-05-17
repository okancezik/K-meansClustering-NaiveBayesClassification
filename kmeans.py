# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:34:30 2023

@author: okan
"""
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plot
from sklearn.metrics import homogeneity_score

class KMeans:
    
    def __init__(self,k = 3,maxiter = 100):
        self.k = k
        self.maxiter = maxiter
        self.niter = 0
        self.cache_y_predict = []
        
    def cluster(self,X):
        # random küme merkezleri seçildi
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False), :] 
        self.calculateDistances(X,self.centroids)

    
    def calculateDistances(self,X,centroids):
                
        print("CENTROIDS")
        print(self.centroids)
        print("\n")
        y_predict = []
        
        for x in X:
            min_distance = 10000
            near_centroid = self.centroids[0]
        
            for centroid in self.centroids:
  
                distance = np.sqrt((x[0] - centroid[0])**2 + (x[1]-centroid[1])**2)     #calculated distance
                if(min_distance > distance):
                    min_distance = distance
                    near_centroid = centroid
            
            for z in range(self.k):
                if(near_centroid[0] == self.centroids[z][0] and near_centroid[1] == self.centroids[z][1]):
                    n = z
            #print(x," ile ",near_centroid," arasındaki")
            #print("arasındaki en kısa uzaklık : ",min_distance)
            #print("kacıncı merkez : ",n)
            y_predict.append(n)
        self.updateCentroid(X, y_predict)

     
    def updateCentroid(self,X,y_predict):
        control1 = self.controlClustering(y_predict)
        control2 = self.controlİter()
        if(control1 == False and control2 == False):
            centroids = []                              
            for i in range(self.k):
                amount = 0
                totalpoints = 0
                for j in range(len(y_predict)):
                    if(i == y_predict[j]):
                        totalpoints += X[j] 
                        amount = amount + 1       
                centroids.append(totalpoints/amount)    # kümelenmiş örneklerin ortalaması alınır ve yeni merkez noktası olarak belirlenir
            self.maxiter = self.maxiter - 1             # 1 iterasyon tamamlanır, değeri azaltılır 
            self.niter += 1
            self.cache_y_predict = y_predict            # cache yenilendi
            self.centroids = np.array(centroids)        # array numpy arrayine dönüştürüldü
            self.calculateDistances(X, self.centroids)
        else:           
            print("\nKÜMELEME İŞLEMİ TAMAMLANDI, tamamlanan iterasyon sayısı ",self.niter)
            self.plotData(X, y_predict, self.centroids)

            
    # bir önceki iterasyon sonucunda kümeleme sonucu ile mevcut kümeleme sonucu karşılaştırılır
    def controlClustering(self,y_predict):
        if(len(self.cache_y_predict) > 0):
            control = True
            for i in range(len(y_predict)):
                if(y_predict[i] != self.cache_y_predict[i]):
                    control = False
            return control
        else:
            return False
        
    # iterasyon adeti kontrol edilir   
    def controlİter(self):
        if(self.maxiter > 0):
            return False
        else:
            return True

        
    # kümeleme işlemi tamamlandıktan sonra kümeler ve merkezleri görselleştirildi
    def plotData(self,X,y_predict,centroids):
        colors = ['r', 'g', 'b', 'c','m','y','r']
        for i in range(self.k):
            cluster_points = np.array([point for j, point in enumerate(X) if y_predict[j] == i])
            plot.scatter(cluster_points[:, 0], cluster_points[:, 1], s=5, color=colors[i])
            plot.scatter(centroids[i, 0], centroids[i, 1], s=100, color='k', marker='X')
        plot.title("After Clustering By Okan Çezik")
        plot.show()
        
    # bu fonksiyon kümeleme işleminin homojenlik skorunu ölçüyor.
    def homogeneityScore(self,y):
        homo_score = homogeneity_score(y, self.cache_y_predict)
        return homo_score
    
    # küme elemanlarının merkezlerine olan uzaklıkları toplanır, inertia hesaplanır
    def inertia(self,X):
        distance = 0
        for i in range(len(X)):
            centroid = self.centroids[self.cache_y_predict[i]]
            distance += np.sqrt(((X[i][0] - centroid[0])**2) + ((X[i][1] - centroid[1])**2))
        return distance
        
#PROGRAM BAŞLANGICI            
# 100 örnekli 2 özellikten oluşan dataset oluşturdum.
X , y = make_blobs(n_samples=500, n_features=2,         
                   centers=2, cluster_std=1.0,random_state=7)

# kümeleme işleminden önce dataset görselleştirildi       
plot.scatter(X[:, 0], X[:, 1], s=50)
plot.title('Dataset')
plot.xlabel('X')
plot.ylabel('Y')
plot.show()

# örnek olusturuldu
kmeans = KMeans(k=7)
kmeans.cluster(X)

# sistemin başarı ölçümünü homojenite skoru ile ölçtüm
result = kmeans.homogeneityScore(y)
print("Homojenlik skoru : ",result)

# inertia başarı metriği sonuç olarak yazdırılır
print("Inertia değeri : ",kmeans.inertia(X))




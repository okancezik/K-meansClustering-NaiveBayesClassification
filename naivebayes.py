# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:32:55 2023

@author: okan
"""

#import section
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

#veri setini kullanmak üzere dataset adlı değişkene aktardım.
dataset = pd.read_csv('Okan_Cezik_Dataset_Soru3.csv')

# veri seti içindeki NaN değerlere sahip satırları ayıkladım.
dataset = dataset.dropna()

# dataset içindeki özellikleri X ve sınıf değişkeni y olarak ayırdım
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]


# veri setini eğitim ve test veriseti olarak ayırdım
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25, random_state=0)


model = GaussianNB()                # sınıflandırma için model tanımladım
model.fit(XTrain, yTrain)           # modeli eğitim verileri ile eğittim     

yPredict = model.predict(XTest)      # eğittiğimiz modeli test için ayırdığımı veri seti ile test ediyoruz.

# karmaşıklık matrisini oluştur
confussionMatrix = confusion_matrix(yTest, yPredict)
print(confussionMatrix)

print("\n")
# accuracy değeri ölçüldü 
accuracy = accuracy_score(yTest, yPredict)
print("Accuracy score : ",accuracy)

# recall değeri hesaplandı
recall = recall_score(yTest, yPredict, average='macro')
print("Recall Score : ",recall)


# precision değeri hesaplandı
precision = precision_score(yTest, yPredict, average='macro')
print("Precision:", precision)

# f1-score değeri ölçüldü
f1 = f1_score(yTest, yPredict, average='macro')
print("f-measure : ",f1)



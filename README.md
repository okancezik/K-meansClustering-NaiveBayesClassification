<h3>Naive Bayes İle Sınıflandırma</h3>

<p>
 Sınıflandırma kavramı, basitçe bir veri kümesi üzerinde tanımlı olan çeşitli sınıflar arasında veriyi dağıtmaktır. 
 Bu yöntemde, önceden etiketlenmiş veri setleri kullanılarak model öğrenir ve daha sonra test veri setindeki verileri sınıflandırarak başarı ölçümü    
 değerlendirilir.
 
 Yapay Zeka sınıflandırma algoritmalarından biri olan Naive Bayes, Gözetimli Öğrenme (Supervised Learning) algoritmalarından biridir. 
 Yani sınıflandırılacak  olan verilerin hangi sınıflara ait olduğu bellidir.

 Naive Bayes algoritması koşullu olasılık hesaplamaya dayalı bir algoritmadır. Peki genel olarak çalışma mantığı nasıldır ?

 Algoritmanın genel mantığı, veri setindeki özelliklerin belirli bir sınıfa ait olma olasılıklarını
 hesaplayarak, bir girdinin hangi sınıfa ait olduğunu tahmin etmektir. Algoritma, bir girdi için tüm özelliklerin koşullu olasılıklarını hesaplar ve bu  
 olasılıkların çarpımını alarak girdinin her bir sınıfa ait olma olasılığını bulur. Son olarak, en yüksek olasılığa sahip olan sınıf tahmin edilir (MAP).
</p>

 <p>Dataset</p>
 
 ![image](https://github.com/okancezik/K-meansClustering-NaiveBayesClassification/assets/73329707/1c9079de-53c7-463e-b6d1-e74d77fa09a5)
 
 <p>Sınıflandırma Sonucu Karmaşıklık Matrisi</p>
 
 ![image](https://github.com/okancezik/K-meansClustering-NaiveBayesClassification/assets/73329707/4e3fe0cb-ae0b-402d-b66c-d599cb80485a)

 <p>Sınıflandırma Raporu</p>
 <ul>
  <li>Accuracy = (42 + 41 + 36) / (42+41+1+36) = 0.9916666667</li>
  <li>Recall, bir sınıfın gerçek pozitiflerinin ne kadarının doğru bir şekilde tespit edildiğini ölçer. 
   <ul>
    <li>Recall_0 = 42 / 42 = 1</li>
    <li>Recall_1 = 41 / (41+1) = 0.9761904762</li>
    <li>Recall_2 = 36 / 36 = 1</li>
   </ul>        
  </li> 
  <li>
   F-measure değeri için öncelikle precision değerleri gereklidir.
    <ul>
    <li>Precision_0 = 42 / (42+0+0) = 1</li>
    <li>Precision_1 = 41 / (41+0+0) = 1</li>
    <li>Precision_2 = 36 / (36+1+0) = 0.972972973</li>
   </ul>
   <p>F-measure = 2*(Recall*Precision)/(Recall+Precision)</p>
   <ul>
    <li>F-measure_0 = 2*(1*1)/(1+1) = 1</li>
    <li>F-measure_1 = 2*(0.9761904762*1)/(0.9761904762+1) = 0.9879518071</li>
    <li>F-measure_2 = 2*(1*0.972972973)/(1+0.972972973) = 0.9863013699</li>
   </ul> 
   <p>Ortalama F-measure değeri = 0.9914177257</p>
 </li>
 
 </ul>
 

<h3>KMeans İle Kümeleme</h3>

<p>
 Yapay zekada kümeleme, bir veri kümesindeki benzer özelliklere sahip verileri gruplandırmak için kullanılan bir makine öğrenmesi tekniğidir.

  Kümeleme, veri setindeki verileri belirli bir sayıda küme veya gruplara ayırmayı amaçlar. Bu kümeleme işlemi, benzerlik ölçüsüne göre yapılmaktadır.
  Veriler arasındaki benzerlik belirli bir mesafe vaya benzerlik ölçüsü kullanılarak hesaplanabilir.

  K-Means algoritması bölütleme mesafeye dayalı bir unsupervised learning(gözetimsiz öğrenme) kümeleme algoritmasıdır. 
  K-Means algoritmasında kümeleme sonucu küme içindeki veriler birbirine oldukça yakın; farklı küme içindeki noktaların birbirine uzak olması amaçlanır.
  Algoritma temel olarak 4 aşamadan oluşur :
    <ul>
     <li>Küme merkezleri belirlenir</li>
     <li>Merkez dışındaki örneklerin küme merkezlerine olan mesafeleri hesaplanır ve örnekler en kısa mesafe olan merkeze atanacak şekilde kümelenir.</li>
     <li>Yapılan kümelemeye göre yeni merkezler belirlenir</li>
     <li>Kararlı hale gelene kadar 2. ve 3. Adımlar tekrarlanır.</li>
    </ul>
</p>  

<p>Dataset</p>

![image](https://github.com/okancezik/K-meansClustering-NaiveBayesClassification/assets/73329707/51d66cd4-4df1-4319-a1b7-c7a2b57b0a8e)

<p>KMeans ile kümeleme sonucu</p>

![image](https://github.com/okancezik/K-meansClustering-NaiveBayesClassification/assets/73329707/3fa288f2-ca94-46de-9eff-660a76b660f7)

<h3>K-Means Algoritmasının Zayıf Yönleri Hakkında</h3>

<ul>
  <li>K-Means algoritması kümeleme yapmak için önceden belirlenmiş küme adet sayısına ihtiyaç duyar. 
    Ve küme sayısı sistemin başarısını doğrudan etkiler. Ancak , doğru küme sayısını en başta belirlemek mümkün olamayabilir. 
    Yanlış bir küme sayısı sistemin başarısını düşürebilir.
  </li>
  <li>
    K-Means algoritmasının ilk adımında veri seti içerisinden küme merkezleri seçilir. Başlangıçta küme merkezleri rastgele seçilmesi
    sistemin kümeleme başarısınıetkileyebilir
  </li>  
  <li>
    K-Means algoritması koşullu olasılık temeline dayandığı için sayısal hesaplamalara oldukça hassastır. Yanlış bir hesaplama veri setindeki örneğin yanlış bir kümeye atanmasına sebep olabilir.
  </li>
  <li>
    K-Means algoritması gürültülü verileri ve aykırı değerleri işleyemez
  </li>
  <li>
    Çok boyutlu verilerin kümelenmesi için K-Means algoritması uygulanabilir olsa da boyut sayısı arttığında veriler arasındaki uzaklıkların ölçülmesi ve benzerliklerin değerlendirilmesi zorlaşabilir 
    bu durum sistem performansını da etkileyebilir.
  </li>  
  
  
</ul>

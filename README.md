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

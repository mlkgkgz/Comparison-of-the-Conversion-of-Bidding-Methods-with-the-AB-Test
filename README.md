
Comparison of the Conversion of Bidding Methods with the AB Test

İş Problemi

Facebook kısa süre önce mevcut "maximumbidding" adı verilen
teklif verme türüne alternatif olarak yeni bir teklif türü olan
"average bidding"’i tanıttı.
Müşterilerimizden biri olan bombabomba.com, bu yeni özelliği test
etmeye karar verdi ve average bidding'inmaximumbidding'den
daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B
testi yapmak istiyor.
A/B testi 1 aydır devam ediyor ve bombabomba.com şimdi sizden
bu A/B testinin sonuçlarını analiz etmenizi bekliyor.
Bombabomba.com için nihai başarı ölçütü Purchase'dır. Bu
nedenle, istatistiksel testler için Purchase metriğine
odaklanılmalıdır.



Veri Seti Hikayesi

Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra
buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri
ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır. Kontrol grubuna Maximum Bidding, test grubuna Average
Bidding uygulanmıştır.




 impression: Reklam görüntüleme sayısı
 
 Click: Görüntülenen reklama tıklama sayısı
 
 Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
 
  Earning: Satın alınan ürünler sonrası elde edilen kazanç
  
  
  
  


Görev 1: Veriyi Hazırlama ve Analiz Etme


Adım 1: ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı
değişkenlere atayınız.



Adım 2: Kontrol ve test grubu verilerini analiz ediniz.

Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.



Görev 2: A/B Testinin Hipotezinin Tanımlanması


Adım 1: Hipotezi tanımlayınız.


H0 : M1 = M2

H1 : M1!= M2



Adım 2: Kontrol ve test grubu için purchase (kazanç) ortalamalarını analiz ediniz.



Görev 3: Hipotez Testinin Gerçekleştirilmesi


Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.


Bunlar Normallik Varsayımı ve Varyans Homojenliğidir. Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni
üzerinden ayrı ayrı test ediniz.


Normallik Varsayımı :
H0: Normal dağılım varsayımı sağlanmaktadır.

H1: Normal dağılım varsayımı sağlanmamaktadır.



p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ

Test sonucuna göre normallik varsayımı kontrol ve test grupları için sağlanıyor mu ? Elde edilen p-value değerlerini yorumlayınız.


Varyans Homojenliği :

H0: Varyanslar homojendir.

H1: Varyanslar homojen Değildir.

p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ


Kontrol ve test grubu için varyans homojenliğinin sağlanıp sağlanmadığını Purchase değişkeni üzerinden test ediniz.



Test sonucuna göre normallik varsayımı sağlanıyor mu? Elde edilen p-value değerlerini yorumlayınız.


Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz.



Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma ortalamaları arasında istatistiki
olarak anlamlı bir fark olup olmadığını yorumlayınız.






Görev 4: Sonuçların Analizi


Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.



Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.









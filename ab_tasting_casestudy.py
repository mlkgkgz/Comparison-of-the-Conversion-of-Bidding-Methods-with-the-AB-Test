#####################################################
# AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması
#####################################################

#####################################################
# İş Problemi
#####################################################

# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi veaveragebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchasemetriğine odaklanılmalıdır.




#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır.
#
#
# Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç



#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.

import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################

# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz.
# Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.

df_c = pd.read_excel("C:/Users/.../ab_testing.xlsx", sheet_name = "Control Group")
df_t = pd.read_excel("C:/Users/.../ab_testing.xlsx", sheet_name = "Test Group")


# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
df_c.head()
df_t.head()

df_c.describe().T
df_t.describe().T

df_c.isnull().sum()
df_t.isnull().sum()

df_c.info()
df_t.info()

df_c.shape # (40, 4)
df_t.shape # (40, 4)




# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

df_c["Bidding"] = "maximum_bidding" 


df_c.groupby("Bidding").agg({"Purchase": "mean"})




df_t["Bidding"] = "average_bidding"

df_t.groupby("Bidding").agg({"Purchase": "mean"})



#ORTALAMALAR BİRBİRİNE YAKIN. IST. OLARAK SINADIGIMIZDA MUHTEMELEN H0 ORT. ARASINDA FARK YOK DIYECEK. (550-582)


df = pd.concat([df_c, df_t], ignore_index = True)


#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# Adım 1: Hipotezi tanımlayınız.

# H0: M1 = M2 # Kontrol ve test grubu purchase(kazanç) ortalamaları arasında fark yok
# H1: M1 != M2 # Kontrol ve test grubu purchase(kazanç) ortalamaları arasında fark var




# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz



df.groupby("Bidding").agg({"Purchase":"mean"})






#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################


# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.
# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz



# VARSAYIM KONTROLU

# NORMALLIK
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

#1.grup
test_stat, pvalue = shapiro(df.loc[df["Bidding"] == "maximum_bidding", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 0.9773, p-value = 0.5891 > 0.05 H0 REDDEDİLEMEZ. # Normal dağılım varsayımı sağlanmaktadır.

# 2.grup
test_stat, pvalue = shapiro(df.loc[df["Bidding"] == "average_bidding", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Test Stat = 0.9589, p-value = 0.1541 > 0.05 H0 REDDEDİLEMEZ. # Normal dağılım varsayımı sağlanmaktadır.





# HOMOJENLIK

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df.loc[df["Bidding"] == "maximum_bidding", "Purchase"],
                           df.loc[df["Bidding"] == "average_bidding", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 2.6393, p-value = 0.1083 > 0.05 H0 REDDEDİLEMEZ.# H0: Varyanslar Homojendir





# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

#2 VARSAYIMDA SAGLANIYOR. bağımsız iki örneklem t testi (parametrik test)



# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.


test_stat, pvalue = ttest_ind(df.loc[df["Bidding"] == "maximum_bidding", "Purchase"],
                              df.loc[df["Bidding"] == "average_bidding", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# Test Stat = -0.9416, p-value = 0.3493 > 0.05 H0 REDDEDİLEMEZ.


# # H0: M1 = M2 # Kontrol ve test grubu purchase(kazanç) ortalamaları arasında fark yok



##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.
#
# Varsayımlar kontrol edildiğinde 2 VARSAYIMDA SAGLANIYORDU. (Normallik ve homojenlik) bu nedenle
# bağımsız iki örneklem t testi (parametrik test) üzerinden giderek seçim yaptım.



# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.

# H0: M1 = M2 # Kontrol ve test grubu purchase(kazanç) ortalamaları arasında fark yok

# kontrol grubu maxiumum_bidding teklif türü, test grubu da yeni teklif türü olan average_biddind ti.
# AB testine göre bu iki grup için
# (purchase) tıklanan reklamlar sonrası satın alınan ürünlerin sayılarına baktığımda
# iki grup arasındaki kazanç ortalamaları arasında herhangi bir istatistiksel farklılık göremedim.
# yani average bidding'in maximum bidding'den daha fazla dönüşüm getirmediğini tespit ettim.
# eski maximum bidding teklif türünden devam edilebilir. yada bu farkındalık bilinerek
# iki bidding türünün uygulanmasına devam edilebilir.
# Conversion rate, click through rate oranlarına bakılabilir.
# yada  kontrol ve test verisetinde gözlem sayıları düşüktü. daha fazla gözlem toplanarak
# tekrar AB testine sokulup ortalama kazanç değerine bakılabilir.




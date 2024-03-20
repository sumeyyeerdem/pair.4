#4Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

#soru4
import math

yaricap = float(input("Yariçapi giriniz: "))

alan= (math.pi*yaricap*yaricap)
cevre= (2*math.pi*yaricap)

totalText = f"Dairenin alani= {alan}"
print(totalText)

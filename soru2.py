#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = float(input("Lütfen maaşinizi giriniz: "))
zamOrani = float(input("Lütfen zam oraninizin yüzde kaç olduğunu giriniz: "))
zamliMaas = (maas*(100 + zamOrani)/100)

totalText = f"Zamli maaşiniz= {zamliMaas}"
print(totalText)
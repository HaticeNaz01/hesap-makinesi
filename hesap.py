İlksayi = int(input("ilk sayiyi giriniz "))
ikincisayi= int(input ("ikinci sayiyi giriniz "))

islem = input("""Yapmak İstediğiniz İşlemi Girin
 (toplama: +, çikarma: -, Çarpma: *, bölme: /) """)

if islem == "+" :
       print("sonuç : "+ str(İlksayi+ikincisayi))

elif islem == "-" :
       print("sonuç : "+ str(İlksayi-ikincisayi))

elif islem == "*" :
       print("sonuç : "+ str(İlksayi*ikincisayi))

elif islem == "/" :
       print("sonuç : "+ str(İlksayi/ikincisayi))


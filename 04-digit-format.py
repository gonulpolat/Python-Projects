number = 200 / 700

print("The result is {n}".format(n=number))      # 0.2857142857142857
print("The result is {n:1.2}".format(n=number))  # 0.29     -> virgülden sonra 2 basamak alır
print("The result is {n:2.2}".format(n=number))  # 0.29     -> sayının zaten totalde kapladığı alan 2'den fazla olduğu için değişiklik olmaz
print("The result is {n:3.2}".format(n=number))  # 0.29     -> sayının zaten totalde kapladığı alan 3'ten fazla olduğu için değişiklik olmaz
print("The result is {n:4.2}".format(n=number))  # 0.29     -> sayı toplam 4 karakterlik bir alan kaplar
print("The result is {n:5.2}".format(n=number))  #  0.29    -> sayı toplam 5 karakterlik bir alan kaplar
print("The result is {n:6.2}".format(n=number))  #   0.29   -> sayı toplam 6 karakterlik bir alan kaplar



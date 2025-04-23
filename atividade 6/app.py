temp_max = input("Digite a temperatura máxima do dia: ")
temp_min = input("Digite a temperatura mínima do dia: ")

try:
    temp_max = float(temp_max)
    temp_min = float(temp_min)
except:
  print("Erro você precisa digitar números válidos para as temperaturas.")

media = (temp_max + temp_min) / 2
print("A média das temperaturas é:", media)

variacao = temp_max - temp_min
print("A variação entre as temperaturas é:", variacao)
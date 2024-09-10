from Moto import Moto
from Veiculo import Veiculo


moto = Moto("Honda", "Falcon NX4", "abc", 2005, 400)

print(moto)

lancer = Veiculo("mitsubishi", "lancer", "abz", 2024)
print(lancer.__str__())
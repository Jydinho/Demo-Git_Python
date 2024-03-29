LIMITE_MAX = 3

stocks = []
stocks.append(3)
stocks.append(0)
stocks.append(1)

nom_boisson = []
nom_boisson.append("Eau")
nom_boisson.append("Soda")
nom_boisson.append("Orangeade")

"""
total_stock = 0
for el in stocks:
    total_stock += el
"""
    
total_stock = sum(stocks)    

choix = 0

while (total_stock > 0) and choix != 4:
    print("Choisissez une boisson : ")
    """
    for i in range(len(nom_boisson)):
        print(f"{i + 1}. {nom_boisson[i]}")   
    """
    for i in range(LIMITE_MAX):
        print(f"{i + 1}. {nom_boisson[i]}") 
    choix = int(input("FINIR : 4 \n"))
    if(choix != 4):
        if stocks[choix-1] > 0:
            print(f"Voici votre {nom_boisson[choix-1]} santé!")
            stocks[choix-1] = stocks[choix-1] - 1
        else:
            print(f"Plus de {nom_boisson[choix-1]}")
    total_stock = sum(stocks)

print("Merci d'utiliser distributeur 3000!")

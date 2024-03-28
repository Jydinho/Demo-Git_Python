stockSoda = 3
stockOrangeade = 5
stockEau = 0
encore = True
choix = 0

while (stockSoda + stockOrangeade + stockEau > 0) and choix != 4:
    choix = int(input("Veuillez sélectionner une boisson : \n" +
            "1. Soda \n" +
            "2. Orangeade \n" +
            "3. Eau \n"
            "4. Quitter\n"))
    match choix:
        case 1 :
            if stockSoda > 0 :
                print("A votre santé, voici votre Soda!")
                stockSoda -= 1
            else:
                print("Sold out! Faîtes un autre choix...")
        case 2 :
            if stockOrangeade > 0 :
                print("A votre santé, voici votre orangeade!")
                stockOrangeade -= 1
            else:
                print("Sold out! Faîtes un autre choix...")
        case 3 :
            if stockEau > 0 :
                print("A votre santé, voici votre eau!")
                stockEau -= 1
            else:
                print("Sold out! Faîtes un autre choix...")
        case 4 :
            print("Vous avez choissi de quitter")
        case _ : 
            print("Erreur, boisson non-disponible...")
print("Merci d'utiliser distributeur 3000!")


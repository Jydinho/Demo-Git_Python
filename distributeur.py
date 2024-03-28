stockSoda = 3
stockOrangeade = 5
stockEau = 0

choix = int(input("Veuillez sélectionner une boisson : \n" +
        "1. Soda \n" +
        "2. Orangeade \n" +
        "3. Eau \n"))
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
    case _ : 
        print("Erreur, boisson non-disponible...")


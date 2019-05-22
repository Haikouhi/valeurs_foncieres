

def recuperation_ligne1(fichier_text):
    with open(fichier_text, "r") as file:
        ligne1 = file.readline().strip()
    return ligne1


def creation_dictionnaire(text_colonnes):
    list_colonnes = text_colonnes.split("|")
    dictionnaire = {}
    for elem in list_colonnes:
        dictionnaire[elem] = []
    return dictionnaire


def remplissage_dictionnaire(dictionnaire, fichier_text):
    counter = 0
    with open(fichier_text, "r") as file:
        file.readline()
        lines = file.readlines(1000)
        for line in lines:
            counter += 1
            list_contenu_ligne = line.strip().split("|")
            i = 0
            for k, v in dictionnaire.items():
                v.append(list_contenu_ligne[i])
                i += 1
    return counter


dict = creation_dictionnaire(recuperation_ligne1("data_foncieres/valeursfoncieres-2018.txt"))

print(remplissage_dictionnaire(dict, "data_foncieres/valeursfoncieres-2018.txt"))
print(dict)


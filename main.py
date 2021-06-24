import os
     
dossier = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"
     
def remonter_dossier(dossier, iterations=1):
        i = 0
        while i < iterations:
            dossier = os.path.dirname(dossier)
            i += 1
     
        return dossier
     
print(remonter_dossier(dossier, 3))
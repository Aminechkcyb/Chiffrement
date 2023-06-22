from hashlib import sha256
entree = input("Entrez le nom du fichier à chiffrer : ")
sortie = input("Entrez le nom du fichier final : ")
key = input("Entrez la clé de chiffrement : ")
keys = sha256(key.encode('utf-8')).digest() 
with open(entree, 'rb') as f_entree:  
    with open(sortie, 'wb') as f_sortie:
        i = 0
        while f_entree.peek():# On lit le fichier octet par octet
            c = ord(f_entree.read(1)) # On récupère le caractère
            j = i % len(keys) # On récupère l'indice de la clé
            b = bytes([c^keys[j]]) # On chiffre le caractère
            f_sortie.write(b) # On écrit le caractère chiffré dans le fichier de sortie
            i = i + 1 # On incrémente i pour passer au caractère suivant




    



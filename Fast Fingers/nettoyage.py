def wash(word): # filtrage des mots à accent circonflexe
    s=''
    for letter in word:
        if letter == 'î' or letter == 'ô' or letter == 'û':
            s=''
            break
        else:
            s += letter
    return s

def counter_letter(word,letters):
    word = [letter for letter in word]
    for letter in word:
        if letter not in letters:
            letters.append(letter)


# parfois : open('text1.txt', 'r',encoding='utf-8')

words = []
# fonction de nettoyage d'un fichier selon fonction wash
with open('text1.txt', 'r') as file_read:
    lignes = file_read.readlines()
    for ligne in lignes:
        ligne = ligne.strip() # strip() pour enlever les éventuels caractères de nouvelle ligne
        #ligne = wash(ligne)
        if ligne not in words: # on supprime les lignes vides
            words.append(ligne)
    file_read.close()


    file_append = "text2" + ".txt"
    file_append = open(file_append, "a")
    for word in words:
        file_append.write(word)
        file_append.write('\n') 
    file_append.close()









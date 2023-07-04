def ispalindrome(sentence: str):
    '''Función que permite identificar si una palabra o frase es un palíndromo.
       Devuelve una frase que indica si el texto es un palíndromo o no'''
    
    import unidecode
    
    sentence = unidecode.unidecode(sentence)
    sentence = sentence.replace(" ", "")
    sentence_low = sentence.lower()
    
    if sentence_low[::-1] == sentence_low:
        print('Este texto es un palíndromo')
    else:
        print('Este texto NO es un palíndromo')
    

text = input("Ingresa una palabra o frase para saber si es un palíndromo: ")

ispalindrome(text)

# Se puede usa: Adán no cede con Eva y Yavé no cede con nada
# Otro: Allí si María avisa y así va a ir a mi silla
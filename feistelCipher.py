#Programme Python pour démontrer
# L'algorithme de géneration de clés chiffrement et déchiffrement de Feistel
 
import binascii
 
#Génération de clés à bits aléatoires
def rand_key(p):
     
    import random
    key1 = ""
    p = int(p)
    for i in range(p):
        temp = random.randint(0,1)
        temp = str(temp)
        key1 = key1 + temp
         
    return(key1)
  
# Fonction permettant de mettre en œuvre le bit exor
def exor(a,b):
     
    temp = ""
     
    for i in range(n):
         
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"
             
    return temp
 
# Définition de la fonction BinarytoDecimal()
def BinaryToDecimal(binary):
       
    # Utilisation de la fonction int pour convertir en
    # string 
    string = int(binary, 2)
       
    return string
 
# Chiffre de Feistel
PT = "Hello"
print("Plain Text is:", PT)
 
# Convertir le texte brut en
# ASCII
PT_Ascii = [ord(x) for x in PT]
 
# Conversion de l'ASCII en
# format binaire 8 bits
PT_Bin = [format(y,'08b') for y in PT_Ascii]
PT_Bin = "".join(PT_Bin)
 
n = int(len(PT_Bin)//2)
L1 = PT_Bin[0:n]
R1 = PT_Bin[n::]
m = len(R1)
  
# Générer la clé K2 pour le
# deuxième tour
K1= rand_key(m)
  
# Générer la clé K2 pour le
# deuxième tour
K2= rand_key(m)
  
# premier tour de Feistel
f1 = exor(R1,K1)
R2 = exor(f1,L1)
L2 = R1
  
# Deuxième tour de Feistel
f2 = exor(R2,K2)
R3 = exor(f2,L2)
L3 = R2
  
# Texte chiffré
bin_data = L3 + R3
str_data =' '
 
for i in range(0, len(bin_data), 7):
       
    # découpage des données bin_data à partir de la plage d'index [0, 6].
    # et le stocker dans temp_data
    temp_data = bin_data[i:i + 7]
        
    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal(temp_data)
        
    # Decoding the decimal value returned by 
    # BinarytoDecimal() function, utilisé chr() 
    # qui retourne la chaîne de caractères correspondant 
    # correspondant à une valeur ASCII donnée, et la stocke 
    # dans str_data
    str_data = str_data + chr(decimal_data)
     
print("Texte chiffré:", str_data)
 
# Décryptage
L4 = L3
R4 = R3
  
f3 = exor(L4,K2)
L5 = exor(R4,f3)
R5 = L4
  
f4 = exor(L5,K1)
L6 = exor(R5,f4)
R6 = L5
PT1 = L6+R6
  
 
PT1 = int(PT1, 2)
RPT = binascii.unhexlify( '%x'% PT1)
print("Le texte brut récupéré est: ", RPT)
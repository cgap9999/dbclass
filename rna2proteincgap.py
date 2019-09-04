def rna2protein(i,  j, string, protein):
#------------- A
    if string[i] == "a":
#--------------- AGX
        if string[i+1] == "g":
            if string[i+2] == "a" or string[i+2] == "g":
                protein[j]= "R"
            else:
                protein[j]= "S"
#---------------   AAX             
        elif string[i+1] == "a":
            if string[i+2] == "a" or string[i+2] == "g":
                protein[j]= "K"
            else:
                protein[j]= "N"
#-------------   ACX
        elif string[i+1]== "c":
            protein[j]= "T"
#------------- AUX
        elif string[i+1] == "u":
            if string[i+2] == "g":
                protein[j]= "M"
            else:
                protein[j]= "I"
                
#-------------- C
    elif string[i] == "c":
#------------- CGX
        if string[i+1] == "g":
            protein[j]= "R"
#------------ CAX
        elif string[i+1] == "a":
            if string[i+2] == "g" or string[i+2] == "a":
                protein[j]= "Q"
            else:
                protein[j]= "H"
#------------- CCX
        elif string[i+1] == "c":
            protein[j]= "P"
#------------ CUX
        elif string[i+1]== "u":
            protein[j]= "L"

#------------ U
    elif string[i]== "u":
#----------- UGX
        if string[i+1]== "g":
            if string[i+2]== "g":
                protein[j]= "W"
            elif string[i+2]== "a":
                print ("UGA is a stop codon")
                protein[j]= "x"
                return
            else:
                protein[j]= "C"
#----------- UAX
        elif string[i+1]== "a":
            if string[i+2]== "a" or string[i+2]== "g":
                print ("UAG/UAA are stop codons")
                protein[j]= "x"
                return
            else:
                protein[j]= "Y"
#------------ UCX
        elif string[i+1]== "c":
            protein[j]= "S"
#----------- UUX
        elif string[i+1] == "u":
            if string[i+2]== "a" or string[i+2]== "g":
                protein[j]= "L"
            else:
                protein[j]= "F"
                
#---------- G
    elif string[i]== "g":
#--------- GGX
        if string[i+1]== "g":
            protein[j]= "G"
#--------- GAX
        elif string[i+1]== "a":
            if string[i+2]== "a" or string[i+2]== "g":
                protein[j]= "E"
            else:
                protein[j]= "D"
#--------- GCX
        elif string[i+1]== "c":
            protein[j]= "A"
#-------- GUX
        elif string[i+1]== "u":
            protein[j]= "V"

import argparse  
parser= argparse.ArgumentParser()
parser.add_argument('text', action="store")
rna= parser.parse_args()
rna= repr(rna.text)
rna= rna.strip("'")
rna= rna.lower()
protein= [0]*(int(len(rna)/3))
j= 0
for i in range(len(rna)):
    if i%3 == 0:
        if j == len(protein):
            break
        rna2protein(i, j, rna, protein)
        j+= 1

print (''.join(protein))

        


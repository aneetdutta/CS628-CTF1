import random
key = [random.randint(0,255) for i in range(8)]
print(key)



plaintext="cs628a{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}"

plaintext = list(plaintext)
plaintext = [ord(i) for i in plaintext]

print(plaintext)
text_len = len(plaintext)
key_len = len(key)
repetitions = int(text_len/key_len)
key = key * repetitions

print(key)

zip1=zip(plaintext, key)
print(zip1)


ciphertext = [i^j for i,j in zip(plaintext, key)]

strr = ""
for i in ciphertext:
    strr += "%02x" % i

print strr
print(len(strr))


k='87fb0742f17436f2d2b95415fe2675a2dce90914aa2575f381ba0611a87678f4d2be5311fe732fbd'


key_p=[]

flag=""
for i in range(0,len(k),2):

    if(i<=12 or i==len(k)-2):
       
    	a=plaintext[int( i/2)]
    	x= int(str(k[i])+str(k[i+1]) ,16 )  
 	
        xi=a^x

        print(chr(a)+":"+str(a)+  ":" +str(xi) + ":" + str(x)+ ":" + "%02x"%x)
        

        key_p.append(xi)

print(key_p)
    



print('decoding')

for i in range(0,len(k),2):
    x= int(str(k[i])+str(k[i+1]) ,16 )  
    xi=x^      key_p[   (i/2)% len(key_p)    ]
   


    print(chr(xi))

    flag+= chr(xi)



print("FLAG : "+ flag)




#c=ord(k[i:i+1])


#print(len(k))

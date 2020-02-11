while True:
    ch = int(input("Press 1 for encrypt Or 2 for decrypt:-\n")) 
    if ch == 1:
        text = input("Text:").lower()       

        sliced=[]
        for tx in range(len(text)//2):
            if text[tx*3:tx*3+3] != '': 
                sliced.append(text[tx*3:tx*3+3])

        listed=[]
        for sl in sliced:
            sl = list(sl)
            listed.append(sl)


        encrypt=[]
        for li in listed:
            for i, x in enumerate(li):  
                if i==0:                
                    x = ord(x)+3 
                    if x > ord('z'):
                        x -=26
                        encrypt.append(chr(x))
                    else:
                        encrypt.append(chr(x))
                elif i==1:
                    x = ord(x)+5 
                    if x > ord('z'):
                        x -=26
                        encrypt.append(chr(x))
                    else:
                        encrypt.append(chr(x))
                elif i==2:
                    x = ord(x)+7 
                    if x > ord('z'):
                        x -=26
                        encrypt.append(chr(x))
                    else:
                        encrypt.append(chr(x))
        print("!!! Encrypted !!!\a")
        print("==========================================")
        print("".join(encrypt))
        print("==========================================\n")

    elif ch == 2:
        text = input("Text:").lower()       

        sliced=[]
        for tx in range(len(text)//2):
            if text[tx*3:tx*3+3] != '': 
                sliced.append(text[tx*3:tx*3+3])

        listed=[]
        for sl in sliced:
            sl = list(sl)
            listed.append(sl)


        decrypt=[]
        for li in listed:
            for i, x in enumerate(li):  
                if i==0:                
                    x = ord(x)-3 
                    if x < ord('a'):
                        x +=26
                        decrypt.append(chr(x))
                    else:
                        decrypt.append(chr(x))
                elif i==1:
                    x = ord(x)-5
                    if x < ord('a'):
                        x +=26
                        decrypt.append(chr(x))
                    else:
                        decrypt.append(chr(x))
                elif i==2:
                    x = ord(x)-7 
                    if x < ord('a'):
                        x +=26
                        decrypt.append(chr(x))
                    else:
                        decrypt.append(chr(x))
        print("!!! Decrypted !!!\a")
        print("==========================================")
        print("".join(decrypt))
        print("==========================================\n")
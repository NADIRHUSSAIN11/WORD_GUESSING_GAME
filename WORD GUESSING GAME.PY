print("********************************************")
print("***********THE WORD GUESSING GAME***********")
print("********************************************\n\n")

print("NOTE\n")
note=("HELLO WE ARE GOING TO PLAY A GAME IN WHICH YOU HAVE TO THINK A WORD IN YOUR MIND AND I WILL\n TELL YOU WHAT IS THAT WORD AND THE WORD SHOULD BE CONSISTS OF 3 LETTERS TO 5 LETTERS\n")
print(note)
inp=int(input("TELL ME THE LENGTH OF THAT WORD YOU THINK (3,4 OR 5):")) #MAIN USER INPUT 
if inp==3:#HERE THIS IF IS FOR INPUT 3
    col=[ '1','2','3','4']
    alpha1=["A","B","C","D"]
    alpha2=['E','F','G','H']
    alpha3=['I','J','K','L']
    alpha4=['M','N','O','P']
    alpha5=['Q','R','S','T']
    alpha6=['U','V','W','X']
    alpha7=['Y','Z',' ',' ']
    print(col)
    print(alpha1)
    print(alpha2)
    print(alpha3)
    print(alpha4)
    print(alpha5)
    print(alpha6)
    print(alpha7)
    a=int(input('TELL ME THE 1ST LETTER OF WORD IS IN WHICH COLUMN:'))
    b=int(input('TELL ME THE 2ND LETTER OF WORD IS IN WHICH COLUMN:'))
    c=int(input('TELL ME THE 3RD LETTER OF WORD IS IN WHICH COLUMN:'))
    T=[] #THIS IS A EMPTY LIST
    if a==1:
        T.append(['A','E','I','M','Q','U','Y'])
    if a==2:
        T.append(['B','F','J','N','R','V','Z'])  
    if a==3:
        T.append(['C','G','K','O','S','W',' '])
    if a==4:
        T.append(['D','H','L','P','T','X',' '])
    if b==1:
        T.append(['A','E','I','M','Q','U','Y']) 
    if b==2:
        T.append(['B','F','J','N','R','V','Z'])   
    if b==3:
        T.append(['C','G','K','O','S','W',' '])   
    if b==4:
        T.append(['D','H','L','P','T','X',' '])
    if c==1:
        T.append(['A','E','I','M','Q','U','Y'])   
    if c==2:
        T.append(['B','F','J','N','R','V','Z'])    
    if c==3:
        T.append(['C','G','K','O','S','W',' ']) 
    if c==4:
        T.append(['D','H','L','P','T','X',' '])
    else:
        print("GIVEN INPUT IS NOT CORRECT")
    for x in T:
        print(x)
    K=[] #THIS IS A EMPTY LIST
    d=int(input("NOW AGAIN TELL ME THE 1ST LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[0][d-1])
    e=int(input("NOW AGAIN TELL ME THE 2ND LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[1][e-1])
    f=int(input("NOW AGAIN TELL ME THE 3RD LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[2][f-1])
    for w in K:
        print(w,end="")
    print(' IS A WORD THAT YOU THINK IN YOUR MIND')
    print('*******THANK YOU FOR PLAYING THIS GAME*********')
if inp==4:#HERE THIS IF IS FOR INPUT 4
    col=[ '1','2','3','4']
    alpha1=["A","B","C","D"]
    alpha2=['E','F','G','H']
    alpha3=['I','J','K','L']
    alpha4=['M','N','O','P']
    alpha5=['Q','R','S','T']
    alpha6=['U','V','W','X']
    alpha7=['Y','Z',' ',' ']
    print(col)
    print(alpha1)
    print(alpha2)
    print(alpha3)
    print(alpha4)
    print(alpha5)
    print(alpha6)
    print(alpha7)
    a=int(input('TELL ME THE 1ST LETTER OF WORD IS IN WHICH COLUMN:'))
    b=int(input('TELL ME THE 2ND LETTER OF WORD IS IN WHICH COLUMN:'))
    c=int(input('TELL ME THE 3RD LETTER OF WORD IS IN WHICH COLUMN:'))
    i4=int(input('TELL ME THE 4TH LETTER OF WORD IS IN WHICH COLUMN:'))
    T=[] #THIS IS A EMPTY LIST
    if a==1:
        T.append(['A','E','I','M','Q','U','Y'])
    if a==2:
        T.append(['B','F','J','N','R','V','Z'])  
    if a==3:
        T.append(['C','G','K','O','S','W',' '])
    if a==4:
        T.append(['D','H','L','P','T','X',' '])
    if b==1:
        T.append(['A','E','I','M','Q','U','Y']) 
    if b==2:
        T.append(['B','F','J','N','R','V','Z'])   
    if b==3:
        T.append(['C','G','K','O','S','W',' '])   
    if b==4:
        T.append(['D','H','L','P','T','X',' '])
    if c==1:
        T.append(['A','E','I','M','Q','U','Y'])   
    if c==2:
        T.append(['B','F','J','N','R','V','Z'])    
    if c==3:
        T.append(['C','G','K','O','S','W',' ']) 
    if c==4:
        T.append(['D','H','L','P','T','X',' '])
    if i4==1:
        T.append(['A','E','I','M','Q','U','Y'])   
    if i4==2:
        T.append(['B','F','J','N','R','V','Z'])    
    if i4==3:
        T.append(['C','G','K','O','S','W',' ']) 
    if i4==4:
        T.append(['D','H','L','P','T','X',' '])
    else:
        print("GIVEN INPUT IS NOT CORRECT")
    for x in T:
        print(x)
    K=[] #THIS IS A EMPTY LIST
    d=int(input("NOW AGAIN TELL ME THE 1ST LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[0][d-1])
    e=int(input("NOW AGAIN TELL ME THE 2ND LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[1][e-1])
    f=int(input("NOW AGAIN TELL ME THE 3RD LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[2][f-1])
    g=int(input("NOW AGAIN TELL ME THE 4TH LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[3][g-1])
    for w in K:
        print(w,end="")
    print(' IS A WORD THAT YOU THINK IN YOUR MIND')
    print('*******THANK YOU FOR PLAYING THIS GAME*********')
if inp==5: #HERE THIS IF IS FOR INPUT 5
    col=[ '1','2','3','4']
    alpha1=["A","B","C","D"]
    alpha2=['E','F','G','H']
    alpha3=['I','J','K','L']
    alpha4=['M','N','O','P']
    alpha5=['Q','R','S','T']
    alpha6=['U','V','W','X']
    alpha7=['Y','Z',' ',' ']
    print(col)
    print(alpha1)
    print(alpha2)
    print(alpha3)
    print(alpha4)
    print(alpha5)
    print(alpha6)
    print(alpha7)
    a=int(input('TELL ME THE 1ST LETTER OF WORD IS IN WHICH COLUMN:'))
    b=int(input('TELL ME THE 2ND LETTER OF WORD IS IN WHICH COLUMN:'))
    c=int(input('TELL ME THE 3RD LETTER OF WORD IS IN WHICH COLUMN:'))
    i4=int(input('TELL ME THE 4TH LETTER OF WORD IS IN WHICH COLUMN:'))
    i5=int(input('TELL ME THE 5TH LETTER OF WORD IS IN WHICH COLUMN:'))
    T=[] #THIS IS A EMPTY LIST
    if a==1:
        T.append(['A','E','I','M','Q','U','Y'])
    if a==2:
        T.append(['B','F','J','N','R','V','Z'])  
    if a==3:
        T.append(['C','G','K','O','S','W',' '])
    if a==4:
        T.append(['D','H','L','P','T','X',' '])
    if b==1:
        T.append(['A','E','I','M','Q','U','Y']) 
    if b==2:
        T.append(['B','F','J','N','R','V','Z'])   
    if b==3:
        T.append(['C','G','K','O','S','W',' '])   
    if b==4:
        T.append(['D','H','L','P','T','X',' '])
    if c==1:
        T.append(['A','E','I','M','Q','U','Y'])   
    if c==2:
        T.append(['B','F','J','N','R','V','Z'])    
    if c==3:
        T.append(['C','G','K','O','S','W',' ']) 
    if c==4:
        T.append(['D','H','L','P','T','X',' '])
    if i4==1:
        T.append(['A','E','I','M','Q','U','Y'])   
    if i4==2:
        T.append(['B','F','J','N','R','V','Z'])    
    if i4==3:
        T.append(['C','G','K','O','S','W',' ']) 
    if i4==4:
        T.append(['D','H','L','P','T','X',' '])
    if i5==1:
        T.append(['A','E','I','M','Q','U','Y'])   
    if i5==2:
        T.append(['B','F','J','N','R','V','Z'])    
    if i5==3:
        T.append(['C','G','K','O','S','W',' ']) 
    if i5==4:
        T.append(['D','H','L','P','T','X',' '])
    else:
        print("GIVEN INPUT IS NOT CORRECT")
    for x in T:
        print(x)
    K=[] #THIS IS A EMPTY LIST
    d=int(input("NOW AGAIN TELL ME THE 1ST LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[0][d-1])
    e=int(input("NOW AGAIN TELL ME THE 2ND LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[1][e-1])
    f=int(input("NOW AGAIN TELL ME THE 3RD LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[2][f-1])
    g=int(input("NOW AGAIN TELL ME THE 4TH LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[3][g-1])
    h=int(input("NOW AGAIN TELL ME THE 5TH LETTER OF WORD IS IN WHICH COLUMN:"))
    K.append(T[4][h-1])
    print("\n ")
    for w in K:
        print(w,end="")
    print(' IS A WORD THAT YOU THINK IN YOUR MIND\n')
    print('*******THANK YOU FOR PLAYING THIS GAME*********')
if inp>5:
    print("YOUR GIVEN INPUT IS NOT CORRECT")
if inp<3:
    print("YOUR GIVEN INPUT IS NOT CORRECT")
input("PRESS ENTER TO EXIT")


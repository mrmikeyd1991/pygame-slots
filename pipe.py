from datetime import date

PipeLaid = 0
Fittinglaid = 0
Feetlaid = 0
CustomCutTogether = 0
CustomCuts = 0

print(date.today())
file = open('notes.txt', "a+")
file.write('\n\n')
file.write(str(date.today()))
file.write('\n')
print('''
---------------------------------
mikeys pipe man skrypt
---------------------------------
''')

while True:
    print('''
    1) add 20Ft                <-- to add            
    2) add 14Ft                <-- to add             
    3) add CUSTOM CUT          <-- to add            
    4) add Fitting             <-- to add              
    5) - 20Ft                  <-- to add         
    6) - 14Ft                  <-- to add         
    7) - CUSTOM CUT            <-- to add        
    8) ADD NOTE                <-- to add        
    9) Figure pipe grade       <-- to add        
    10) show 1ft in tenths     <-- to add        
    
    Pipe Laid:  ''', PipeLaid,'''
    Fittings laid:  ''', Fittinglaid, '''
    Feet Laid:  ''', Feetlaid,'''
    Custom Cuts Together:  ''', CustomCutTogether,'''
    Custom Cuts:  ''', CustomCuts)
 
    Mq = input(">  ")

    if Mq == 'q':
        break

    if Mq == '1':
        PipeLaid += 1
        Feetlaid += 20

    if Mq == '2':
        PipeLaid += 1
        Feetlaid += 14

    if Mq == '3':
        Cut = input('\n\nEnter Custom Cut length:  ')
        CustomCuts += 1
        CustomCutTogether += Cut
        Feetlaid += Cut

    if Mq == '4':
        Fittinglaid += 1
        Feetlaid += 1

    if Mq == '5':
        Feetlaid -= 20
        PipeLaid -= 1

    if Mq == '6':
        Feetlaid -= 14
        PipeLaid -= 1

    if Mq == '7':
        Custom = input('enter custom cut to -  :  ')
        Feetlaid -= Custom

    if Mq == '8':
        Note = input('Enter Note to add/n put break symbol for new line:   ')
        file.write(Note)
        file.write('\n')

    if Mq == '9':
        manhole = input('enter manhole shot:  ')
        distance = input('enter distance:  ')
        
        of15 = input('of 15ft::   ')
        of20 = input('of20 ft:    ')
    if Mq == 'q':
        break
    if Mq == 'q':
        break
    if Mq == 'q':
        break

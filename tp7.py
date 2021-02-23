test=0
mot_select=''

while test < 2:
    mot=input('Tapez mot de passe: ')

    if len(mot) > 6 or len(mot) < 12:
        maj=[c for c in mot if c.isupper()]
        numb=[c for c in mot if c.isdigit()]

        if len(maj) > 0 and len(numb) > 0:
            mot_select=mot
            break

    print('veuillez vérifier votre mot de passe')
    test+=1

if len(mot_select) > 0:
    print('\n[Mot retenu] > %s'%mot_select)
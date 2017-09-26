def new_password(new):
    for i in new:
        if i in '0123456789':
            if new != oldpas and len(new) > 5:
                return True
            else:
                return False
        else:
            print('Uw nieuwe ww bevat geen cijfer.')
            break


oldpas = input('Old password: ')
newpas = input('New password: ')

confrim = new_password(newpas)
print(confrim)

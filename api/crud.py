'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)

UPDATE AND DELETE NEED A WHERE CLAUSE *
'''
from database import con
import os

menu_status = True

def main_menu():
    opt_status = True
    os.system('clear')
    print("::: MAIN MENU :::")
    print("[1]. Create user")
    print("[2]. List users")
    print("[3]. Salir")
    
    while opt_status:
        opt = int(input('Press any option: '))
        if opt < 1 or opt > 3:
            print("Error: Invalid option. Try 1 to 3")
            #opt = int(input('Press any option: '))
        else:
            opt_status = False #break
            return opt

def create_user():
    os.system('clear')
    
    uname = input('Username: ')
    uemail = input('E-mail_: ')
    upasswd = input('Password: ')
    
    new_user_query = f'''
        INSERT INTO users (username, email, password, role)
            VALUES ('{uname}','{uemail}','{upasswd}', '1')
    '''
    con.execute(new_user_query)
    con.commit()

    print('User created succesfully.')
    os.system('pause')    
    con.close()
    
while menu_status:
    op = main_menu()
    
    if op == 1:
        create_user()
    elif op == 2:
        os.system('clear')
        print("Option under construction :::")
        os.system('pause')
    else:
        print("Exit ...")
        os.system('pause')
        menu_status = False
        #break

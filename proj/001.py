import main
from person import Person
import inquirer
from time import sleep
list = []
list_options = ['Add a new person','Show database', 'Edit database', 'Quit']

while True:
    main.inishow()
    questions = [
        inquirer.List('opt',
                message='What do you want me to do?',
                choices=list_options,
                ),
    ]
    answ = inquirer.prompt(questions)
    sel = answ['opt']
    if sel == list_options[0]:
        main.add(list)
    elif sel == list_options[1]:
        if list == []:
            main.datashow()
            print("\033[1;31mERROR! There's no database to be shown\033[m")
            print('\033[1;31mGoing back to the MENU!\033[m')
        else:  
            main.datashow()
            main.show(list)
    elif sel == list_options[2]:
        if list == []:
            main.editshow()
            print("\033[1;31mERROR! There's no database to be edited\033[m")
            print('\033[1;31mGoing back to the MENU!\033[m')
        else:
            main.editshow()
            main.edit(list)
            
    elif sel == list_options[3]:
        main.quitshow()
        print('\033[1;31mQUITTING...\033[m')
        break  
    sleep(1) 






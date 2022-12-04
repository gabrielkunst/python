from person import Person
import inquirer

def line():
    print('\033[1;32m-\033[m'*40)

def inishow():
    print()
    line()
    print('\033[1;32m{:^40}\033[m'.format('MENU'))
    line()
    print()

def datashow():
    line()
    print('\033[1;32m{:^40}\033[m' .format('DATABASE'))
    line()

def editshow():
    line()
    print('\033[1;32m{:^40}\033[m' .format('EDIT'))
    line()

def quitshow():
    line()
    print('\033[1;32m{:^40}\033[m' .format('QUIT'))
    line()

def intvalidador(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[1;31mERROR! Invalid input!\033[m') 
            continue
        else:
            return n

def add(list):
    name = str(input('\033[1;32mName: \033[m')).strip().title()
    age = intvalidador('\033[1;32mAge: \033[m')
    prof = str(input('\033[1;32mLiving: \033[m')).strip().title()
    person = Person(name, age, prof)
    list.append(person)
    print()

def show(list):
    print('{:<20}{:<15}{:<5}' .format('NAME','PROF','AGE'))
    for person in list:
        print(person.toString())    

def edit(list):
    options = []
    for person in list:
        options.append(person.toString())
    questions = [
            inquirer.List('opt',
                    message='Select user: ',
                    choices=options,
                    ),
    ]
    answ = inquirer.prompt(questions)
    sel = answ['opt']
    posedit(list, options.index(sel))

def posedit(list, index):
    print(f'Editing {list[index].name}')
    opts = ['Name', 'Age', 'Prof']
    questions = [
            inquirer.List('opt',
                message='What do you wannna rename?',
                choices=opts,
                ),
    ]
    answ = inquirer.prompt(questions)
    sel = answ['opt']
    if sel == 'Name':
        editname(list,index)


def editname(list, index):
    new = str(input('New name: '))
    list[index].name = new
    

#DEVE SER FEITO UMA CONDIÇÃO EM QUE SE SEL = NAME, TROCA NAME, ETC...

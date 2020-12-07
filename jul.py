while True:
    print('[1] Do stuff')
    print('[2] Kapitel 5')
    print('[7] Stop doing stuff')
    choice = int(input('Choice : '))


    if choice == 7:
        confirm = input('Do you wish to exit [Y/N]')
        if confirm.lower() == 'y':
            break

        elif choice == 1:
            text = input("Write something")
            print(f'Text: {text[3]}, {text.upper()}')

            if text[3] == '':
                print('Du skrev ett mellanslag')


        elif choice == 2:
            print('\t[1] Uppgift 5.1\n\t[2] Uppgift 5.2\n')
            choice = int(input('\Make a new choice: '))
import functions as f

defaults = dict(path = 'C:\\0Utvikling\\Installasjon\\bmc-tools-master\\output\\', extension = 'bmp')

if __name__ == '__main__':
    f.welcome_screen()
    main_menu = f.menu()
    keep_running = True
    while keep_running:
        command = input("> ").split(' ',maxsplit = 2)
        if command[0] in main_menu:
            if main_menu[command[0]] == 1:  # help menu
                f.help_screen()
            elif main_menu[command[0]] == 2:  # load menu
                if len(command) > 1:
                    print('Loading ' + command[1])
                    f.find_images(path=command[1], file_extension=command[2])
                else:
                    print(f.message('invalid_path'))

            elif main_menu[command[0]] == 3:  # quick load
                list_images = f.find_images(defaults['path'],defaults['extension'])
                print(list_images)
                f.create_new_image(list_images)

            elif main_menu[command[0]] == 99: # quit the program
                print(f.message('quit'))
                keep_running = False
        else:
            print("cannot find item")
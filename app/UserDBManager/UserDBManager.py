from os import system, name
from sqlite3 import Connection
from typing import Optional
from enums.MenuOptionsEnum import MenuOptionsEnum
from enums.TablesEnum import TablesEnum
from dbManager.bo import get_athletes_data, get_athlete_exercises

class UserDBManager:
    CONTINUE_MSG = 'Press something to continue ...'

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def run(self) -> None:
        """ Run main user manager loop """

        selectedOption: Optional[int] = None
        while selectedOption != MenuOptionsEnum.EXIT.value:
            self.clear_terminal()
            self.show_menu()

            try:
                selectedOption = int(input('Select option: '))
                self.clear_terminal()

                if selectedOption == MenuOptionsEnum.SHOW_ATHLETES.value:
                    print(get_athletes_data(self.conn).to_string(index=False))
                elif selectedOption == MenuOptionsEnum.SHOW_ATHLETE_EXERCISES.value:
                    firstname = input('Enter firstname: ')
                    lastname = input('Enter lastname: ')
                    print(get_athlete_exercises(self.conn, firstname, lastname).to_string(index=False))
                elif selectedOption == MenuOptionsEnum.EXIT.value:
                    print('Exit program')

            except ValueError:
                print('Pls type number to select option !')
            finally:
                input(self.CONTINUE_MSG)


    def clear_terminal(self) -> None:
        """ Clear terminal with specific command based on OS type """

        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def show_menu(self) -> None:
        """ Print user menu """

        print(f'{MenuOptionsEnum.SHOW_ATHLETES.value}) Show athletes')
        print(f'{MenuOptionsEnum.SHOW_ATHLETE_EXERCISES.value}) Show athlete exercises')
        print(f'{MenuOptionsEnum.EXIT.value}) Exit program')

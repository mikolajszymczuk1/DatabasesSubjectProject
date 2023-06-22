from os import system, name
from sqlite3 import Connection
from typing import Optional
from enums.MenuOptionsEnum import MenuOptionsEnum
from dbManager.bo import (
    get_athletes_data,
    get_athlete_exercises,
    create_exercise_for_athlete,
    create_athlete
)

class UserDBManager:
    CONTINUE_MSG = 'Press something to continue ...'

    def __init__(self, conn: Connection) -> None:
        """
        Initialize UserDBManager instance.

        :param conn: The database connection.
        :type conn: Connection
        """

        self.conn: Connection = conn

    def run(self) -> None:
        """ Run main user manager loop """

        selected_option: Optional[int] = None
        while selected_option != MenuOptionsEnum.EXIT.value:
            self.clear_terminal()
            self.show_menu()

            try:
                selected_option = int(input('Select option: '))
                self.clear_terminal()

                if selected_option == MenuOptionsEnum.SHOW_ATHLETES.value:
                    self.show_athletes_operation()
                elif selected_option == MenuOptionsEnum.SHOW_ATHLETE_EXERCISES.value:
                    self.show_athletes_exercises_operation()
                elif selected_option == MenuOptionsEnum.ADD_ATHLETE.value:
                    self.add_athlete_operation()
                elif selected_option == MenuOptionsEnum.ADD_EXERCISE.value:
                    self.add_exercise_operation()
                elif selected_option == MenuOptionsEnum.EXIT.value:
                    print('Exit program')

            except ValueError:
                print('Pls type number to select option !')
            finally:
                input(self.CONTINUE_MSG)

    def clear_terminal(self) -> None:
        """ Clear terminal with specific command based on OS type. """

        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def show_menu(self) -> None:
        """ Print user menu """

        print(f'{MenuOptionsEnum.SHOW_ATHLETES.value}) Show athletes')
        print(f'{MenuOptionsEnum.SHOW_ATHLETE_EXERCISES.value}) Show athlete exercises')
        print(f'{MenuOptionsEnum.ADD_ATHLETE.value}) Add new athlete')
        print(f'{MenuOptionsEnum.ADD_EXERCISE.value}) Add new exercise')
        print(f'{MenuOptionsEnum.EXIT.value}) Exit program')

    def show_athletes_operation(self) -> None:
        """ Show athletes"""

        print(get_athletes_data(self.conn).to_string(index=False))

    def show_athletes_exercises_operation(self) -> None:
        """ Show athletes exercise. """

        firstname = input('Enter firstname: ')
        lastname = input('Enter lastname: ')
        print(get_athlete_exercises(self.conn, firstname, lastname).to_string(index=False))

    def add_athlete_operation(self) -> None:
        """ Add new athlete. """

        firstname: str = input('Enter firstname: ')
        lastname: str = input('Enter lastname: ')
        age: int = int(input('Enter age: '))
        weight: int = int(input('Enter weight: '))
        gender: str = input('Enter gender: ')
        experience_id: int = int(input('Enter experience id: '))
        create_athlete(self.conn, firstname, lastname, age, weight, gender, experience_id)

    def add_exercise_operation(self) -> None:
        """ Add new exercise. """

        firstname: str = input('Enter firstname: ')
        lastname: str = input('Enter lastname: ')
        plan_id: int = int(input('Enter plan id: '))
        exercise_type_id: int = int(input('Enter exercise type id: '))
        sets_count: int = int(input('Enter exercise sets: '))
        reps_count: int = int(input('Enter exercise reps: '))
        create_exercise_for_athlete(self.conn, firstname, lastname, plan_id, exercise_type_id, sets_count, reps_count)

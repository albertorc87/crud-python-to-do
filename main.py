import os
from app.tasks.actions import Actions
from store.dummy import Dummy as dummy

def welcome():
    print('MYADMIN TASKS V0.1 🔥')
    print('*' * 50)
    print('Bienvenido, que quieres hacer hoy:')
    print('[C]rear una nueva tarea')
    print('[L]ista de tareas')
    print('[M]arcar tarea como hecha')
    print('[E]liminar una tarea')
    print('[S]ALIR')
    print('*' * 50)


def get_command():
    command = input()
    return command.upper()

def validate_command(command, actions):
    if command == 'C':
        actions.create_task()
    elif command == 'L':
        actions.list_tasks()
    elif command == 'M':
        actions.update_status_task()
    elif command == 'E':
        actions.delete_task()
    elif command == 'S':
        os._exit(1)
    else:
        print('El comando introducido no es válido, por favor, inténtalo de nuevo')

if __name__ == '__main__':

    actions = Actions()

    while True:

        welcome()
        command = get_command()

        try:
            validate_command(command, actions)
        except Exception as err:
            print('*' * 50)
            print(err)
            print('*' * 50)

        print('Pulsa intro para continuar...')
        input()
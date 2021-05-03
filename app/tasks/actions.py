from store.dummy import Dummy as ddbb
from app.tasks.model import Model as TaskModel
from prettytable import PrettyTable


class Actions:

    def create_task(self):
        print('Introduce el nombre de la tarea, pulsa enter para salir')
        task_name = input()

        if task_name == '':
            return

        try:
            task = TaskModel(task_name=task_name)
        except ValueError as err:
            print(err)
            self.create_task()

        data = {
            'id': 0,
            'task_name': task.task_name,
            'created_at': task.created_at,
            'updated_at': task.updated_at,
            'is_done': task.is_done
        }

        res = ddbb.create(task.TABLE_NAME, data)

        if res:
            print('Tarea guardada con éxito')
        else:
            print('Error al guardar la tarea')

    def list_tasks(self, where=None):
        rows = ddbb.get_by(TaskModel.TABLE_NAME, where)

        if not rows:
            return print('Todavía no se ha creado ninguna tarea')

        table = None
        for row in rows:
            if table is None:
                table = PrettyTable([key for key in row.keys()])

            values = []
            for field in row.values():
                if field is True:
                    field = '✅'
                elif field is False:
                    field = ''

                values.append(field)

            table.add_row(values)

        print(table)

    def get_id(self):
        id = (input() or None)

        if id is None:
            return None

        try:
            id = int(id)
        except ValueError as err:
            print('Debes introducir un valor numérico, inténtalo de nuevo o pulsa enter para salir')
            return self.get_id()

        return id

    def delete_task(self):
        print('Introduce el id de la tarea que quieras actualizar o pulsa enter para salir')
        self.list_tasks()

        id = self.get_id()

        if id is None:
            return

        res = ddbb.delete(TaskModel.TABLE_NAME, id)

        if res:
            print('Tarea eliminada con éxito')
        else:
            print('Error al eliminar la tarea')

    def update_status_task(self):
        print('Introduce el id de la tarea que quieras actualizar o pulsa enter para salir')
        self.list_tasks({'is_done': False})

        id = self.get_id()

        if id is None:
            return

        task = self.get_task_by_id(id)

        if not task:
            print('No hemos encontrado la tarea por el id introducido, por favor inténtelo de nuevo')
            self.update_status_task()

        task_model = TaskModel(task_name=task['task_name'], id=task['id'], created_at=task['created_at'], updated_at=task['updated_at'], is_done=task['is_done'])
        task_model.is_done = True

        updated_task = {
            'updated_at': task_model.updated_at,
            'is_done': task_model.is_done,
        }

        res = ddbb.update(TaskModel.TABLE_NAME, id, updated_task)

        if res:
            print('Tarea marcada como realizada con éxito')
        else:
            print('Error al marcar como realizada la tarea')

    def get_task_by_id(self, id):
        return ddbb.get_by_id(TaskModel.TABLE_NAME, id)

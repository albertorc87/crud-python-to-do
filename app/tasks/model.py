import datetime

class Model:

    __id = 0
    __task_name = ''
    __created_at = None
    __updated_at = None
    __is_done = False

    TABLE_NAME = 'tasks'

    def __init__(self, task_name='', id=0, created_at=None, updated_at=None, is_done=False):

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.task_name = task_name
        self.id = id

        self.is_done = is_done

        if created_at is None:
            self.__created_at = timestamp

        if updated_at is None:
            self.__updated_at = timestamp


    @property
    def id(self):
        return self.__id


    @property
    def task_name(self):
        return self.__task_name


    @property
    def created_at(self):
        return self.__created_at


    @property
    def updated_at(self):
        return self.__updated_at


    @property
    def is_done(self):
        return self.__is_done


    @id.setter
    def id(self, id):
        if type(id) != int:
            raise ValueError('El campo id debe ser un número entero')
        elif id < 0:
            raise ValueError('El campo id no puede ser un número negativo')

        self.__id = id


    @task_name.setter
    def task_name(self, task_name):
        if len(task_name) < 3 or len(task_name) > 50:
            raise ValueError(f'El nombre de la tarea debe tener como mínimo 3 caractares y un máximo de 50 caracteres, tamaño actual: {len(task_name)}')
        self.__task_name = task_name


    @is_done.setter
    def is_done(self, is_done):
        self.__updated_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__is_done = is_done
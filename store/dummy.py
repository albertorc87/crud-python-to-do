import json
from json.decoder import JSONDecodeError


class Dummy:

    FILE_NAME = 'store/bbdd.json'

    @classmethod
    def create(cls, table, data):
        ddbb = cls.get_file()

        create_id = None
        if table not in ddbb:
            create_id = 1
            ddbb[table] = []

        if create_id is None:
            create_id = cls.get_last_id(table)

        data['id'] = create_id
        ddbb[table].append(data)
        return cls.save_file(ddbb)

    @classmethod
    def update(cls, table, id, data):
        ddbb = cls.get_file()

        if table not in ddbb:
            return False

        for row in ddbb[table]:
            if row['id'] == id:
                for key, value in data.items():
                    row[key] = value

                return cls.save_file(ddbb)

        return False

    @classmethod
    def delete(cls, table, id):
        ddbb = cls.get_file()

        if table not in ddbb:
            return False

        for row in ddbb[table]:
            if row['id'] == id:
                ddbb[table].remove(row)

                return cls.save_file(ddbb)

        return False

    @classmethod
    def get_last_id(cls, table):
        ddbb = cls.get_file()

        last_id = 0
        for row in ddbb[table]:
            if last_id < row['id']:
                last_id = row['id']

        return last_id + 1

    @classmethod
    def get_all(cls, table):
        ddbb = cls.get_file()

        if table not in ddbb:
            return []

        return ddbb[table]

    @classmethod
    def get_by(cls, table, where):
        rows = cls.get_all(table)

        if where is None:
            return rows

        valid_results = []
        for row in rows:
            is_valid = True
            for key_where, value_where in where.items():
                if value_where != row[key_where]:
                    is_valid = False
                    break

            if is_valid:
                valid_results.append(row)

        return valid_results

    @classmethod
    def get_by_id(cls, table, id):
        ddbb = cls.get_file()

        if table not in ddbb:
            return {}

        rows = ddbb[table]

        for row in rows:
            if row['id'] == id:
                return row

        return {}

    @classmethod
    def save_file(cls, ddbb):
        with open(cls.FILE_NAME, mode='w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(ddbb))

            return True

    @classmethod
    def get_file(cls):

        try:
            f = open(cls.FILE_NAME)
            f.close()
        except IOError:
            raise Exception('DDBB not found')

        with open(cls.FILE_NAME, mode='r', encoding='utf-8') as json_file:
            try:
                ddbb = json.load(json_file)
            except JSONDecodeError:
                raise Exception('Error to read DDBB')

            return ddbb

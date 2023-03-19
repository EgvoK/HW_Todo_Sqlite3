import sqlite3

import config


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def get_item_title(text):
    title = input(text)
    return title


def get_item_description(text):
    description = input(text)
    return description


def string_validation(string):
    if len(string) < 1:
        print(config.STRING_ERROR)
    else:
        title = string
        return title


class Model:

    @staticmethod
    def get_items():
        connection = get_db_connection()
        items = connection.execute('select * from items').fetchall()
        connection.close()
        return items

    @staticmethod
    def add_item():
        titles_list = []
        connection = get_db_connection()
        titles = connection.execute('select title from items').fetchall()
        for i in titles:
            titles_list.append(i[0])

        while True:
            getting_title = get_item_title(config.TITLE_TEXT)
            title = string_validation(getting_title)
            if title:
                if title in titles_list:
                    return print("This title already exists!")
                else:
                    break

        while True:
            getting_description = get_item_description(config.DESC_TEXT)
            description = string_validation(getting_description)
            if description:
                break

        connection.execute('insert into items (title, description) values (?, ?)', (title, description))
        connection.commit()
        connection.close()

        return title

    @staticmethod
    def modify_item():
        titles_list = []
        connection = get_db_connection()
        titles = connection.execute('select title from items').fetchall()
        for i in titles:
            titles_list.append(i[0])

        search_title = get_item_title(config.TITLE_TEXT)
        if search_title not in titles_list:
            print("Todo not found!")
        else:
            while True:
                getting_title = get_item_title(config.NEW_TITLE_TEXT)
                title = string_validation(getting_title)
                if title:
                    break

            while True:
                getting_description = get_item_description(config.NEW_DESC_TEXT)
                description = string_validation(getting_description)
                if description:
                    break

            connection.execute('''update items set title = ?, description = ? where title = ?''',
                               (title, description, search_title))
            connection.commit()
            connection.close()

            return title

    @staticmethod
    def delete_item():
        titles_list = []
        connection = get_db_connection()
        titles = connection.execute('select title from items').fetchall()
        for i in titles:
            titles_list.append(i[0])

        search_title = get_item_title(config.TITLE_TEXT)
        if search_title not in titles_list:
            print("Todo not found!")
        else:
            connection.execute("delete from items where title = ?", (search_title,))
            connection.commit()
            connection.close()

            return search_title

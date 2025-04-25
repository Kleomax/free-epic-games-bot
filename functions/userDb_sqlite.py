import sqlite3




class UsersDatabase:
    def __init__(self):
        self.__connection = sqlite3.connect("db.sqlite3")
        self.__cursor = self.__connection.cursor()

    def add_user(self, user_id: int, activity: str):
        with self.__connection:
            return self.__cursor.execute("INSERT INTO users (user_id, activity) VALUES (?, ?)", (user_id, activity,))

    def set_activity(self, user_id: int, activity: str):
        with self.__connection:
            return self.__cursor.execute("UPDATE `users` SET `activity` = ? WHERE `user_id` = ?", (activity, user_id,))

    def user_exists(self, user_id: int) -> bool:
        with self.__connection:
            result = self.__cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()

            return bool(len(result))

    def get_users(self) -> list:
        with self.__connection:
            result = self.__cursor.execute("SELECT `user_id` FROM `users`").fetchall()

            res = []
            for i in result:
                for b in i:
                    res.append(b)

            return res

    def get_activity_user(self, user_id: int) -> list:
        with self.__connection:
            result = self.__cursor.execute("SELECT `activity` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()

            for row in result:
                activity = str(row[0])

            return activity

    def get_activity_users(self) -> list:
        with self.__connection:
            result = self.__cursor.execute("SELECT `user_id` FROM `users` WHERE `activity` = 'active'").fetchall()

            res = []

            for i in result:
                for b in i:
                    res.append(b)

            return res

    user_activity = property(set_activity, get_activity_users)

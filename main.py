#Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
from operator import index

class User:
    def __init__(self, user_id, name ):
        self._id = user_id
        self._name = name
        self._access_level = 'user'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_access_level(self):
        return self._access_level

class Admin(User):
    _users_list = []

    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def get_access_level(self):
        return self._access_level
    def add_user(self, user):
        if isinstance(user, User):
            Admin._users_list.append(user)
        else:
            raise TypeError('Only user instances can be added')

    def remove_user(self, user_id):
        for index, user in enumerate(Admin._users_list):
            if user.get_id() == user_id:
                deleted_user = Admin._users_list[index]
                print(
                    f"[Удаление] ID: {deleted_user.get_id()}, "
                    f"Имя: {deleted_user.get_name()}, "
                    f"Доступ: {deleted_user.get_access_level()}"
                )
                del Admin._users_list[index]
                return
        raise ValueError('User not found')

    @classmethod
    def get_all_users(cls):
        return cls._users_list.copy()

# создание пользователей
user1 = User(1, 'Саша')
user2 = User(2, 'Оля')
admin = Admin(3, 'Надя')

# администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)

# вывод списка пользователей
for user in Admin.get_all_users():
    print(f'ID: {user.get_id()}, Name: {user.get_name()}, Access: {user.get_access_level()}')

# администратор удаляет пользователя
print("\nУдаление пользователя:")
try:
    admin.remove_user(1)  # Успешное удаление
    admin.remove_user(99) # Несуществующий ID
except ValueError as e:
    print(f"Ошибка: {e}")

# изменение имени пользователя
user2.set_name('actress')
print(f'New name: {user2.get_name()}')

# Итоговый список пользователей
print("\nСписок пользователей после удаления:")
for user in Admin.get_all_users():
    print(f"ID: {user.get_id()}, Name: {user.get_name()}")
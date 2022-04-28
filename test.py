from app.database import Users

from docxtpl import DocxTemplate


import datetime
# from werkzeug.security import generate_password_hash
# from random import choice, randint
#
# for cl in range(1, 12):
#     for let in ["н", "о", "п"] if cl < 8 else ["н", "о"]:
#         for num in range(11, 24):
#             u = Users(
#                 username=f"Student{cl}.{let}.{num}", password=generate_password_hash("qwerty"),
#                 firstname=f"Имя{cl}.{let}.{num}",
#                 lastname=f"Фамилия{cl}.{let}.{num}",
#                 patronymic=f"Отчество{cl}.{let}.{num}",
#                 classroom=f"{cl}{let}", email=f"email{cl}.{let}.{num}@ema.il", role="student"
#             )
#             db.session.add(u)
#             db.session.flush()
#             ui = UserInfo(
#                 user_id=u.id, sex=choice([0, 1]),
#                 birthdate=int(datetime.datetime(year=2022 - cl - randint(6, 8),
#                               month=randint(1, 12), day=randint(1, 28)).timestamp()),
#                 many_children=choice([0, 0, 0, 1]),
#                 fathers_firstname=f"Имя_отца{cl}.{let}.{num}",
#                 fathers_lastname=f"Фамилия_отца{cl}.{let}.{num}",
#                 fathers_patronymic=f"Отчество_отца{cl}.{let}.{num}",
#                 mothers_firstname=f"Имя_матери{cl}.{let}.{num}",
#                 mothers_lastname=f"Фамилия_матери{cl}.{let}.{num}",
#                 mothers_patronymic=f"Отчество_матери{cl}.{let}.{num}"
#             )
#             db.session.add(ui)
#
#
# input("Подтверждение")
#
# db.session.commit()


doc = DocxTemplate("app/templates/documents/word/Справка об обучении.docx")

t1 = datetime.datetime.now().timestamp()


def write_data(users: list or Users):
    need_length = 45
    users = users if type(users) is list else [users]
    for index, user in enumerate(users):
        name = user.firstname
        lastname = user.lastname
        patronymic = user.patronymic
        length = sum(map(lambda x: len(x), [name, lastname, patronymic])) + 4
        residual = (need_length - length) if length < need_length else 0
        # user = [
        #     " " * (residual // 2) + name,
        #     lastname,
        #     patronymic + " " * (residual // 2),
        #     datetime.datetime.fromtimestamp(user.info.birthdate).strftime("%d.%m.%Y"),
        #     user.classroom[:-1],
        #     user.classroom[-1]
        # ]
        users[index].firstname = " " * (residual // 2) + name
        users[index].patronymic = patronymic + " " * (residual // 2)
        users[index].birthdate = datetime.datetime.fromtimestamp(user.info.birthdate).strftime("%d.%m.%Y")

    doc.render(context={"users": users})
    doc.save(f"word/справка-Пользователи.docx")


# user_list = sample(Users.query.all(), 100)
#
# for num, user in enumerate(user_list):
#     user: Users
#     if "student" not in user.role:
#         continue
#     l = len(user_list)
#     if not (l - num) % 50:
#         print(f"Осталось: {l - num}")
#     write_data(user)
#
#
# t2 = datetime.datetime.now().timestamp()
#
# t = t2 - t1
#
# print("Время выполнения:", t, "Секунд")

write_data(Users.query.first())

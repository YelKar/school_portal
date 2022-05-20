import os
import time

from application.database import Users

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


# def progress_bar_update(
#         value: int,
#         bar="[%b]%d%",
#         on_let="#",
#         off_let=" ",
#         max_val=100,
#         step: int = 2,
#         last: bool = False
# ):
#     value //= step
#     max_val //= step
#     print(
#         "\r" +
#         bar.replace(
#             "%d",
#             str(value * step)
#         ).replace(
#             "%b",
#             on_let * value + off_let * (max_val - value)
#         ), end="\n" if last else ""
#     )
#
#
# progress_bar_update(0, bar="%b Progress: %d", on_let="▓", off_let="░")
# time.sleep(1)
# for i in range(120):
#     progress_bar_update(i, bar="%b Progress: %d", on_let="▓", off_let="░", last=i == 100)
#     time.sleep(.1)
from docx2pdf import convert


for doc in os.listdir("app/templates/documents/docx/templates"):
    convert(f"app/templates/documents/docx/templates/{doc}",
            f"app/templates/documents/pdf/templates/{doc.replace('docx', 'pdf')}")

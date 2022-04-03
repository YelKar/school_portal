from app.database import Users, UserInfo
from app import db
import datetime
from werkzeug.security import generate_password_hash
from random import choice, randint

for cl in range(1, 12):
    for let in ["н", "о", "п"] if cl < 8 else ["н", "о"]:
        for num in range(11, 24):
            u = Users(
                username=f"Student{cl}.{let}.{num}", password=generate_password_hash("qwerty"),
                firstname=f"Имя{cl}.{let}.{num}",
                lastname=f"Фамилия{cl}.{let}.{num}",
                patronymic=f"Отчество{cl}.{let}.{num}",
                classroom=f"{cl}{let}", email=f"email{cl}.{let}.{num}@ema.il", role="student"
            )
            db.session.add(u)
            db.session.flush()
            ui = UserInfo(
                user_id=u.id, sex=choice([0, 1]),
                birthdate=int(datetime.datetime(year=2022 - cl - randint(6, 8), month=randint(1, 12), day=randint(1, 28)).timestamp()),
                many_children=choice([0, 0, 0, 1]),
                fathers_firstname=f"Имя_отца{cl}.{let}.{num}",
                fathers_lastname=f"Фамилия_отца{cl}.{let}.{num}",
                fathers_patronymic=f"Отчество_отца{cl}.{let}.{num}",
                mothers_firstname=f"Имя_матери{cl}.{let}.{num}",
                mothers_lastname=f"Фамилия_матери{cl}.{let}.{num}",
                mothers_patronymic=f"Отчество_матери{cl}.{let}.{num}"
            )
            db.session.add(ui)


input("Подтверждение")

db.session.commit()


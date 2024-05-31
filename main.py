# Модуль 8/2 классы. Наследование, Инкапсуляция, Полиморфизм.
# Кошлаков Евгений Python 320-2

# Задача 1
# У вас есть абстракция учитель, вам надо написать класс согласно этой абстракции характеристики класса: Поля
# (атрибуты) класса class Teacher: имя (name) в примере Иван Петров; образование (education) в примере БГПУ; опыт работы
# (experience) в примере 4 года; Все атрибуты необходимо сделать защищенными. Для данных атрибутов необходимо написать
# геттеры (для всех) а для атрибута опыт работы (experience) также необходим еще и сеттер.

class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_teacher_data(self):
        return f'{self.__name}, образование {self.__education}, опыт работы {self.__experience} года.'

    def add_mark(self, student_name, mark):
        return f'{self.__name} поставил оценку {mark} студенту {student_name}.'

    def remove_mark(self, student_name, mark):
        return f'{self.__name} удалил оценку {mark} студенту {student_name}.'

    def give_a_consultation(self, class_name):
        return f'{self.__name} провел консультацию в классе {class_name}.'


teacher_1 = Teacher('Иван Петров', 'БГПУ', 4)
print(teacher_1.get_teacher_data())
print(teacher_1.add_mark('Петр Сидоров', 4))
print(teacher_1.remove_mark('Петр Сидоровв', 3))
print(teacher_1.give_a_consultation('9Б'))

# Задача 2
# Написать класс наследник DisciplineTeacher, его классом родителем (базовым классом) будет класс Teacher, ему
# необходимо добавить 2 новых атрибута. discipline - предмет его надо перенести из класса Teacher; job_title - должность
# (например завуч, директор, учитель старших классов). Все атрибуты необходимо сделать защищенными. Для данных атрибутов
# необходимо написать геттеры (для всех) а для атрибута job_title также необходим еще и сеттер. Далее необходимо
# адаптировать методы класса родителя а именно: get_teacher_data add_mark remove_mark give_a_consultation

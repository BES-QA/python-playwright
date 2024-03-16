from faker import Faker


class Fake:

    @staticmethod
    def random_rus_phone():
        """Генератор случайного российского номера телефона"""
        return Faker('ru_RU').phone_number()

    @staticmethod
    def random_mail():
        """Генератор случайной электронной почты"""
        return Faker().ascii_free_email()

    @staticmethod
    def random_job():
        """Генератор случайного наименования профессии"""
        return Faker('ru_RU').job()

    @staticmethod
    def random_hostname():
        """Генератор случайного hostname"""
        return Faker().hostname()

    @staticmethod
    def random_url():
        """Генератор случайного URL"""
        return Faker().uri()

    @staticmethod
    def random_company_name():
        """Генератор случайного названия компании"""
        return Faker().company()

    @staticmethod
    def random_full_name(gender: str = None):
        """Генератор случайного ФИО"""
        full_name = None
        if gender is None:
            full_name = Faker('ru_RU').name()
        elif gender.casefold() == 'male':
            full_name = Faker('ru_RU').name_male()
        elif gender.casefold() == 'female':
            full_name = Faker('ru_RU').name_female()
        return full_name

    @staticmethod
    def random_last_name(gender: str = None):
        """Генератор случайной фамилии"""
        last_name = None
        if gender is None:
            last_name = Faker('ru_RU').last_name()
        elif gender.casefold() == 'male':
            last_name = Faker('ru_RU').last_name_male()
        elif gender.casefold() == 'female':
            last_name = Faker('ru_RU').last_name_female()
        return last_name

    @staticmethod
    def random_first_name(gender: str = None):
        """Генератор случайного имени"""
        first_name = None
        if gender is None:
            first_name = Faker('ru_RU').first_name()
        elif gender.casefold() == 'male':
            first_name = Faker('ru_RU').first_name_male()
        elif gender.casefold() == 'female':
            first_name = Faker('ru_RU').first_name_female()
        return first_name

    @staticmethod
    def random_full_address():
        return Faker('ru_RU').address()

    @staticmethod
    def random_city_name():
        return Faker('ru_RU').city()

    @staticmethod
    def random_street_name():
        return Faker('ru_RU').street_name()

    @staticmethod
    def random_postalcode():
        return Faker('ru_RU').postcode()

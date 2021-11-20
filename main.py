import datetime as dt

"""
    Общие замечания.
    # Комментарий к функции или методу класса, пишем внутри.
    https://www.python.org/dev/peps/pep-0257/
    
    def complex(real=0.0, imag=0.0):
        '''
        Form a complex number.
        '''
    
    # Старатся избегать лишних if, else, а так же применять Guard Block.
    # Правильно и в одном стиле форматировать f строки.
"""


class Record:

    # Можно записать более лакочнее обработку параметра date.
    # Например 'результат1' if 'условие' else 'результат2'.
    # Что сделает код еще более читабельнее.

    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0

        # Record - это сам класс, а в списке self.records, экземпляры класса.
        # Поэтому как и остальные пременные называем с маленькой буквы.
        # Сравните с вашей функцей get_week_stats.

        for Record in self.records:
            if Record.date == dt.datetime.now().date():

                # Старайтесь передерживаться одинакового подхода,
                # Сравните с get_week_stats() => week_stats += record.amount

                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            """
            Здесь можно улучшить код с конструкцией,
            if 'условие1' > a > 'условие2'
            """
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):

    # В функции get_calories_remained пристуствует лишний else.
    # Бэкслеши для переносов не применяются.
    # При возвращении результата строки скобки избыточны.

    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'

        # Последний блок заменяем на else

        elif currency_type == 'rub':

            # И здесь ошибка, '==' оператор сравнения, а не присвоения.
            # В случае с рублевой валютой не происходит пересчет.
            # Поэтому строчка c cash_remained здесь вообще лишняя.

            cash_remained == 1.00
            currency_type = 'руб'

        # Отделяем следующую логическую часть пустой строкой.

        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'

        # Бэкслеши для переносов не применяются.
        # Последний elif избыточен, потому что вариантов больше не осталось.

        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        # Метод и так наследуется из класса Calculator.
        # В этой конструкции нету смысла.

        super().get_week_stats()

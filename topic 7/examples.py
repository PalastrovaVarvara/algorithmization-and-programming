class BankAccount:
    # Атрибут класса
    bank_name = "Python Bank"
    accounts_count = 0
    
    def __init__(self, owner, initial_balance=0):
        # Атрибуты экземпляра
        self.owner = owner
        self._balance = initial_balance    # защищённый атрибут
        self._transactions = []            # история операций
        
        # Увеличиваем счётчик созданных счетов
        BankAccount.accounts_count += 1
    
    @property
    def balance(self):
        """Геттер для баланса"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """Сеттер с валидацией"""
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value
    
    def deposit(self, amount):
        """Пополнение счёта"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        self._transactions.append(f"Пополнение: +{amount}")
        return f"Пополнено {amount}. Баланс: {self._balance}"
    
    def withdraw(self, amount):
        """Снятие со счёта"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._transactions.append(f"Снятие: -{amount}")
        return f"Снято {amount}. Баланс: {self._balance}"
    
    def get_transactions(self):
        """Получить историю операций"""
        return self._transactions.copy()  # возвращаем копию для защиты данных
    
    @classmethod
    def get_total_accounts(cls):
        """Метод класса — получить количество счетов"""
        return f"Всего открыто счетов: {cls.accounts_count}"
    
    @staticmethod
    def validate_owner_name(name):
        """Статический метод — проверка имени владельца"""
        return bool(name and len(name) >= 2)
    
    def __str__(self):
        return f"Счёт владельца {self.owner}, баланс: {self._balance}"
    
    def __del__(self):
        """Деструктор — уменьшаем счётчик при удалении счёта"""
        BankAccount.accounts_count -= 1
        print(f"Счёт {self.owner} закрыт")

# Использование
print(BankAccount.get_total_accounts())     # Всего открыто счетов: 0

account1 = BankAccount("Иван Петров", 1000)
account2 = BankAccount("Мария Сидорова", 500)

print(account1.deposit(500))                # Пополнено 500. Баланс: 1500
print(account1.withdraw(200))               # Снято 200. Баланс: 1300
print(account1.balance)                     # 1300

print(BankAccount.get_total_accounts())     # Всего открыто счетов: 2
print(account1)                             # Счёт владельца Иван Петров, баланс: 1300

print(BankAccount.validate_owner_name("Анна"))  # True
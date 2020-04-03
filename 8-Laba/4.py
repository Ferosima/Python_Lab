#17. Клас Покупець: Прізвище, Ім'я, По батькові, Адреса, Номер кредитної картки, Номер банківського рахунку;
#  конструктор; Методи: установка значень атрибутів, отримання значень атрибутів, висновок інформації.
# Створити масив об'єктів даного класу.
# Вивести список покупців в алфавітному порядку і список покупців, у яких номер кредитної картки знаходиться в заданому діапазоні.
import random
import string

def randomStr(size):
  return ''.join(random.choice(string.ascii_letters) for _ in range(size))
def randomNumeralStr(size):
  return ''.join(random.choice(string.digits) for _ in range(size))

class Customer:
  firstName: str = None
  secondName: str = None
  middleName: str = None
  address: str = None
  creditCard: str = None
  bankNum: str = None

  def __str__(self):
    return f"""
      Имя покупателя {self.firstName}
      Фамилия покупателя {self.secondName}
      Отчество покупателя {self.middleName}
      Аддрес покупателя {self.address}
      Номер кредитной карты покупателя {self.creditCard}
      Номер банковскового счета покупателя {self.bankNum}
      """

  def __init__(self, firstName: str, secondName: str, middleName: str, address: str, creditCard: str, bankNum: str):
    self.firstName = firstName
    self.secondName = secondName
    self.middleName = middleName
    self.address = address
    self.creditCard = creditCard
    self.bankNum = bankNum

  def __getattr__(self, name: str):
    if(name == 'fullName'):
      return self.firstName + ' ' + self.secondName + ' ' + self.middleName

  def setFirstName(self, firstName: str):
    self.firstName = firstName
  def setSecondName(self, secondName: str):
    self.firstName = secondName
  def setMiddleName(self, middleName: str):
    self.firstName = middleName
  def setAddress(self, address: str):
    self.firstName = address
  def setCreditCard(self, creditCard: str):
    self.firstName = creditCard
  def setBankNum(self, bankNum: str):
    self.firstName = bankNum

  def getFirstName(self):
    return self.firstName
  def getSecondName(self):
    return self.secondName
  def getMiddleName(self):
    return self.middleName
  def getAddress(self):
    return self.address
  def getCreditCard(self):
    return self.creditCard
  def getBackNum(self):
    return self.bankNum

customers = []

def isCreditCardInDiap(customer: Customer, maxNum: str):
  for i in range(0, len(customer.creditCard)):
    if(int(customer.creditCard[i]) > int(maxNum[i])):
      return customer
    if(int(customer.creditCard[i]) < int(maxNum[i])):
      return False
  return False

for i in range(0, 5):
  customers.append(Customer(
    randomStr(10), randomStr(10), randomStr(10), randomStr(20), randomNumeralStr(16), randomNumeralStr(8)
  ))
  print("Информация о покупателе ", customers[i])

customers.sort(key=lambda customer: customer.fullName)

print('Отсортированный список покупателей')
for i in range(0, 5):
  print(customers[i])

maxNum = randomNumeralStr(16)
print('Список покупателей чей номер карты находится в диапазоне от 0 до maxNum')
for i in range(0, 5):
  if(isCreditCardInDiap(customers[i], maxNum) == False):
    pass
  else:
    print(customers[i])
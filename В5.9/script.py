from script2 import TimeThis

#Контекстный менеджер
def f():
    for j in range(1000000):
        pass
with TimeThis() as t:
	f()


# Количество запусков по умолчанию
@TimeThis()
def g():
    for j in range(1000000):
        pass
g()
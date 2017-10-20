# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
import datetime
import contextlib


# @contextlib.contextmanager
# def timer():
#     t1 = datetime.datetime.now()
#     yield
#     t2 = datetime.datetime.now()
#     res = t2 - t1
#     res1 = str(res.seconds) + '.' + str(res.microseconds)
#     print('Execution time '+res1)

class timer:
    t1 = 0
    def __enter__(self):
        self.t1 = datetime.datetime.now()
    def __exit__(self, exp_type,exp_value, traceback):
        t2 = datetime.datetime.now()
        res = t2 - self.t1
        res1 = str(res.seconds) + '.' + str(res.microseconds)
        print('Execution time ' + res1)
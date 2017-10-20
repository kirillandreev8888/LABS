# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.items = iter(items) if isinstance(items, list) else items
        #self.ignore_case = False

        self.ignore_case = kwargs.get('ignore_case', False)

        self.dupl = []


    def __next__(self):
        # Нужно реализовать __next__
        while True:
            try:

                cur = next(self.items)

                if isinstance(cur, str) and self.ignore_case is True:
                    check = cur.upper()
                else:
                    check = cur

                if not check in self.dupl:
                    self.dupl.append(check)
                    return cur
            except Exception:
                raise StopIteration

    def __iter__(self):
        return self

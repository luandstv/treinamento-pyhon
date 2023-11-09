def multiplicaArgs(*args):
    def multiplica():
        total = 1
        for i in args:
            total *= i
        return total
    return multiplica()

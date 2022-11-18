reg = set()


def register(active=True):
    def wrapper(func):
        if active:
            reg.add(func)
        else:
            reg.discard(func)

        return func

    return wrapper


@register(active=False)
def f1():
    print("F1")

print(register()(f1)())

register(active=True)(f1)
print(reg)

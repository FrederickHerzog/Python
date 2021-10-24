from datetime import datetime


def magic(*args, **kwargs) -> tuple:
    date = datetime.now().strftime("%D - %H%M.%S")
    a = args
    print(*a)
    k = kwargs
    return (*a, [*k.items()], date)


def magic2():
    pass


r = True
i = magic(1212,
          "Welcome",
          name="Rick",
          age=33,
          rank='captain',
          id='2345234234',
          is_valid=True,
          n={11, 12, 12, 13, 14}
          )

print(i)

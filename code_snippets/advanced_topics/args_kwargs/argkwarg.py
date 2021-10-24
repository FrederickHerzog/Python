from datetime import datetime

def magic(*args, **kwargs) -> tuple:
    a = args
    k = kwargs
    return (*a, [*k.items()])
    
date = datetime.now().strftime("%D - %H%M.%S")
r = True
i = magic(date,
    "Welcome",
    name="Rick", 
    age=33, 
    rank='captain',
    id='2345234234',
    is_valid=True,
    n = {11, 12, 12, 13, 14}
      )

print(i[2])

def add(firstName: str | None  ,lastName : str = None):
    return firstName + " " +lastName



f_name = 34
l_name = "gates"

name  = add(f_name,l_name)
print(name)
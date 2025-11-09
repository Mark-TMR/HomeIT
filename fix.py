

result = []

def divider(a, b):


    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше за 100")
    return a / b


raw_items = [
    (10, 2),
    (2, 5),
    ("123", 4),
    (18, 0),
    ([], 15),
    (8, 4)
]

for key, val in raw_items:
    try:
        res = divider(key, val)
    except Exception as e:

        print(f"Ключ={key!r}, Значення={val!r} -> Виникла помилка: {type(e).__name__}: {e}")
    else:
        result.append(res)

print("Результат:", result)
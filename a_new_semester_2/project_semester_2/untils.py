import re

def check_query(query: str):
    # Паттерн для перевірки відповідності формату
    pattern = r'^[a-zA-Z]+(?: [a-zA-Z]+)*$'

    # Використовуємо регулярний вираз для перевірки
    if re.match(pattern, query):
        return True
    else:
        return False
    

def introspection_info(obj):
    """Функция для интроспекции объекта."""
    # Получаем тип объекта
    type_info = {'type': type(obj).__name__}

    # Получаем только атрибуты объекта, исключая методы
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    type_info['attributes'] = attributes

    # Проверяем, является ли объект экземпляром класса
    if isinstance(obj, type):
        # Если объект является классом, получаем его методы
        methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
        type_info['methods'] = methods

    # Получаем модуль, к которому принадлежит объект
    module = obj.__class__.__module__
    type_info['module'] = module

    return type_info


# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция списка
list_info = introspection_info([1, 2, 3])
print(list_info)


# Интроспекция класса
class MyClass:
    pass


my_class_info = introspection_info(MyClass)
print(my_class_info)
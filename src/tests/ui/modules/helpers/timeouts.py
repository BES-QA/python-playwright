class Timeouts:
    """
    Класс описывает ожидания.
    Для получения секунд используется формула 1мс * 1000 = 1сек
    """
    page_timeout: float = 30 * 1000
    element_timeout: float = 10 * 1000

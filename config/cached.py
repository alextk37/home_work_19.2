from django.core.cache import cache


def get_cached(model, cached_time=0):
    """
        Функция для кеширования.
        cached_time - Время кеширования в секундах
    """
    model_name = model.__name__ + '_data'
    data = cache.get(model_name)

    if not data:

        data = model.objects.all()
        cache.set(model_name, data, cached_time)
    return data


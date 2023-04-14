from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(text):
    bad_words = ['сфинкса', 'китай']
    if type(text) == str:
        for word in text.split():
            if word.lower() in bad_words:
                text = text.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    else:
        raise ValueError('Входные данные не являются строкой!')
    return text
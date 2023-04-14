import django_filters
from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateTimeInput

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ), label= 'После даты'
    )
    # title_search = django_filters.CharFilter(
    #     field_name='title',
    #     lookup_expr='icontains',
    #     label='Поиск по постам:',
    # )
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           'title': ['icontains'],
           'categoryType': ['exact']
       }
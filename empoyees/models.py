from django.db import models
import mptt
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Employees(MPTTModel):
    class Meta:
        ordering = ('tree_id', 'level')

    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=50, unique=True, verbose_name = u'Имя')
    position = models.CharField(max_length = 25, verbose_name = u'Должность')
    date_begin = models.DateField(verbose_name="Дата приема на работу", null=True)
    salary = models.FloatField(verbose_name="Заработная плата")
    photo = models.ImageField(upload_to="img/photo_emp/", default='img/photo_emp/1_1_design.png', null=True, blank=True, verbose_name = u'Фото')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', verbose_name="Начальник")

    # start Ограничение максимального уровня вложенности
    # def save(self, *args, **kwargs):
    #     max_nesting = 5
    #     if self.parent.level:
    #         current_level = self.parent.level
    #     else: 0
    #
    #     if current_level < max_nesting:
    #         super().save(*args, **kwargs)
    #     else:
    #         raise ValueError("Превышен максимальный уровень вложенности: %i" % max_nesting)
    #end Ограничение максимального уровня вложенности

    def delete(self, *args, **kwargs):
        Employees.objects.rebuild()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

mptt.register(Employees, order_insertion_by=['name'])
# Generated by Django 2.1.3 on 2018-12-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empoyees', '0003_auto_20181203_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'ordering': ('tree_id', 'level')},
        ),
        migrations.AlterField(
            model_name='employees',
            name='photo',
            field=models.ImageField(blank=True, default='img/photo_emp/1_1_design.png', null=True, upload_to='img/photo_emp/'),
        ),
    ]
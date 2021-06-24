# Generated by Django 3.2.4 on 2021-06-24 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=10, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=10, verbose_name='Предмет'),
        ),
    ]

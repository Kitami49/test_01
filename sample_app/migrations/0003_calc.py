# Generated by Django 4.1.3 on 2022-11-10 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0002_alter_post_micropost_alter_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField(verbose_name='num1')),
                ('num2', models.IntegerField(verbose_name='num2')),
                ('sum', models.IntegerField(blank=True, verbose_name='加')),
                ('sub', models.IntegerField(blank=True, verbose_name='減')),
                ('mul', models.IntegerField(blank=True, verbose_name='乗')),
                ('div', models.IntegerField(blank=True, verbose_name='除')),
            ],
        ),
    ]

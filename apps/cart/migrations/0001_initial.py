# Generated by Django 5.0.2 on 2024-03-05 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flour', '0001_initial'),
        ('tort', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session', models.CharField(max_length=120, verbose_name='Сессия пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.card', verbose_name='Корзина')),
                ('flour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='flour.flour', verbose_name='Мучное')),
                ('tort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='tort.tort', verbose_name='Торт')),
            ],
        ),
    ]

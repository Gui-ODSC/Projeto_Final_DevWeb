# Generated by Django 3.1.4 on 2023-12-05 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id_portfolio', models.AutoField(db_column='id_portfolio', primary_key=True, serialize=False)),
                ('nome_portfolio', models.CharField(max_length=255)),
                ('descricao_portfolio', models.TextField()),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Portfolio',
            },
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-29 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('arquivo', models.FileField(upload_to='pdf/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materiais.categoria')),
            ],
        ),
    ]

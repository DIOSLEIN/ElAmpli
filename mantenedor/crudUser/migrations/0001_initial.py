# Generated by Django 2.1.1 on 2019-10-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('appat', models.CharField(max_length=50)),
                ('apmat', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ct_pacienteId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
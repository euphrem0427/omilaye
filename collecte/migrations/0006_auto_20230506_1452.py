# Generated by Django 3.2.12 on 2023-05-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0005_alter_collectonsite_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parameterswaterquality',
            options={'verbose_name': "Paramètres qualité de l'eau"},
        ),
        migrations.AddField(
            model_name='parameterswaterquality',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
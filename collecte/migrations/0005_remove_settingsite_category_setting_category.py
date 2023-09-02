# Generated by Django 4.2.3 on 2023-09-02 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collecte', '0004_remove_maintenance_category_settingsite_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingsite',
            name='category',
        ),
        migrations.AddField(
            model_name='setting',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='collecte.categorymaintenance'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-11 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20210411_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viveros',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.ciudades'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_exercisehistory_final_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisehistory',
            name='final_score',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Score'),
        ),
    ]

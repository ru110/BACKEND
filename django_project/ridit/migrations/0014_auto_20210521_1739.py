# Generated by Django 3.2 on 2021-05-21 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0013_auto_20210521_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='service',
        ),
        migrations.AddField(
            model_name='partner',
            name='service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ridit.service'),
            preserve_default=False,
        ),
    ]

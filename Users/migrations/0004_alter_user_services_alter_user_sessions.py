# Generated by Django 4.0.1 on 2022-02-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='services',
            field=models.JSONField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='sessions',
            field=models.JSONField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
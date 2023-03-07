# Generated by Django 4.0.1 on 2022-02-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_user_code_user_code_expired_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='code_expired_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Code expired time'),
        ),
    ]
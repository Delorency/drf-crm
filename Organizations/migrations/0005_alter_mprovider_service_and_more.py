# Generated by Django 4.0.1 on 2022-02-10 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0004_mprovider_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mprovider',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_mprovider', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='organization_member',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_members', to='Organizations.service', verbose_name='Service'),
        ),
    ]

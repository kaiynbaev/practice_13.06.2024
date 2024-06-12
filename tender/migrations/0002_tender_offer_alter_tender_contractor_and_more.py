# Generated by Django 5.0.6 on 2024-06-12 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='offer',
            field=models.ManyToManyField(blank=True, related_name='tender_offers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tender',
            name='contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenders_as_contractor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tender',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenders_as_customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
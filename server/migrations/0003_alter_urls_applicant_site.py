# Generated by Django 4.2.7 on 2024-03-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_urls_applicant_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='applicant_site',
            field=models.CharField(blank=True, default='None', max_length=300, null=True),
        ),
    ]

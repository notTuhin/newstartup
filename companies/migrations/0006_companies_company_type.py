# Generated by Django 3.2.3 on 2021-07-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20210711_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='company_type',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Gaming', 'Gaming Company'), ('Web Services', 'Senior'), ('Products', 'Products')], default='Software', max_length=12),
        ),
    ]
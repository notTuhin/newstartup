# Generated by Django 3.2.3 on 2021-07-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_companies_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='logo',
            field=models.ImageField(default='media/default.jpg', upload_to='posts/media/'),
        ),
    ]
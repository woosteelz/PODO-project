# Generated by Django 3.2.8 on 2021-11-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='priority',
            field=models.CharField(choices=[(1, 'very important'), (2, 'important'), (3, 'normal')], default=3, max_length=11),
        ),
    ]
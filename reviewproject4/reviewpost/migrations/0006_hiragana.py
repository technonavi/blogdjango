# Generated by Django 4.1.5 on 2023-02-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0005_remove_reviewmodel_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiragana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moji', models.CharField(max_length=50, verbose_name='平文字')),
            ],
        ),
    ]
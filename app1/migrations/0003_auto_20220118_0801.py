# Generated by Django 2.2 on 2022-01-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='personal', max_length=255),
        ),
    ]

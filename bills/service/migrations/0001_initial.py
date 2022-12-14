# Generated by Django 2.2.16 on 2022-08-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=20)),
                ('client_org', models.TextField()),
                ('account_number', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('service', models.TextField()),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]

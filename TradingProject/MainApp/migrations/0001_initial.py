# Generated by Django 3.2.4 on 2023-02-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BANKNIFTY', models.CharField(max_length=20)),
                ('DATE', models.DateField()),
                ('TIME', models.TimeField()),
                ('OPEN', models.FloatField()),
                ('HIGH', models.FloatField()),
                ('LOW', models.FloatField()),
                ('CLOSE', models.FloatField()),
                ('VOLUME', models.IntegerField()),
            ],
        ),
    ]

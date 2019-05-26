# Generated by Django 2.2.1 on 2019-05-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('tweet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('tweet_text', models.CharField(max_length=30, null=True)),
                ('user_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-02-17 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='verify',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='smsauth.signup')),
                ('smscode', models.CharField(max_length=20)),
            ],
        ),
    ]

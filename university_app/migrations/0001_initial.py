# Generated by Django 3.1.5 on 2021-01-31 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_app.university')),
            ],
        ),
    ]

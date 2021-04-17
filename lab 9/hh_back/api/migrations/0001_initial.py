# Generated by Django 2.1.5 on 2021-04-17 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('salary', models.FloatField()),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Company')),
            ],
        ),
    ]

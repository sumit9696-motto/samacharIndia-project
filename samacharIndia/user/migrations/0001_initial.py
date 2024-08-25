# Generated by Django 3.2.4 on 2021-10-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('cpic', models.ImageField(default='', upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='desnews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('headlines', models.CharField(max_length=400)),
                ('subject', models.CharField(max_length=800)),
                ('newsdes', models.TextField(max_length=8000)),
                ('newspic', models.ImageField(default='', upload_to='static/news/')),
                ('ndate', models.DateField()),
                ('ncategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2018-02-09 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('born', models.CharField(max_length=100)),
                ('Bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('published_at', models.DateField(null=True)),
                ('summary', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='books')),
                ('authors', models.ManyToManyField(blank=True, to='mysite.Authors')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('book', models.ManyToManyField(blank=True, to='mysite.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('rate', models.IntegerField()),
                ('review', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='user',
            field=models.ManyToManyField(blank=True, through='mysite.User_books', to='mysite.Profile'),
        ),
    ]

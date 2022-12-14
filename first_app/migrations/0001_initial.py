# Generated by Django 4.1.1 on 2022-09-13 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name='Book title')),
                ('description', models.TextField(default='Any text')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('genre', models.CharField(choices=[('COMEDY', 'Comedy'), ('TRAGEDY', 'Tragedy'), ('FICTION', 'Fiction'), ('NON_FICTION', 'Non Fiction'), ('ROMANCE', 'Romance')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('number', models.PositiveSmallIntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(default='Lagos', max_length=255)),
                ('country', models.CharField(default='Nigeria', max_length=255)),
                ('publisher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='first_app.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='first_app.publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', through='first_app.BookAuthor', to='first_app.book'),
        ),
    ]

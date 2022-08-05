# Generated by Django 4.0.6 on 2022-08-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_slug', models.IntegerField(default=0)),
                ('blog_title', models.CharField(default='', max_length=100)),
                ('blog_sub_heading', models.CharField(default='', max_length=50)),
                ('blog_sub_heading1', models.CharField(default='', max_length=50)),
                ('blog_content', models.CharField(default='', max_length=5000)),
                ('blog_pub_date', models.DateField()),
            ],
        ),
    ]

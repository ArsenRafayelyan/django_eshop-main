# Generated by Django 4.1.7 on 2023-02-22 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='homeslider',
            options={'verbose_name': 'HomeSlider', 'verbose_name_plural': 'HomeSliders'},
        ),
        migrations.AlterModelOptions(
            name='homeslideractive',
            options={'verbose_name': 'HomeSliderActive', 'verbose_name_plural': 'HomeSlidersActive'},
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='SubCategory name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categ', to='main.category')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategories',
            },
        ),
    ]

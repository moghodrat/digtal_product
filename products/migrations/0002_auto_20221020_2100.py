# Generated by Django 3.2 on 2022-10-20 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=2, verbose_name='file_type'),
        ),
        migrations.AlterField(
            model_name='category',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='categories/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='products.product', verbose_name='product'),
        ),
    ]
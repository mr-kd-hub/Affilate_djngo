# Generated by Django 3.0.8 on 2020-10-02 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0013_remove_category_feature_to_home_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='feature_to_home_page',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
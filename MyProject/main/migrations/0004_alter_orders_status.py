# Generated by Django 4.2.11 on 2024-05-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_for_sale_product_is_new_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Нова'), ('Order Confirmed', 'Приета'), ('Out for Delivery', 'Обработва се'), ('Delivered', 'Изпратена')], max_length=50, null=True),
        ),
    ]

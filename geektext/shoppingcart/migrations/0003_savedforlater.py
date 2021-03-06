# Generated by Django 2.1.5 on 2019-04-09 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0002_product_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedForLater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.Cart')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.Product')),
            ],
        ),
    ]

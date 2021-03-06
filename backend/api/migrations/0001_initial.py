# Generated by Django 3.2.9 on 2021-11-20 22:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('shipping_address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('fk_customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('product_description', models.CharField(default='N/A', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('product_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=250, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('fk_order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.order')),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='StorageRack',
            fields=[
                ('storage_rack_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('fk_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_racks', to='api.inventory')),
                ('fk_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='storage_racks', to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('product_specification_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_specification_name', models.CharField(max_length=50)),
                ('product_specification_value', models.CharField(max_length=50)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='api.producttype')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.producttype'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_products', to='api.productspecification'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_products', to='api.productspecification'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tertiary_products', to='api.productspecification'),
        ),
        migrations.AddField(
            model_name='order',
            name='fk_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.store'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='fk_building',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='api.store'),
        ),
        migrations.CreateModel(
            name='FiredEmployee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('ssn', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('work_place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.store')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('ssn', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='api.employee')),
                ('work_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='api.store')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('product_name', 'spec1', 'spec2', 'spec3', 'product_description')},
        ),
    ]

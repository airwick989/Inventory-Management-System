# Generated by Django 3.2.9 on 2021-11-22 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_firedemployee_work_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='fk_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fk_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='api.store'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='fk_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.order'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='fk_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactionbs', to='api.product'),
        ),
    ]

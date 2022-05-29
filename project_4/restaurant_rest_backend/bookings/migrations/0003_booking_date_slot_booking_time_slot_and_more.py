# Generated by Django 4.0 on 2022-05-14 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_orderitem_order_alter_user_email_alter_user_id_and_more'),
        ('bookings', '0002_remove_timeslot_available_tables_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date_slot',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slot',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='accounts.user'),
        ),
    ]

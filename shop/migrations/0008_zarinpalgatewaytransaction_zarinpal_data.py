# Generated by Django 5.1.1 on 2024-10-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_zarinpalgatewaytransaction_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='zarinpalgatewaytransaction',
            name='zarinpal_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-09 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvv_otp_check', '0005_auto_20181007_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcarddetails',
            name='cvc',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='creditcarddetails',
            name='mm',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='creditcarddetails',
            name='number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='creditcarddetails',
            name='yyyy',
            field=models.SmallIntegerField(),
        ),
    ]

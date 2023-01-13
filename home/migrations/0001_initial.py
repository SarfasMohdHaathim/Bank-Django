# Generated by Django 4.1.5 on 2023-01-13 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(choices=[('ERANAKULAM', 'ERANAKULAM'), ('KOZHIKODE', 'KOZHIKODE'), ('ALAPUZHA', 'ALAPUZHA'), ('MALAPPURAM', 'MALAPPURAM'), ('TRISUR', 'TRISUR')], max_length=20)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20)),
                ('account_type', models.CharField(choices=[('SAVINGS', 'SAVINGS ACCOUNT'), ('CURRENT', 'CURRENT ACCOUNT')], max_length=20)),
                ('debitcard', models.BooleanField(default=False)),
                ('creditcard', models.BooleanField(default=False)),
                ('passbook', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
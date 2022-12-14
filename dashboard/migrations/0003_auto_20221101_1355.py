# Generated by Django 2.2.12 on 2022-11-01 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20221025_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailtrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('kodebrg', models.CharField(max_length=8)),
                ('qty', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('tgltrans', models.DateTimeField(auto_now_add=True)),
                ('total', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Jenis'),
        ),
    ]

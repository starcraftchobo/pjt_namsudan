# Generated by Django 4.2.16 on 2024-11-19 06:13

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
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.IntegerField()),
                ('fin_co_no', models.IntegerField()),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField()),
                ('dcls_strt_day', models.IntegerField()),
                ('dcls_end_day', models.IntegerField()),
                ('fin_co_subm_day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSavings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=50)),
                ('product', models.TextField()),
                ('mtrt', models.FloatField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('max_limit', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('savings_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.savingproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
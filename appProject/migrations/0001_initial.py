# Generated by Django 3.0.5 on 2020-05-02 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cif', models.CharField(max_length=10)),
                ('nombre_empresa', models.CharField(max_length=20)),
                ('datos_contacto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_referencia', models.IntegerField()),
                ('nombre_modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=20)),
                ('precio', models.FloatField()),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
                ('tipo_componente', models.ManyToManyField(to='appProject.Componente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_referencia', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('cantidad_producto', models.IntegerField()),
                ('precio_total', models.FloatField()),
                ('datos_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProject.Cliente')),
                ('producto_solicitado', models.ManyToManyField(to='appProject.Producto')),
            ],
        ),
    ]

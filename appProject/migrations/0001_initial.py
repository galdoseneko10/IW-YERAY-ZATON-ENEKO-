# Generated by Django 3.0.5 on 2020-04-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cif', models.CharField(max_length=50)),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('datos_contacto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_referencia', models.IntegerField()),
                ('nombre_modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('tipo_componente', models.ManyToManyField(to='appProject.Componentes')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_referencia', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('cantidad_producto', models.IntegerField()),
                ('precio_total', models.IntegerField()),
                ('datos_cliente', models.ManyToManyField(to='appProject.Cliente')),
                ('producto_solicitado', models.ManyToManyField(to='appProject.Productos')),
            ],
        ),
    ]

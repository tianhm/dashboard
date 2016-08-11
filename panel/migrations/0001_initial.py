# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('url', models.CharField(max_length=128, verbose_name='地址')),
                ('type', models.CharField(choices=[('交易', '交易'), ('行情', '行情')], max_length=16, verbose_name='类型')),
                ('operator', models.CharField(choices=[('电信', '电信'), ('联通', '联通')], max_length=16, verbose_name='运营商')),
            ],
            options={
                'verbose_name_plural': '前置地址集合',
                'verbose_name': '前置地址',
            },
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('contract_type', models.CharField(choices=[('股票', '股票'), ('期货', '期货'), ('期权', '期权')], max_length=32, verbose_name='市场')),
                ('identify', models.CharField(max_length=32, verbose_name='唯一标志')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('market_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='market_address', to='panel.Address')),
                ('trade_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_address', to='panel.Address')),
            ],
            options={
                'verbose_name_plural': '券商集合',
                'verbose_name': '券商',
            },
        ),
        migrations.CreateModel(
            name='DailyBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('上期所', '上期所'), ('大商所', '大商所'), ('郑商所', '郑商所'), ('中金所', '中金所')], max_length=8, verbose_name='交易所')),
                ('code', models.CharField(max_length=8, verbose_name='合约代码')),
                ('time', models.DateField(verbose_name='时间')),
                ('open', models.FloatField(verbose_name='开盘价')),
                ('high', models.FloatField(verbose_name='最高价')),
                ('low', models.FloatField(verbose_name='最低价')),
                ('close', models.FloatField(verbose_name='收盘价')),
                ('volume', models.IntegerField(verbose_name='成交量')),
                ('open_interest', models.IntegerField(verbose_name='持仓量')),
            ],
            options={
                'verbose_name_plural': '日K线集合',
                'verbose_name': '日K线',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('上期所', '上期所'), ('大商所', '大商所'), ('郑商所', '郑商所'), ('中金所', '中金所')], max_length=8, verbose_name='交易所')),
                ('product_code', models.CharField(max_length=16, unique=True, verbose_name='品种代码')),
                ('all_inst', models.CharField(max_length=32, verbose_name='合约月份汇总')),
                ('main_code', models.CharField(max_length=16, verbose_name='主力合约')),
                ('last_main', models.CharField(max_length=16, verbose_name='上个主力合约')),
                ('change_time', models.DateTimeField(verbose_name='切换时间')),
            ],
            options={
                'verbose_name_plural': '合约集合',
                'verbose_name': '合约',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ref', models.CharField(max_length=13, verbose_name='报单号')),
                ('instrument', models.CharField(max_length=8, verbose_name='品种代码')),
                ('front', models.IntegerField(verbose_name='前置编号')),
                ('session', models.IntegerField(verbose_name='会话编号')),
                ('price', models.FloatField(verbose_name='报单价格')),
                ('direction', models.CharField(choices=[('多', '多'), ('空', '空')], max_length=8, verbose_name='方向')),
                ('offset_flag', models.CharField(choices=[('买开', '买开'), ('卖平', '卖平'), ('卖开', '卖开'), ('买平', '买平')], max_length=8, verbose_name='开平')),
                ('status', models.CharField(choices=[('0', '全部成交'), ('1', '部分成交还在队列中'), ('2', '部分成交不在队列中'), ('3', '未成交还在队列中'), ('4', '未成交不在队列中'), ('5', '撤单'), ('a', '未知'), ('b', '尚未触发'), ('c', '已触发')], max_length=16, verbose_name='状态')),
                ('send_time', models.DateTimeField(verbose_name='发送时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Broker')),
            ],
            options={
                'verbose_name_plural': '报单集合',
                'verbose_name': '报单',
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Broker')),
            ],
            options={
                'verbose_name_plural': '策略集合',
                'verbose_name': '策略',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('上期所', '上期所'), ('大商所', '大商所'), ('郑商所', '郑商所'), ('中金所', '中金所')], max_length=8, verbose_name='交易所')),
                ('instrument', models.CharField(max_length=8, verbose_name='品种代码')),
                ('direction', models.CharField(choices=[('多', '多'), ('空', '空')], max_length=8, verbose_name='方向')),
                ('open_time', models.DateTimeField(verbose_name='开仓日期')),
                ('close_time', models.DateTimeField(blank=True, null=True, verbose_name='平仓日期')),
                ('shares', models.IntegerField(blank=True, verbose_name='手数')),
                ('filled_shares', models.IntegerField(blank=True, null=True, verbose_name='已成交手数')),
                ('avg_entry_price', models.FloatField(verbose_name='持仓均价')),
                ('avg_exit_price', models.FloatField(blank=True, null=True, verbose_name='平仓均价')),
                ('profit', models.FloatField(verbose_name='持仓盈亏')),
                ('frozen_margin', models.FloatField(verbose_name='冻结保证金')),
                ('cost', models.FloatField(verbose_name='手续费')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Broker')),
                ('close_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='close_order', to='panel.Order')),
                ('open_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='open_order', to='panel.Order')),
                ('strategy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.Strategy')),
            ],
            options={
                'verbose_name_plural': '交易记录集合',
                'verbose_name': '交易记录',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='strategy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.Strategy'),
        ),
    ]

# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EndingPeriodBudget.ending_amount'
        db.alter_column(u'daily_expenses_endingperiodbudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'DailyExpense.to_transaction_sum'
        db.alter_column(u'daily_expenses_dailyexpense', 'to_transaction_sum', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'DailyExpense.amount'
        db.alter_column(u'daily_expenses_dailyexpense', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'Cash.amount'
        db.alter_column(u'daily_expenses_cash', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'BeginningPeriodBudget.beginning_amount'
        db.alter_column(u'daily_expenses_beginningperiodbudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'DailyBudget.beginning_amount'
        db.alter_column(u'daily_expenses_dailybudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'DailyBudget.ending_amount'
        db.alter_column(u'daily_expenses_dailybudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'PeriodBudget.beginning_amount'
        db.alter_column(u'daily_expenses_periodbudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'PeriodBudget.ending_amount'
        db.alter_column(u'daily_expenses_periodbudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'EndingDailyBudget.ending_amount'
        db.alter_column(u'daily_expenses_endingdailybudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'BeginningDailyBudget.beginning_amount'
        db.alter_column(u'daily_expenses_beginningdailybudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'TotalDailyExpenses.amount'
        db.alter_column(u'daily_expenses_totaldailyexpenses', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'PeriodExpense.amount'
        db.alter_column(u'daily_expenses_periodexpense', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'Transaction.period_budget'
        db.alter_column(u'daily_expenses_transaction', 'period_budget', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'Transaction.daily_budget'
        db.alter_column(u'daily_expenses_transaction', 'daily_budget', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'Transaction.amount'
        db.alter_column(u'daily_expenses_transaction', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

        # Changing field 'Transaction.daily_expense_id'
        db.alter_column(u'daily_expenses_transaction', 'daily_expense_id', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=8))

    def backwards(self, orm):

        # Changing field 'EndingPeriodBudget.ending_amount'
        db.alter_column(u'daily_expenses_endingperiodbudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'DailyExpense.to_transaction_sum'
        db.alter_column(u'daily_expenses_dailyexpense', 'to_transaction_sum', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'DailyExpense.amount'
        db.alter_column(u'daily_expenses_dailyexpense', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'Cash.amount'
        db.alter_column(u'daily_expenses_cash', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'BeginningPeriodBudget.beginning_amount'
        db.alter_column(u'daily_expenses_beginningperiodbudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'DailyBudget.beginning_amount'
        db.alter_column(u'daily_expenses_dailybudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'DailyBudget.ending_amount'
        db.alter_column(u'daily_expenses_dailybudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'PeriodBudget.beginning_amount'
        db.alter_column(u'daily_expenses_periodbudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'PeriodBudget.ending_amount'
        db.alter_column(u'daily_expenses_periodbudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'EndingDailyBudget.ending_amount'
        db.alter_column(u'daily_expenses_endingdailybudget', 'ending_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'BeginningDailyBudget.beginning_amount'
        db.alter_column(u'daily_expenses_beginningdailybudget', 'beginning_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'TotalDailyExpenses.amount'
        db.alter_column(u'daily_expenses_totaldailyexpenses', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'PeriodExpense.amount'
        db.alter_column(u'daily_expenses_periodexpense', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'Transaction.period_budget'
        db.alter_column(u'daily_expenses_transaction', 'period_budget', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'Transaction.daily_budget'
        db.alter_column(u'daily_expenses_transaction', 'daily_budget', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'Transaction.amount'
        db.alter_column(u'daily_expenses_transaction', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'Transaction.daily_expense_id'
        db.alter_column(u'daily_expenses_transaction', 'daily_expense_id', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'daily_expenses.beginningdailybudget': {
            'Meta': {'object_name': 'BeginningDailyBudget'},
            'beginning_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.beginningperiodbudget': {
            'Meta': {'object_name': 'BeginningPeriodBudget'},
            'beginning_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.cash': {
            'Meta': {'object_name': 'Cash'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.dailybudget': {
            'Meta': {'object_name': 'DailyBudget'},
            'beginning_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'ending_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.dailyexpense': {
            'Meta': {'object_name': 'DailyExpense'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_transaction_sum': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.datepicker': {
            'Meta': {'object_name': 'DatePicker'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.endingdailybudget': {
            'Meta': {'object_name': 'EndingDailyBudget'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'ending_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.endingperiodbudget': {
            'Meta': {'object_name': 'EndingPeriodBudget'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'ending_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.periodbudget': {
            'Meta': {'object_name': 'PeriodBudget'},
            'beginning_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'ending_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.periodexpense': {
            'Meta': {'object_name': 'PeriodExpense'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.totaldailyexpenses': {
            'Meta': {'object_name': 'TotalDailyExpenses'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'daily_expenses.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'daily_budget': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'daily_expense_id': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_budget': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '8'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['daily_expenses']
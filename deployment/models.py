# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from utilities.djangohelper import ListField

# Create your models here.
class Cluster (models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50, default='')
    created = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    addrs = ListField(null=True)
    systems = ListField(null=True)

    def genManagement(self, name, path='', port=0):
        if port:
            url = 'http://%s:%d%s' % (self.addrs[0], port, path)
        else:
            url = 'http://%s%s' % (self.addrs[0], path)

        return {
            'name': name,
            'url': 'http://www.baidu.com'
        }

    def managements(self):
        if not self.addrs:
            return []
        managements =  [
            self.genManagement(name='日志管理', port=5601),
            self.genManagement(name='Ganglia', path='/ganglia'),
            {
                'name': '优化与诊断',
                'subitems': [
                    self.genManagement(name='日志诊断', port=5000),
                    self.genManagement(name='参数优化', port=5001)
                ]
            }
        ]
        if 'HDFS' in self.systems:
            managements.append(self.genManagement(name='HDFS', port=50070))
        if 'Spark' in self.systems:
            managements.append(self.genManagement(name='Spark History', port=18080))
        if 'MapReduce' in self.systems:
            managements.append(self.genManagement(name='YARN', port=8088))
        return managements
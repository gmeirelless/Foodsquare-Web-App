from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
                         host(r'manager', 'manager.urls', name='manager'),
                         host(r'delivery', 'delivery.urls', name='delivery'),
                         host(r'admin', 'webAdmin.urls', name='webAdmin'),
                         host(r'www', settings.ROOT_URLCONF, name='www'),
                         ) 

from distutils.core import setup

setup(name='bloom',
     version='0.1',
     description='Mobile pluggable applications for Django.',
     author='Handi Mobility Inc.',
     author_email='team@handimobility.ca',
     url='http://code.google.com/p/django-bloom/',
     packages=['bloom', 'bloom.device', 'bloom.device.templates', 'bloom.ad', 'bloom.ad.templatetags', 'bloom.image', 'bloom.image.templatetags', 'bloom.share', 'bloom.share.templates', 'bloom.sms', 'bloom.sms.lib', 'bloom.sms.lib.upside', 'bloom.track', 'bloom.user', 'bloom.utils'],
     classifiers=['Development Status :: 4 - Beta',
                  'Environment :: Web Environment',
                  'Intended Audience :: Developers',
                  'License :: OSI Approved :: GNU General Public License v3',
                  'Operating System :: OS Independent',
                  'Programming Language :: Python',
                  'Topic :: Utilities'],
     )

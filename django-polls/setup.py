import os 
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
    os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
    setup(
        name='django-polls',
        version='0.1',
        packages=find_packages(),
        include_package_data=True,
        license='BSD License',
        description='A simple Django app to conduct web-based polls.',
        long_description=README,
        url='https://www.example.com/',
        author='d_uchida',
        author_email='d_uchida@example.com',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: 2.1.3',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operatiing System :: OS Independet',
            'Programming Language :: Python :: 3.6.5',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
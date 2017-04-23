from setuptools import setup, find_packages

version = '0.0.1'
long_description = ""

setup(name='asnlookup-web',
      version=version,
      description="ASN http ui",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ASN',
      author='Justin Azoff',
      author_email='justin@bouncybouncy.net',
      url='',
      license='MIT',
      py_modules=['asnlookup_web'],
      include_package_data=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "asnlookup-client",
          "flask",
      ],
      entry_points = {
        'console_scripts': [
            'asnlookup-web   = asnlookup_web:main',
        ]
      },
  )

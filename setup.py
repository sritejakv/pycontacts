from setuptools import setup, find_packages

setup(
        name='py-contacts',
        version='1.0',
        description='Contacts storage application',
        author='Sriteja Kummita',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'pycontacts = contacts.pycontacts:main',
            ]
        },
        install_requires=[
            'argparse',
        ]
      )

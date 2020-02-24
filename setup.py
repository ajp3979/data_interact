
from setuptools import find_packages
from setuptools import setup

import versioneer

setup(
    name='data_interact',
    description='An app for interacting with data via Pandas.',
    author='Andrew Pritchett',
    url='http://expel.io',
    license='Proprietary',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points={'console_scripts': [
        'data_interact = data_interact.data_interact:main']},
    packages=find_packages(),
    install_requires=[
    ],
    # Do not zip the installed egg.
    zip_safe=False,
    include_package_data=True,
)
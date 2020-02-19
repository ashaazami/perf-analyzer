from setuptools import find_packages
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

setup(
    name='performance',
    version='1.0.0',
    description="Module to instrument a python code and visualize the call patterns",
    long_description=readme + '\n\n',
    author="Ashkan Aazami",
    author_email='aazami@gmail.com',
    url='https://github.com/ashaazami/performance',
    packages=find_packages(),
    package_dir={'perf_loger': 'perf_loger'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords=['perf'],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ]
)

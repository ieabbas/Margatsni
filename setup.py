from setuptools import setup, find_packages

setup(
    name='Margatsni',
    version='1.0',
    author='Solid State Group',
    packages=find_packages(),
    py_modules = ['app'],
    zip_safe=False,
    install_requires=['flask', 'flask_sqlalchemy']
)
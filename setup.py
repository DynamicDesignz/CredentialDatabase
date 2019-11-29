from setuptools import setup, find_packages

from BreachCompilationRestAPI import __version__, __author__, __email__, __license__

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", encoding='utf-8') as f:
    readme = f.read()

with open("CHANGELOG.rst") as f:
    changelog = f.read()

setup(
    name="CredentialDatabase",
    version=__version__,
    description="creates a massive credential database",
    long_description=readme + "\n\n" + changelog,
    license=__license__,
    author=__author__,
    author_email=__email__,
    url="https://github.com/bierschi/BreachCompilationRestAPI",
    packages=find_packages(),
    data_files=[
        ('/etc/systemd/system', ['service/BreachCompilationApp.service'])
    ],
    package_data={'BreachCompilationRestAPI': ['config/*']},
    install_requires=required,
    keywords=["BreachCompilation", "credentials", "leaked", "database"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={
        "console_scripts": [
            'BreachCompilationApp = BreachCompilationRestAPI.app:main',
            'BreachCompilationDatabase = CredentialDatabase.breachcompilation.BreachCompilationDatabase:main',
            'PasswordDatabase = CredentialDatabase.PasswordDatabase:main'
        ],
    },
    zip_safe=False,
)

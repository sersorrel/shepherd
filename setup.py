from setuptools import setup

setup(
    name="shepherd",
    version="0.1",
    packages=["shepherd"],

    install_requires=[
        "Flask",
        "enum34 ; python_version < '3.4'",
        "pytz",
    ],

    author="Ash Holland",
    author_email="ash@sorrel.sh",
)

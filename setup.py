from setuptools import setup

VERSION = "1.3.0"

install_requires = [
    "pygelf>=0.4.1"
]

setup(
    name="muselog",
    version=VERSION,
    description="themuse.com log utilities",
    zip_safe=False,

    packages=["muselog"],

    install_requires=install_requires
)

from setuptools import find_packages, setup


setup(
    name="p2",
    version="1.0.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    author="Isaac Murchie",
    author_email="isaac.murchie@benevolent.ai",
    description="Package Two",
)

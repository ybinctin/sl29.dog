from setuptools import setup, find_packages

setup(
    name="sl29.dog",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Yves Cadour",
    author_email="yves.cadour@saint-louis29.net",
    description="Un projet pour enseigner la POO en Python avec une classe Dog",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/saintlouis29/sl29.dog",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
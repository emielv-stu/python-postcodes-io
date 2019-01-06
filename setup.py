import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postcodes-io-simple",
    version="0.0.1",
    author="Rohit Deshmukh",
    author_email="raigad1630@gmail.com",
    description="A Python Wrapper for postcodes.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raigad/python-postcodes-io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

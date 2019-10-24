import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textprocessing-omar-zaki",
    version="0.0.1",
    author="Omar Zaki",
    author_email="omartawba1@gmail.com",
    description="A text processor package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omartawba1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

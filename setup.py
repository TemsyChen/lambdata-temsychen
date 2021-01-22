import setuptools

REQUIRED = ["numpy", "pandas"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_temsychen", # Replace with your own username
    version="0.0.2",
    author="temsychen",
    author_email="temsy.chen@gmail.com",
    description="A collection of data science functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TemsyChen/lambdata-temsychen",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
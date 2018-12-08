import setuptools

setuptools.setup(
    name="raspi_thermometer",
    version="0.1dev",
    author="Doug Ollerenshaw",
    author_email="d.ollerenshaw@gmail.com",
    description="temperature logger for raspberry pi",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
print('setup')
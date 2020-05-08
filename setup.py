import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="erede-python",
    version="1.0.0",
    author="Developers Rede",
    description="SDK Python Rede",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevelopersRede/erede-python",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

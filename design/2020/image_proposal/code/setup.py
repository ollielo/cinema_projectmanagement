import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cinemagic",
    version="1.0",
    author="David H. Rogers",
    author_email="dhr@lanl.gov",
    description="Tools for the Cinema scientific toolset.",
    url="https://github.com/cinemascience",
    packages=["cinemagic"],
    scripts=["cinema"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD",
        "Operating System :: OS Independent",
    ],
)

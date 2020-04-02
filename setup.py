import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="buxfer",
    version="0.0.0",
    author="Jacques Beukes",
    author_email="jpbeukes27@gmail.com",
    description="Python API for Buxfer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JPBeukes/buxfer",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

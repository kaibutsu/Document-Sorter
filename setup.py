import setuptools
import os

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="document_sorter",
    version="0.0.1",
    description="Sorts documents according to filename, metadata and content.",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Sven (github.com/kaibutsu)",
    packages=["document_sorter"],
    install_requires=install_requires,
)

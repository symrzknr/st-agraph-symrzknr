import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# python setup.py sdist bdist_wheel
# twine upload  dist/*

setuptools.setup(
    name="st-agraph-symrzknr",
    version="0.0.40",
    author="symrzknr",
    author_email="mrevuelta.deca@gmail.com",
    description="Interactive Graph Vis for Streamlit, forked from original",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/symrzknr/st-agraph-symrzknr",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "networkx >= 2.5",
    ],
)

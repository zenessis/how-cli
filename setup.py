from how import __version__, __author__
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().strip().splitlines()

setup(
    name="how-cli",
    version=__version__,
    description="An AI-based CLI assistant to help you with command line & shell.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zenessis/how-cli",
    project_urls={
        "Issue Tracker": "https://github.com/zenessis/how-cli/issues",
    },
    author=__author__,
    author_email="guptashiv018@gmail.com",
    platforms="any",
    license="",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "how=how.how:app",
        ]
    }
)

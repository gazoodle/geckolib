import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geckolib-gazoodle",
    version="0.3.9.3",
    author="Gazoodle",
    author_email="gazoodle@hash.fyi",
    description="A library to interface with Gecko Alliance products using in.touch2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gazoodle/geckolib",
    packages=setuptools.find_packages("src/"),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"": "src"},
    license="GPLv3",
)
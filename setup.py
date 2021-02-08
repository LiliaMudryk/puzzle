import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Puzzle",
    version = "0.0.1",
    author = "Lilia Mudryk",
    author_email = "liliia.mudryk@ucu.edu.ua",
    description= "A package to check if puzzle game board is ready to start the game",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url =" ",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Licence",
        "Operating System :: OS Independent",
    ],
    python_requires ='>=3.8'   
)
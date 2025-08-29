from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements = []
    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                req = line.strip()
                if req and req != "-e ." and not req.startswith("#"):
                    requirements.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements
setup(
    name="Project_2",
    version="0.1.0",
    author="Anshul Patel",
    author_email="anshulpatel1905@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

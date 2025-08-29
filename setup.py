from setuptools import setup, find_packages

def get_requirements(file_path: str):
    """
    Reads requirements file and returns a list of dependencies.
    Ignores comments, empty lines, and '-e .' entries.
    """
    requirements = []
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#") and line != "-e .":
                requirements.append(line)
    return requirements

setup(
    name="news_recommender",
    version="0.1.0",
    author="Viplav Singh",
    author_email="viplavs2004@gmail.com",
    description="A personalized news recommendation system",
    packages=find_packages(where="."),  # root folder, not src
    package_dir={"": "."},              # look in root dir
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)

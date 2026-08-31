from setuptools import setup, find_packages

setup(
    name="journal-app",
    version="0.2.0",
    description="A habit-focused daily journal covering relationships, learning, money, and health",
    author="Damian Garcia",
    packages=find_packages(),
    install_requires=[
        "click>=8.1",
    ],
    entry_points={
        "console_scripts": [
            "journal=journal.cli:cli",
        ],
    },
    python_requires=">=3.6",
)

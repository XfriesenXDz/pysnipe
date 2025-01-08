# setup.py

from setuptools import setup, find_packages

setup(
    name="pysnipe",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyautogui',
        'opencv-python',
        'numpy',
    ],
    author="Sniper",
    author_email="vipzzpvp@gmail.com",
    description="A library for recording screen and some features.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/XfriesenXDz/pysnipe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

from os import path
from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dvdss",
    version="1.0.0",
    packages=["dvdss"],
    description="DVD ScreenSaver with XScreenSaver and Tkinter ",
    long_description=long_description,
    url="https://github.com/adlgrbz/dvdss",
    author="Adil Gürbüz",
    author_email="adlgrbz@tutamail.com",
    platforms=["Linux"],
    keywords="tkinter xscreensaver dvd screensaver",
    package_data={"dvdss": ["data/*.*"]},
    entry_points={"console_scripts": ["dvdss = dvdss.screensaver:main"]},
)



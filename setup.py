from setuptools import setup

setup(
    name="runner",
    version="1.1",
    description="Task runner",
    author="Chris AtLee",
    author_email="chris@atlee.ca",
    py_modules=["runner"],
    entry_points={
        "console_scripts": ["runner = runner:main"],
    },
    url="https://github.com/catlee/runner",
    setup_requires=["nose==1.3.1"],
)

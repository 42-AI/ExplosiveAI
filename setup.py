# from distutils.core import setup
# # setup(name='gym_42ai',
# #       version='1.0',
# #       py_modules=['gym_42ai'],
# #       )

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bomberman",
    version="0.1.0",
    description='42AI gym environment for Bomberman!',
    long_description=long_description,
    long_description_content_type="text/markdown",
	author='42AI',
	author_email='contact@42ai.fr',
	url='https://www.42ai.fr/',


    install_requires=[
		"setuptools>=42",
		"colorama >= 0.4.4",
		"matplotlib >= 3.5.1",
		"wheel",
	],
	python_requires='>=3.8',



    project_urls={
        "Bug Tracker": "https://github.com/42-AI/ExplosiveAI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "gym_42ai"},
    packages=setuptools.find_packages(where="gym_42ai"),
)

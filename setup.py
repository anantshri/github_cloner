#coding:utf-8

from setuptools import setup, find_packages

setup(	name="Github Cloner",
		version="0.1",
		packages=find_packages(),
		install_requires=[ 'GitPython==0.3.6', 'requests==2.6.0' ],
		entry_points={
			'console_scripts': [ 'ghclone = src.github_clone_user:main']
						},
		author="Anantshri",
		author_email="anant@anantshri.info",
		description="Tool to clone any users Github repos.",
		license=open('LICENSE').read()
		)

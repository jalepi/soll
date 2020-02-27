import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='soll',
    version='0.0.1',
    description='Python HTTP POST method invoker',
    author='jalepi',
    author_email='jalepi@live.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jalepi/soll',
    packages=['soll.api'],
    install_requires=[
        'flask',
        'tornado',
    ],
)
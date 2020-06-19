import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='cobry',
    version='0.0.1',
    author='Jan Larwig',
    author_email='jan@larwig.com',
    description='Yet another command line interface toolkit to built versatile and modern CLI applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tuunit/cobry',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)

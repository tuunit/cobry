from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cobry',
    version = '0.1.0',
    author = 'Jan Larwig',
    author_email = 'jan@larwig.com',
    license='MIT License',
    url='https://github.com/tuunit/cobry',
    description='Yet another command line interface toolkit to built versatile and modern CLI applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    install_requires = [],
    python_requires='>=3.0',
    packages=['cobry']
)

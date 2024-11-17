from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='spotifystl',
    version='0.1.0',
    author='Nicolás García Sastre',
    author_email='n.garcia.sastre@gmail.com',
    description='This code generates STL objects that can be used to 3D print Spotify codes in multiple colors.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NikoConn/spotify-stl-generator',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='==3.10.*',
)
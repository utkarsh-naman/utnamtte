from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3'
]

setup(
    name='utnamtte',
    version='0.0.1',
    description='A better eval function, eg 2π = 2*math.pi',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/utkarsh-naman/MATEX',
    author='Utkarsh Naman',
    author_email='its.utnam@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='eval calculator text-to-expression',
    packages=find_packages(),
    install_requires=['']
)
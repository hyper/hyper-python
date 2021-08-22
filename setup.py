from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='hyper',
    version='0.0.1',
    author='Hyper',
    author_email='support@hyper.co',
    description='Python library for the Hyper API.',
    long_description=long_description,
    long_description_content_type='',
    license='MIT',
    url='https://github.com/meta-labs/hyper-python',
    project_urls={
        "Documentation": "https://docs.hyper.co/reference",
        "Source Code": "https://github.com/meta-labs/hyper-python",
    },
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(include=['hyper']),
    python_requires=">=3.0",
)

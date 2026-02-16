from setuptools import setup, find_packages

setup(
    name='contentclaw',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'contentclaw=contentclaw.generator:main',
        ],
    },
    author='Ash OpenClaw',
    description='AI Content Generation Toolkit'
)
from setuptools import setup, find_namespace_packages

setup(
    name='contentclaw',
    version='0.2.0',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'contentclaw=contentclaw.__main__:main',
        ],
    },
    author='Ash OpenClaw',
    description='AI-Powered Content Generation Toolkit'
)
from setuptools import setup, find_packages

setup(
    name='contentclaw',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai',
        'requests',
        'pandas',
        'tiktok-api',  # Placeholder for actual TikTok API
        'brave-search-api'
    ],
    extras_require={
        'dev': ['pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'contentclaw=contentclaw.main:main',
        ],
    },
    author='Ash OpenClaw',
    author_email='ashopenclaw@proton.me',
    description='AI-Powered Content Generation Toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
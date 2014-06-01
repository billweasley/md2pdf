# coding=utf8


from setuptools import setup
from md2pdf import __version__


setup(
    name='md2pdf',
    version=__version__,
    author='hit9',
    author_email='nz2324@126.com',
    description='Convert single markdown file to pdf.',
    license='BSD',
    keywords='markdown pdf',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'md2pdf=md2pdf.cli:main'
        ]
    },
    install_requires=open("requirements.txt").read().splitlines(),
    packages=['md2pdf']
)

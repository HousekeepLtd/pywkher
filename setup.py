from setuptools import setup

setup(
    name='pywkher',
    version='1.0.6',
    url='https://github.com/jwmayfield/pywkher',

    author_email='jason@codetalk.rs',
    author='Jason Mayfield',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description='wkhtmltopdf for Python on Heroku',
    install_requires=[
        'Mock>=1.0.1',
    ],
    long_description=open('README.rst').read(),
    packages=['pywkher', ],
    test_suite='tests',
    zip_safe=False
)

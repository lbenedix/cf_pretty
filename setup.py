from distutils.core import setup

setup(
    name='cf_pretty',
    packages=['cf_pretty'],
    version='0.1.3',
    license='MIT',
    description='makes cf cli output more readable',
    author='Lukas Benedix',
    author_email='pypi@l3q.de',
    url='https://github.com/lbenedix/cf_pretty',
    keywords=['CF', 'CLOUD FOUNDRY', 'KEYWORDS'],
    install_requires=[
        'rapidtables',
    ],
    entry_points={
        'console_scripts': ['cf_pretty=cf_pretty:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
    ],
)

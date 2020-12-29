
from distutils.core import setup
setup(
    name='MailMag',
    packages=['MailMag'],
    version='1.0',
    license='MIT',
    description='This library can help you send bulk emails using google spreadsheets',
    author='Rohtansh Sehgal',
    author_email='rohtanshsehgal@gmail.com',
    url='https://github.com/user/reponame',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['Google Spreadsheet', "smtplib", 'Emails'],
    install_requires=["gspread"],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

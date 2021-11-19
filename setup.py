from distutils.core import setup
setup(
  name = 'Login-util',
  packages = ['login-util'],
  version = '0.0.1',
  license='MIT',
  description = 'easy to use python login utility', 
  author = 'LucasAmmer',
  author_email = 'lucas@ammer.nl',
  url = 'https://github.com/lucasammer/login-util', 
  download_url = 'https://github.com/lucasammer/handydandy/archive/refs/tags/0.0.8.tar.gz',
  keywords = ['LOGIN', 'EASY', 'SIMPLE'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
from distutils.core import setup
setup(
  name = 'premath',
  packages = ['premath'],
  version = '0.1',
  license='MIT',
  description = 'This is a library for predictive math.',
  author = 'Iñaki Salcedo',
  author_email = 'isalcedodurston@gmail.com',
  url = 'https://github.com/inakisalcedo/premath',
  download_url = 'https://github.com/inakisalcedo/premath/archive/refs/tags/v_01.tar.gz',
  keywords = ['MATH', 'REGRESSION', 'PREDICTION'],
  install_requires=[
          'numpy',
          'sklearn',
          'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: >= 3',
  ],
)

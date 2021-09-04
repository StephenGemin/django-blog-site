from setuptools import setup

# read the contents of README file
from os import path
current_dir = path.abspath(path.dirname(__file__))
# with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
#     long_desc = f.read()
long_desc = ""
setup(
  name='django-blog-site',
  packages=[''],
  version='0.0.1',
  license='MIT License',
  description='Blog website using Django framework',
  long_description=long_desc,
  long_description_content_type='text/markdown',
  author='Stephen Gemin',
  author_email='s.gemin88@gmail.com',
  url='https://github.com/StephenGemin/django-blog-site',
  download_url='https://github.com/StephenGemin/django-blog-site/',
  extras_require={
          'dev': [
              'pytest',
              'pytest-pep8',
              'pytest-cov'
          ]
  },
  keywords=["django", "blog", "website"],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Debuggers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)

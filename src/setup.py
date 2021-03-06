# setup.py
from distutils.core import setup
import glob, sys, os
import py2exe

mum_path = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path = [mum_path] + sys.path

setup(name="mum",
      scripts=["mum.py"],
      version="1.3.0",
      description="mum - Thumbnail Software",
      author="Gianluigi Calcaterra",
      author_email="gianluigi.calcaterra@gmail.com",
      url="http://www.blog.duea.info/mum/",
      )

from setuptools import setup
import os.path
 

with open(os.path.join(os.path.dirname(__file__), 'thonny', 'VERSION'), encoding="ASCII") as f:
    version = f.read().strip()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NB! Before creating sdist, copy source files required by backend to thonny/backend_private
# See installers/setuptools/create_sdist.bat 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

setup(
      name="thonny",
      version=version,
      description="Python IDE for beginners",
      url="http://thonny.cs.ut.ee",
      author="Aivar Annamaa",
      license="GPLv3",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
      ],
      keywords="IDE education debugger",
      packages=["thonny", "thonny.plugins"],
      package_data={'': ['VERSION',  'res/*', 'backend_private/*.py', 'backend_private/thonny/*.py']},
      entry_points={
        'gui_scripts': [
            'thonny = thonny:launch',
        ]
      },      
)
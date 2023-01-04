from setuptools import setup, find_packages

setup(name='svg2lottie',
      version='1.0.0',
      description='SVG to Lottie converter',
      url='https://github.com/LottieFiles/svg-to-lottie-converter',
      author='LottieFiles',
      author_email='support@lottiefiles.com',
      license='GNU Affero General Public License v3',
      packages=find_packages(include=['svg2lottie', 'svg2lottie.*']),
      install_requires=[
          'numpy == 1.24.0',
          'dataclasses == 0.6',
          'CairoSVG',
          'triangle',
          'pydantic == 1.6.1',
          'matplotlib == 3.3.0',
          'uvicorn == 0.11.6',
          'fastapi == 0.61.0',
      ],
      zip_safe=False)

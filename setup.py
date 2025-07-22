from setuptools import find_packages, setup

setup(
    name='StudentPerformancePredictor',
    version='0.0.1',
    author='Yash',
    author_email='yash@example.com', # Replace with your email
    packages=find_packages(),
    install_requires=['pandas', 'scikit-learn'], # Add any other libraries like numpy here
)
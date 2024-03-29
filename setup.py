from setuptools import find_packages, setup

setup(
    name='fpq_app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'werkzeug', 'attr', 'pytest'
    ],
    setup_requires=[
        'pytest',
    ],
    tests_require=[
        'pytest',
    ],
)

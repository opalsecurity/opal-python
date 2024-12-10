# coding: utf-8

"""
    Opal API

    The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "opal-security"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    description="Opal API",
    author="Opal Team",
    author_email="hello@opal.dev",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Opal API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    long_description_content_type='text/markdown',
    long_description="""\
    The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.
    """,  # noqa: E501
    package_data={"opal_security": ["py.typed"]},
)

import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="twarc-edits",
    version="0.0.1",
    url="https://github.com/docnow/twarc-edits",
    author="Ed Summers",
    author_email="ehs@pobox.com",
    py_modules=['twarc_edits'],
    description="Find edited tweetes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.3",
    install_requires=["twarc"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points="""
        [twarc.plugins]
        edits=twarc_edits:edits
    """,
)

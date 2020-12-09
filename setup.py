from setuptools import setup

VERSION = "2.3.0"

install_requires = [
    "JSON-log-formatter>=0.2.0",
    "ddtrace>=0.22.0",  # This is the minimum version allowed as trace helpers weren't added until 0.22.0
    "typer>=0.3.0"
]

setup(
    name="muselog",
    version=VERSION,
    description="themuse.com log utilities",
    zip_safe=False,

    packages=["muselog"],
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "django": ["Django>=2.2.12"],
        "flask": ["Flask>=1.0.2"],
        "tornado": ["tornado>=4.5.1"],
        "asgi": ["starlette>=0.13.6"]
    },
    entry_points={
        "console_scripts": [
            "muselog-run = muselog.commands.muselog_run:app",
        ],
    },
)

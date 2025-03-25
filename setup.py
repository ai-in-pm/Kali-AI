from setuptools import setup, find_packages

setup(
    name="kaliagent",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'agno>=1.2.3',
        'openai>=1.0.0',
        'python-dotenv>=1.0.0',
        'rich>=13.0.0',
        'pydantic>=2.0.0',
    ],
    entry_points={
        'console_scripts': [
            'kaliagent=kaliagent.cli:main',
        ],
    },
    author="Kali AI Team",
    author_email="contact@kaliagent.sec",
    description="AI-powered Ethical Hacking Assistant for Kali Linux",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords="kali, linux, ethical-hacking, cybersecurity, penetration-testing",
    url="https://github.com/kali-ai/kaliagent",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.8",
)

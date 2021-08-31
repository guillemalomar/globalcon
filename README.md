[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

# GlobalCon Tools

*    Author: Guillem Alomar
*    Initial release: December 12th, 2020
*    Availability: Public

**Index**
* [Documentation](#documentation)
    * [Explanation](#explanation)
* [Using the application](#using-the-application)
    * [Requirements](#requirements)
    * [Installation](#installation)
    * [Using the application](#using-the-application)
    * [Output](#output)
* [Development](#development)
    * [Code style](#code-style)

## Documentation

![alt text][logo2]

[logo2]: documentation/UI.png "ClassificationAutomation"

![alt text][logo3]

[logo3]: documentation/DiplomaExample.png "DiplomaExample"


### Explanation

This project consists in a few tools related to the GlobalCon event. A calculator that will be used to evaluate global
sets in following GlobalCons, and a diploma creator for the competitors in the event.

## Using the application

### Requirements

- Python +3.8

The complete list of packages is available in the file _requirements.txt_

### Installation

I recommend creating a virtualenv for this project:
```bash
# Create the virtual environment
~/globalcon virtualenv -p python3.8 venv

# Activate it (linux/mac)
~/globalcon source venv/bin/activate

# Activate it (windows)
~/globalcon venv/Scripts/activate.bat

# Install the pip packages from the requirements file
(venv) ~/globalcon pip install -r requirements.txt
```
Now all pip packages needed to run the application have been installed.

### Using the application

To obtain the scores, you can run the  _calculate.py_ script like this:
```bash
(venv) ~/globalcon python calculate.py
```

To obtain the diplomas from the score files previously created, you can run the  _calculate.py_ script like this:
```bash
(venv) ~/globalcon python create_diplomas.py
```

### Output

You can check the obtained result files in the _DATA_ folder (the 
folder name can be renamed in _src/\_\_init\_\_.py_).

## Development

### Code style

This project uses [Black](https://github.com/psf/black) to lint the files
automatically and provide an uniform look and let devs worry about what really
matters: writing code that solves problems.

It also makes use of [pre-commit](https://pre-commit.com/), a framework for
managing and maintaining pre-commit hooks. It has a pre-commit hook that
automatically runs Black. To install it, just do:

```bash
pip install -r requirements-dev.txt
pre-commit install
```

This will install the corresponding git pre-commit hooks which will be run in
your next commit of Python files.

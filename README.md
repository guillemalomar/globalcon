[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

# GlobalCon Tools

*    Author: Guillem Alomar
*    Initial release: December 12th, 2020
*    Availability: Public

**Index**
* [Documentation](#documentation)
    * [Explanation](#explanation)
    * [Must Read](#must-read)
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

![alt text][logo4]

[logo4]: documentation/GlobalSetList_Example.png "GlobalsetListExample"


### Explanation

This project consists in a few tools related to the GlobalCon event:
- A calculator that will be used to evaluate global sets in following GlobalCons.
- A diploma creator for the competitors in the event.
- A global set list creator.

### Must Read

The GlobalSet List Generator must be updated from time to time if the card to process has recent reprints.
There might be expansions which haven't been added yet, which will result in an error when generating the list.
To avoid this, it's as easy as adding that new set to the file globalcon_tools/globalset_list/specifications.py file,
together with its available languages. Feel free to create a PR with the newly added sets :)
Also, the rarities list is not exact, as rarities such as playtests or testprints are very specifical to each card.

Finally, the weights applied to each field in the calculator are not final, the GlobalCon organizers might make changes
in the future, or give extra points during a GlobalCon to participants showing their Global Sets :)

## Using the application

### Requirements

- Python +3.7

The complete list of packages is available in the file _requirements.txt_

### Installation

I recommend creating a virtualenv for this project:
```bash
# Create the virtual environment
~/globalcon virtualenv -p python3.7 venv

# Activate it (linux/mac)
~/globalcon source venv/bin/activate

# Activate it (windows)
~/globalcon venv/Scripts/activate.bat

# Install the pip packages from the requirements file
(venv) ~/globalcon pip install -r requirements.txt
```
Now all pip packages needed to run the application have been installed.

### Using the application

To start the application:
```bash
(venv) ~/globalcon python globalcon.py
Please enter the desired tool to use:
1 - Calculate Score
2 - Generate Diplomas
3 - Generate Globalset List
```

### Output

You can check the obtained result files in the _DATA_ folder (the 
folder name can be renamed in _globalcon_tools/\_\_init\_\_.py_).

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

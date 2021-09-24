# init-tox

This repository aims to introduce the tox automation project standarizing testing in Python and how to work with such a complete automation CI system workflow.

## Objective

Create a develop, build, test, and deploy workflow based on tox from scratch.

## What is tox?

Is a generic "virtualenv" management and test command line tool you can use for:
* checking environments and dependencies required
* running your tests
* acting as a frontend to continuos integration servers

>Note: [tox documentation](https://tox.readthedocs.io/en/latest/)

## Getting started

On your python environment set the tox tool via `pip install tox`

>Note: this repo used the 6.2.4 tox version

## Config

    $ tox --showconfig

Shows basically the objects (environments) in the configuration.

Also will show up what kind of variables you might set when configuring an environment.

For seeing verbosity

    $ tox -vvvvvv

first 3vs are for tox and the rest for pip

Run commands as part of your `toxrun` to give you more information

Run `tox` programmatically and attach a debugger to the process (see [tox developer faq](https://tox.readthedocs.io/en/latest/developers.html))

If you dont set `envlist` it will run all environments by default.
But you can specify which ones tox should run, listing them in that variable.


to see the environments declared, the default and the additional

    $ tox -av

to recreate the environments inside .tox/

    $ tox --recreate (tox -r (in short form))


You can use subsitutions like {envpython} to refer specific tox variables

## setup.py
Describes how our python code should be packaged.

## usedevelop
Install the current package in development mode with "setup.py develop" using symbolic links to the source folder not copying all the stuff

## Activate

You may activate specific environments to work with them and to not run again tox (to recreate)

cuz maybe you prefer to install manually some packages

    $ .tox/{environment_name}/scripts/bin/activate
    $ pip install {package or module}
    $ pip install -e . (for own packages set in the actual pwd)

## Notes

[tox] -> basic top level section to specify whats globally available
envlist -> key which environments the test will run

[testenv] -> basic section for specific commands
          -> list the commands you wanna use to test ur library/project and the dependencies that should be installed

// tox will manage to setup the environment and install all the dependencies listed to be added
// inside .tox will be created the virtual environments tested when running tox.ini (tox)


## Linting: Black

    $ tox -e black
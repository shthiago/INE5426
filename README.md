# INE5426

# Usage requirements

You need to have [`virtualenv`](https://pypi.org/project/virtualenv/) installed, using `pip` compatible with `python=^3.8`.

# Setup

Run `make setup` to createthe environment. A virtual environment will be created using `virtualenv` in `./venv` folder. To activate it manually, you can run `source venv/bin/activate`, but using the `make run` command, it is used by default.

# Executing

Run `make run filepath=<source/code/file/path>`. If you run `make run` without setting up a `filepath`, the `examples/exemplo1.ccc` will be used.
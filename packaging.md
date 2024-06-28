# Packaging reminder

This package is composed by the modified (json output) 6s Fortan code and the python wrapper.
The goal is to have the package available on conda-forge for linux, osx and windows.


## conda-forge

conda-forge take care of the packaging for linux, osx and windows so that we don´t have to (see [conda-forge](https://conda-forge.org/docs/user/introduction/)).

## PyPi
Build the package with the following command:

```bash
python -m build
```

Check it's content in the archive and then upload it to PyPi with the following command:

```bash
twine upload -r pypi dist/*
```

## Conda
Build the package with the following command:

```bash
conda build .
```

convert it to other platforms with the following command:

```bash
conda convert --platform all <path_to_package> -o ~/output
```

upload it to the conda channel with the following command:

```bash
anaconda upload <path_to_package>
```
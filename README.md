# sixs_json
The 6S code but with JSON output for easier parsing.

# Packaging reminder

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
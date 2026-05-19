## primepackage

`primepackage` is a small Python package for demonstrating a Poetry-managed
project. It includes simple utilities for working with prime numbers and for
writing generated prime numbers to a CSV file.

The package can:

- check whether an integer is prime
- generate the first `n` prime numbers
- write a list of prime numbers to a CSV file
- read prime numbers back from a CSV file
- run a command-line script that generates the first 100 prime numbers

## Project Structure

```text
src/primepackage/
  __init__.py
  generator.py
  primeio.py
  primemodule.py
tests/
  test_is_prime.py
pyproject.toml
poetry.lock
```

## Installation

This project uses [Poetry](https://python-poetry.org/) for packaging and
dependency management.

```bash
poetry install
```

## Usage

Run the command-line script:

```bash
poetry run myprimes
```

The script generates the first 100 prime numbers, writes them to `output.csv`,
then reads the file and prints the list.

You can also use the package from Python:

```python
from primepackage import get_n_prime, is_prime, read_primes, write_primes

print(is_prime(83))

primes = get_n_prime(10)
write_primes(primes, "output.csv")
print(read_primes("output.csv"))
```

## Development

Run the test suite with:

```bash
poetry run pytest
```

Format code with:

```bash
poetry run black src tests
```

## License

This project is licensed under the terms in `LICENSE`.

import csv

import pytest

from primepackage import get_n_prime, is_prime, read_primes, write_primes
from primepackage.generator import main


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (8, False),
        (83, True),
        (97, True),
        (100, False),
    ],
)
def test_is_prime_identifies_prime_and_composite_numbers(number, expected):
    assert is_prime(number) is expected


@pytest.mark.parametrize("invalid_number", [0, -1, 3.14, "Hello"])
def test_is_prime_rejects_non_natural_integers(invalid_number):
    with pytest.raises(ValueError):
        is_prime(invalid_number)


def test_get_n_prime_returns_the_first_n_primes():
    assert get_n_prime(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_get_n_prime_returns_the_first_prime():
    assert get_n_prime(1) == [2]


def test_write_and_read_primes_round_trip_csv(tmp_path):
    output_file = tmp_path / "primes.csv"
    primes = [2, 3, 5, 7, 11]

    write_primes(primes, output_file)

    with output_file.open(newline="") as csvfile:
        assert next(csv.reader(csvfile)) == ["2", "3", "5", "7", "11"]
    assert read_primes(output_file) == primes


def test_generator_main_writes_and_prints_one_hundred_primes(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    main()

    generated_file = tmp_path / "output.csv"
    generated_primes = read_primes(generated_file)
    captured = capsys.readouterr()

    assert len(generated_primes) == 100
    assert generated_primes[:5] == [2, 3, 5, 7, 11]
    assert generated_primes[-1] == 541
    assert str(generated_primes) in captured.out

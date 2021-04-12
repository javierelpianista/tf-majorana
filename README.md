# tf-majorana
A simple Python program to compute the slope at origin of the Thomas-Fermi solution using the Majorana method as detailed in *Am. J. Phys.* **70** (2002) 852-856.

# Requirements
This program requires the `mpmath` module to run

# Usage
```
usage: c0.py [-h] [-N N] [--digits DIG] [--print-frequency FREQ] [--output-file FILE]

optional arguments:
  -h, --help            show this help message and exit
  -N N                  Sum up to N coefficients. (default: 5000)
  --digits DIG          Use DIG digits in the computation. (default: 400)
  --print-frequency FREQ
                        The partial sum is printed every FREQ coefficients. (default: 100)
  --output-file FILE    File where the results are printed. (default: results.dat)
```

# Examples
By default the program sums up to the first 5000 coefficients using 400 digits of precision, which is enough.
Its output is contained in the file `results.dat`.
The first 10000 digits can be summed up instead by using the following command:

```
python tf_majorana.py -N 10000 --digits 1000 --output-file 10000_digits.dat
```


import mpmath as mp
import argparse

# ------------------------------------------------------------------------------
# Read options from command line
# ------------------------------------------------------------------------------
parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-N', help = "Sum up to N coefficients.", default = 5000)
parser.add_argument('--digits', metavar = 'DIG', help = 
        "Use DIG digits in the computation. ")
parser.add_argument('--print-frequency', metavar = 'FREQ', help = 
        "The partial sum is printed every FREQ coefficients.")
parser.add_argument('--output-file', metavar = 'FILE', help = 
        'File where the results are printed.') 

parser.set_defaults(N=5000)
parser.set_defaults(digits=400)
parser.set_defaults(print_frequency=100)
parser.set_defaults(output_file = 'results.dat')

args = parser.parse_args()

# ------------------------------------------------------------------------------
# Set the number of digits
# ------------------------------------------------------------------------------
mp.mp.dps = int(args.digits)
from coefficients import coeffn

# ------------------------------------------------------------------------------
# Here we sum the coefficients 
# ------------------------------------------------------------------------------
v = 0

for n in range(int(args.N) + 1):
    v += coeffn(n)
    # Write the partial sum to the output file every FREQ coefficients
    if n % int(args.print_frequency) == 0:
        ans = (mp.mpf(3)/mp.mpf(16))**(1/mp.mpf(3))*v
        write_file = open(args.output_file, 'a')
        write_file.write('{:<6}{}\n'.format(n, ans))
        write_file.close()
        print('{:<6}{}'.format(n, ans))

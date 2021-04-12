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

# ------------------------------------------------------------------------------
# Here we compute the coefficient list. 
# ------------------------------------------------------------------------------

# The first two coefficients 
c = [1, 9-mp.sqrt(73)]

# The rest of the coefficients using recurrence Eq. (38) from 
# Am. J. Phys. 70 (2002) 852-856
def coeffn(M):
    global c

    while len(c) < M+1:
        m = len(c)
        c0 = 0
        for n in range(1, m-1):
            c0 += c[m-n]*(
                    (n+1)*c[n+1] - 2*(n+4)*c[n] + (n+7)*c[n-1]
                    )
        c1 = c[m-1] * ((m+7) - 2*(m+3)*c[1])
        c2 = c[m-2] * ((m+6)*c[1])

        c.append((c0+c1+c2)/(2*(m+8)-(m+1)*c[1]))

    return c[M]


# ------------------------------------------------------------------------------
# Here we sum the coefficients 
# ------------------------------------------------------------------------------
v = 0

for n in range(int(args.N) + 1):
    v += coeffn(n)
    # Write the partial sum to the output file every FREQ coefficients
    if n % int(args.print_frequency) == 0:
        ans = (3/16)**(1/3)*v
        write_file = open(args.output_file, 'a')
        write_file.write('{:<6}{}\n'.format(n, ans))
        write_file.close()
        print('{:<6}{}'.format(n, ans))

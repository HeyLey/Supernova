# Please, provide values


seconds = 3            # length the number of seconds in the file
minimum = 100          # rough minimum signal value
peak =    108          # rough signal peak value
lambd =   100          # lambda of poisson distribution
num = 1                # the number of signals (n > 0 && n <= s) in file with signal
pos = [2]

population_size = 1000  # populations size, number of different kernels
files_num = 500         # number of example files dt_b and dt_s
n = 10000               # number of iterations
eps = 0.01              # stop if score < eps (score of best kernel -> 0)


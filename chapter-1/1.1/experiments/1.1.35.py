'''
Dice Simulation
The following code computes the exact probability distrobution for the sum of the two dice:

int SIDES = 6;
int[] frequencies = new int[2*SIDES+1];
for (int i = 1; i <= SIDES; i++)
    for (int j = 1; j <= SIDES; j++)
        frequencies[i+j]++;

double[] probabilities = new double[2*SIDES+1];
for (int k = 1; k <= 2*SIDES; k++)
    probabilities = frequencies[k]/36.0;

The value probabilities[k] is the probability that the dice sum to k.
Run experiments to validate this calculation simulating n dice throws, keeping
track of the frequencies of occurence of each value when you compute the sum of two
random integers between 1 and 6. How large does n have to be before your emperical results match the exact
results to three decimal places?
'''

# step one is to implement this code in python
SIDES = 6
frequencies = [2*SIDES-1]
print(frequencies)
for i in range(SIDES+1):
    for j in range(SIDES+1):
        frequencies[i+j] += 1

probabilities = [2*SIDES-1]
for k in range(2*SIDES+1):
    probabilities = frequencies[k]/36.0

print(probabilities)
## Périat Prime Generator

A simple and efficient prime numbers generator. It does not use any multiplication (except binary shifts), neither modulo.

### How It Works

Instead of trying to remove all the non-prime factors, we associate each prime number (value) with its next multiple (key) in a dictionary structure. If a multiple is already present in the map, we iterate until we find a new one.
The multiples are thus recognised in constant time with the hashing (implicitly), and the new multiple can be associated with the prime number as a key.
A number is prime if and only if it is not detected as a key; it is associated with its double.

### Time and Space Complexities

n: the included limit

As each prime appears in the map at the end, it works with O(π(n)) ~ O(n / log n) auxiliary space.


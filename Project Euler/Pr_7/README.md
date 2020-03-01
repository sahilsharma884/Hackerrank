# Algorithm

1. Input the number of test case
2. Before proceeding the test case, precompute the prime number using Sieve. https://www.geeksforgeeks.org/sieve-of-eratosthenes/ <br>
`- Consider n (to iterate till maximum number) [Let say n= 10lakhs)`<br>
`- Just follow Sieve algorithm until number of prime number we got it in the list is 10k `<br>
`- If for given 'n' didnt give the number of prime number in the list is 10k, then just increase the n into 10x times`<br>
3. Each of test case, [let says, a0]
4. Since all the prime number are listed in sorted already. If you want to call 1st prime number (means, a0=1), just pass the index = a0-1.<br>

__Why -1 in a0? Because python start the list with index 0. And 1st prime number is stored in index = 0.__

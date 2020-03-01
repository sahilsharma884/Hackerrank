# Algorithm

1. Input the number of test case
2. Before proceeding the test case, precompute the prime number using Sieve. https://www.geeksforgeeks.org/sieve-of-eratosthenes/ <br>
`- Consider n (to iterate till maximum number) [Let say n= 10lakhs)`<br>
`- Just follow Sieve algorithm until number of prime number we got it in the list is 10k `<br>
`- If for given 'n' didnt give the number of prime number in the list is 10k, then just increase the n into 10x times`<br>
3. Now, we have stored all 10lakhs prime number in `prime_` variable
4. All you need is just pass the index and subtract 1 to get your desired output as per test caae.
For example

prime_ = [2,3,4,7,9, ....] <br>
If you want to call 1st prime number, then put n = 1. However in python, list starting index start with 0.<br>
So, if you `print(prime_[n])`, it will give you wrong output `3`.<br>
To make it correctly just pass n-1, `print(prime_[n-1])`<br>

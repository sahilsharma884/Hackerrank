# Algorithm

1. Enter number of test case
2. Enter number of digits `n` and window size `k`
3. Enter interger input value `num`
4. Convert `num` into list of each digit. Ex:- `num = 1234` ---> `num = [1,2,3,4]`
5. Initialize starting point `i = 0` and max product as `max_prod = -1`
6. Iterate starting point with windows size `(i+k)` till length of the digit `n`
7. In each iteration, initlaize starting `product = 1`
8. Fetch the __list of number within the windows size k__ and __product__ them all elementwise (using __for loop__)
9. If exisiting product is greater than max product `max_prod`, then update it otherwise continue to __next window slide__(or size)

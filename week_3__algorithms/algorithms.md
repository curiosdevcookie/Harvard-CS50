# Algorithms

In the context of CS50, we have a row of lockers, in which monopoly money is hidden behind each door. We search for the door with the 50 behind it.

## Searching

### Linear search

The money behind the doors are randomly placed.

Pseudo-coded linear search 1:

```code
For each door from left to right
    If 50 is behind door
            Return true
Return false
````

Pseudo-coded linear search 2:

```code
For i from 0 to n-1
    If 50 is behind dooors[i]
        return true
return false
````

* Upper bound: _O_(n)
* Lower bound: _Ω_(1)
* Upper bound == Lower bound (Θ): false

### Binary search

The money behind the doors is sorted from left to right.

Pseudo-coded binary search 1:

```code
If no door is left
    Return false
if 50 is behind middle door
    Return true
else if 50 < middle door
    Search left half
else if 50 > middle door
    Search right half
````

Pseudo-coded binary search 2:

```code
If no door is left
    Return false
if 50 is behind doors[middle]
    Return true
else if 50 < doors[middle]
    Search doors[0] through doors[middle-1]
else if 50 > doors[middle]
    Search doors[middle+1] through doors[n-1]
````

* Upperbound: _O_(log n)
* Lower bound: _Ω_(1)
* Upper bound == Lower bound (Θ): false

## Sorting

8 students are in a row with numbers in their hands. The teacher wants to sort them from smallest to largest.

### Selection Sort

Pseudo-coded selection sort 1:

```code
For i from 0 to n-1
    Find smallest number between i'th number and last number
    Swap smallest number with i'th number
````

Pseudo-coded selection sort 2:

```code
For i from 0 to n-1
    Find smallest number between numbers[i] and numbers[n-1]
    Swap smallest number with numbers[i]
````

Number of comparions:

* (n-1) + (n-2) + (n-3) + ... + 1
* n(n-1)/2
* (n^2-n)/2
* n^2/2 - n/2
* Upper bound: _O_(n^2)
* Lower bound: _Ω_(n^2)
* Upper bound == Lower bound (Θ): true

### Bubble Sort

Pseudo-coded bubble sort :

```code
Repeat n-1 times
    For i from 0 to n-2
        If numbers[i] > numbers[i+1]
            Swap numbers[i] with numbers[i+1]
        If no swaps
            Break
````

* (n-1)*(n-1)
* n^2 - 2n + 1
* Upper bound: _O_(n^2)
* Lower bound: _Ω_(n)
* Upper bound == Lower bound (Θ): false

### Merge Sort

Pseudo-coded merge sort 1:

```code
If only one number 
  Quit
Else 
  Sort left half of numbers
  Sort right half of numbers
Merge sorted halves
````

Pseudo-coded merge sort 2:

```code
If only one number 
  Quit
Else 
  Sort numbers[0] through numbers[middle]
  Sort numbers[middle+1] through numbers[n-1]
`````

* Upper bound: _O_(n log n)
* Lower bound: _Ω_(n log n)
* Upper bound == Lower bound (Θ): true

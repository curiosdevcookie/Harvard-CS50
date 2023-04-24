# Memory

## Storage

The storage in memory is divided into two parts: the stack and the heap. The stack is used to store local variables and function parameters. The heap is used to store dynamically allocated memory.

The pysical memory is divided into pages. Each page is 4KB in size. The operating system keeps track of which pages are in use and which pages are free. When a program requests memory, the operating system allocates a page of memory to the program. The operating system keeps track of which pages are in use by which programs. When a program is done using a page of memory, the operating system marks the page as free.

### The Heap

The heap is used to store dynamically allocated memory. The heap is managed by the `malloc` and `free` functions. The `malloc` function is used to allocate memory on the heap. The `free` function is used to free memory on the heap. For example:

```c
int *p = malloc(sizeof(int));
*p = 5;
free(p);
```

### The Stack

The stack is used to store local variables and function parameters. The stack is managed automatically by the compiler. When a function is called, the compiler allocates space on the stack for the local variables and function parameters. When the function returns, the compiler frees the space on the stack that was allocated for the local variables and function parameters.

```c
int add(int x, int y) {
    int z = x + y;
    return z;
}
```

## Pointers

Pointers are variables that store the memory address of another variable. Pointers are declared with the `*` operator. For example:

```c
int *p;
```

The `*` operator is called the dereference operator. It is used to access the value stored at the memory address stored in the pointer. For example:

```c
int x = 5;
int *p = &x;
printf("%d", *p); // prints 5
```

The `&` operator is called the address-of operator. It is used to get the memory address of a variable. For example:

```c
int x = 5;
int *p = &x;
printf("%p", p); // prints 0x7ffeeb5c9cfc
```

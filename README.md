# ADM-HW1
## Homework-1

##### *The submissission is organized as following:*
-  ***Scripts**: Python code of the Hackerrank submissions.*
- ***hackerrank_submissions**: The PDF file of the all submissions.*


 
#### Scripts.py
*The code is organized as following:*

- *Each module is identified by a title:*
> ```
> #######################
> #                     #
> # BASIC-DATA-TYPES    #
> #                     #
> #######################
>```

- *Each challenge is separated by a dashed line and the title of the challenge:* 
> ```
> # --------------------------------------------------------------- 
> # List Comprehensions
> ```

*Example*:

```
#######################
#                     #
# BASIC-DATA-TYPES    #
#                     #
#######################

# --------------------------------------------------------------- 
# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print(
        [
            [i,j,k] for i in range(x + 1) 
                    for j in range(y + 1)
                    for k in range(z + 1)
                    if i + j + k != n
        ]
    )
    
# ---------------------------------------------------------------  
# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(
        max([i for i in arr if i != max(arr)])
    )

```


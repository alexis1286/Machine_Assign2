# Requirements

  * Python 3.9

# Sample Execution & Output

If run without command line arguments, using

```

main.py


the following message will be displayed


main.py : The term 'main.py' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ main.py
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (main.py:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 


If run using

``` 

python main.py 16 -0.55

```

output *simliar* to

|       Base 10      |        Base 16      |
|:-------------------|:-------------------|
|-0.55               |-0.8CCC             |


```

will be generated.



If run using

```

python main.py 8 15

```

output *simliar* to

```

|       Base 10      |        Base 8      |
|:-------------------|:-------------------|
|15                  |17.                 |


```

will be generated.




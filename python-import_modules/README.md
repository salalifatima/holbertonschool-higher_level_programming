# Python - import & modules

In this project, I learned about importing and using functions and creating
modules in Python. I further practiced using the builtin function
`dir()` and using command line arguments within Python programs.

## Tasks :page_with_curl:

* **0. Import a simple function from a simple file**
  * [0-add.py](./0-add.py): Python program that imports the function
  `def add(a, b):` from the file [add_0.py](./add_0.py) and prints the
  result of the addition `1 + 2 = 3`.
  * Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

* **1. My first toolbox!**
  * [1-calculation.py](./1-calculation.py): Python program that imports functions
  from the file [calculator_1.py](./1-calculator.py) and prints the result
  of the addition, subtraction, multiplication and division of `10` and `5`.
  * Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

* **2. How to make a script dynamic!**
  * [2-args.py](./2-args.py): Python program that prints the number of
  and list of its arguments.
  * Output: `[Number of arguments] argument` (if number is one) or `arguments` (otherwise), followed by:
    * `:` (or `.` if no argumets were passed), followed by
    * A new line, followed by
    * One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

* **3. Infinite addition**
  * [3-infinite_add.py](./3-infinite_add.py): Python program that prints the result of the
  addition of all arguments.
  * Output: Sum of the arguments followed by a new line.

* **4. Who are you?**
  * [4-hidden_discovery.py](./4-hidden_discovery.py): Python program that prints all the
  names defined by the compiled module `hidden_4.pyc`.
  * Output: One name per line in alphabetical order.
  * Names starting with `__` are not printed.
* **5. Everything can be imported**
  * [5-variable_load.py](./5-variable_load.py): Python program that imorts the
  variable `a` from the file [variable_load_5.py](./variable_load_5.py) and prints its value.

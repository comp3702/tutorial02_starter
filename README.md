# Starter Code - Tutorial 02

Start by running the tests in [TestPuzzleNode.py](tests/TestPuzzleNode.py) and implementing the [PuzzleNode.py](PuzzleNode.py).

Once your environment is finished, run the [test_breadth_first_search.py](tests/test_breadth_first_search.py) and [test_depth_first_search.py](tests/test_depth_first_search.py) and implement the [BFS](breadth_first_search.py) and [DFS](depth_first_search.py) to satisfy the tests.

Finally, run the [test_uniform_cost_search.py](tests/test_uniform_cost_search.py) and implement the [UCS](uniform_cost_search.py) to pass the tests.

## Breadth First Search, Depth First Search and Uniform Cost Search

Loosely based on official solutions that will be released later in the week.

The main differences to the other solutions:

1) It uses agent taking actions/steps in environment paradigm - rather than graph / node / children paradigm (similar to Nick's solution)
2) Hides the Node implementation from the end user by accepting 2D arrays as initial and goal state
3) Keeps the state as immutable tuple of tuples rather than lists
4) Fixes naming conventions and caches some calculations to make the code more readable
5) __There are unit tests__ - for the PuzzleNode as well as the searches - I am hoping they will help with debugging issues faced by the students
6) It's faster and uses less memory than the other solutions - __although it is still not good enough to solve the 15-puzzle__ - see the [main.py](main.py) - see the [next week's tutorial](https://github.com/comp3702/tutorial03) on how to solve the 15-puzzle

### Dependencies
I used Python 3.10 (because of the match/case - but I removed it later), but it should work with any 3.x.
There are no extra dependencies, but just in case there will be, there is [environment.yml](environment.yml).

To create/restore the environment:

    conda env create -f environment.yml

To update the file:

    conda env export > environment.yml


### Running
[main.py](main.py) can be used for experimentation testing different initial/goal combinations.

    python main.py

### Running Tests
The tests are in [tests/](tests/) dir and can be either run individually or everything:

    python -m unittest discover -s tests -t tests

The easiest is probably using the IDE such as PyCharm (I am using professional version, but there is a community version as well):

<a href="https://drive.google.com/file/d/19lTjYU7GBHJtXwr1gd1rknzzjRqftJNh/preview" target="_blank">
<img src="docs/running_tests.png">
</a>

The tests cover the `PuzzleNode` a.k.a. the environment as well as the searches and the problems from Q2.2. 
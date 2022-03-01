# ECM2429-workshop-4-exercises

Python programming exercises

## Concurrency

Concurrency means a program is doing mutliple things at the same time.  In computing this is achieved through the use of multiple processors or time-slicing, sharing a single processor between tasks by rapidly switching between them.

Mutliple processors can also be used for *parallel-processing* where the same task, but with different data, is run on each processor to reduce the time taken to compute results. 

## Python threading

In Python there are various ways of creating programs with concurrent tasks.  The most popular is threading, and this is used in other programming languages.  In a threaded program the code is shared between all the threads, there is no need to write separate units of code for each one, but there will be several parts of the program being executed at the same time.

## Threads example

Here is a simple example where a thread is created to run a countdown.  Note that
both the main program and the thread created using the threading module use
sleep() but doing so only pauses the relevant part of the program.

[threads_demo/countdown.py](threads_demo/countdown.py)

```python
from threading import Thread
from time import sleep


def countdown_activity():
    for i in range(10, -1, -1):
        print(f"   COUNTDOWN {i}")
        sleep(1.5)
    print("   Thread ends.")

# Change to daemon=True and observe the different behaviour.
mythread = Thread(target=countdown_activity, daemon=False)
print("About to start thread...")
mythread.start()

for i in range(5):
    print(f"Main program counter {i}")
    sleep(0.4)

print("Main ends.")

```

Creating many threads is easy.  The program will end when all non-daemon threads have finished.  The main program is a non-daemon
thread.  However, it can be very hard to rationalise what a program with many threads is doing at any point in time, and extremely difficult to debug if it doesn't behave as expected.  Therefore we need to think carefully about our design.

## Using threads with an event-loop

A event-loop is an ideal design pattern for launching threads to complete user requests.

[threads_demo/app.py](threads_demo/app.py)

## Designing for concurrency

Concurrency can add significant complexity to the run-time environment.  However, used appropriately
it can simplify the design and implementation of software and produce better performance.

Something we can see already is that a daemon-thread can end suddenly, perhaps during file or database access.

Even when a thread runs to completion it doesn't usually
return any data to the main program.  Threads aren't a "non-blocking" alternative to function.

If we want to pass data between threads we need to use appropriate "thread-safe" communication such as a Queue.

## Music player example

This is a more advanced example that uses threads to enable audio playing, database access and a GUI to run simultaneously.  The main program runs the tkinter GUI and coordinates communication with the two other threads.

[code/app.py](code/app.py)

### Running the example

Must be in the same directory (folder) as music.db
```sh
cd code
python app.py
```

### Running the tests

There are some basic tests in code/tests.  Pytest should find these automatically if PYTHON_PATH is correct.  The easiest way to ensure this is to run using ```python -m```
```sh
> cd code
> python -m pytest --cov .
```

## Resources

<https://docs.python.org/3/library/queue.html>

<http://tkdocs.com/tutorial/morewidgets.html#listbox>

<https://docs.python.org/3/library/tkinter.html#threading-model>


## Reading

1. Chapters 29 and 30 of Hunt Advanced

1. Coroutines <https://en.wikipedia.org/wiki/Coroutine>

1. Designing with threads <https://www.oreilly.com/library/view/the-art-of/9780596802424/ch04.html>
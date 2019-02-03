Serial Usage
=============

If you are using the code for a single process (not several parallel processes)
the basic usage is very simple.

First, we import the package and initialize a `ProgressBar` object.

.. code:: python

    from pprogress import ProgressBar
    pg = ProgressBar(N)

Here `N` is the number of steps in the iteration.

Next, we setup out loop and within the loop, we update the progress bar
(usually at the end). Note that the progress bar does not print until `update`
runs the first time. If the loop takes a long time or each iteration, we can
call `update(0)` to simply initialize the bar on the screen.

.. code:: python

    pd.update(0) #  Only needed if you want to initialize the progress
                 #  bar on the screen before the loop starts.
    for i in range(N):
        # Do stuff inside your loop.
        pb.update()

Finally, it is recommended that at the end of the loop you call `pb.done()`.
This ensures that the terminal inserts a newline at the end of the code. The
use of this is much more apparent in the parallel version but I would recommend
using it in the serial version too.

Putting it all together:

.. code:: python

    from pprogress import ProgressBar

    pb.ProgressBar(N)

    pb.update(0) #  Optional, see above
    for i in range(N):
        # Do stuff inside your loop.
        pb.update()

    pb.done()

And that's it! You now have a progress bar working for your loop.

PProgress: A progress bar that works with MPI
=========================================================

.. image:: https://badge.fury.io/py/PProgress.svg
    :target: https://badge.fury.io/py/PProgress

Features
--------

Provides an all purpose Python based progress bar utility that can be run in
loops either running in serial or parallel with MPI or other utilities.

 * When using parallel loops, each parallel progress gets a progress bar.
 * The progress bar shows the percent completion of the tasks assigned to that process.
 * If there are multiple processes, all progress bars remain until the final onefinishes.

Quick Start
--------------

PProgess can simply be install using pip as:

    pip install pprogress

Then you can try out a simple serial example as:

.. code:: python

    from pprogress import ProgressBar
    from time import sleep

    N = 100
    pb = ProgressBar(N)
    for i in range(N):
        pb.update()
        sleep(0.1)
    pb.done()



Documentation
--------------

Full documentation with parallel examples coming soon!

# Highcharts for Python Demos
This is a collection of demonstrations of the Highcharts for Python toolkit. Fundamentally, they are a Python port of the fantastic demos that Highsoft has already published for their [Highcharts JavaScript library](https://www.highcharts.com/demo).

## Overview

The demos showcase a variety of ways of working with Highcharts for Python to create and visualize data. Because Highcharts for Python provides multiple paths to create your visualizations, we have tried to showcase various methods. Some demos use:

  * **Direct instantiation**. They create Python instances of objects using Python constructors like ``LineSeries(...)`` directly.
  * ``.from_js_literal()``. They create ``HighchartsOptions`` instances by taking a string of a JS literal option configuration using the ``.from_js_literal()`` method.
  * ``.from_dict()``. They create Python instances using the Highcharts for Python ``.from_dict()`` convenience method.
  * other demo-specific techniques, which may vary from demo to demo

Each demo ultimately demonstrates one or more visualizations using one of the techniques mentioned above. The basic pattern we use is to:

  1. Import the needed dependencies.
  2. Assemble the options.
  3. Assemble the chart.
  4. Visualize the chart.

**NOTE!! The demos in this repository are a work in progress, and various demos will be added over time. Please check back periodically to see if new demos have been added.**

## How to Use the Demos

### Organization
The demos are organized in Jupyter Notebooks, which make it easy to follow how they work, see their results in action, and experiment with them as needed.

The repository is organized into folders for each of the Highcharts for Python libraries:

  * ``highcharts-core`` contains demos of the [Highcharts Core for Python](https://core-docs.highchartspython.com) library
  * ``highcharts-stock`` contains demos of the [Highcharts Stock for Python](https://stock-docs.highchartspython.com) library
  * ``highcharts-maps`` contains demos of the [Highcharts Maps for Python](https://maps-docs.highchartspython.com) library
  * ``highcharts-gantt`` contains demos of the [Highcharts Gantt for Python](https://gantt-docs.highchartspython.com) library

Within each of these folders, you will find sub-folders grouping demos into a particular category. For example:

  * the ``highcharts-core/line-charts`` folder contains Jupyter Notebooks which demonstrate different line chart functionality. 
  * the ``highcharts-core/python-features`` folder contains Notebooks which demonstrate some Python-specific features

### Using the Demos via MyBinder.org

The easy way to use or review the demos is to launch a MyBinder session using the following buttton: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/highcharts-for-python/highcharts-for-python-demos/HEAD)

Once the MyBinder launches, you will find yourself in a Jupyter Lab environment within a Docker image. You'll have this full repository available to you, and you can navigate the folders to find the demo you want to run. 

For example, to see how **Highcharts Core for Python** generates a basic line chart, you can open the Notebook at ``highcharts-core/line-charts/basic-line.ipynb``.

Then just run the Notebook, and you should see the results.

### Using the Demos Locally
To use the demos locally, you need to take several additional steps:

1. First, clone this Github repo:

    ```
    $ git clone git@github.com:highcharts-for-python/highcharts-for-python-demos.git
    ```

2. Next, navigate to its directory:

    ```
    $ cd highcharts-for-python-demos

    highcharts-for-python-demos/ (master)
    $
    ````

3. Create a virtual environment:

    ```
    highcharts-for-python-demos/ (master)
    $ python -m venv .venv
    ```

4. Then activate your virtual environment:

    ```
    highcharts-for-python-demos/ (master)
    $ source .venv/Scripts/activate

    (.venv)
    highcharts-for-python-demos/ (master)
    $
    ```

5. And install the requirements:

    ```
    (.venv)
    highcharts-for-python-demos/ (master)
    $ pip install -r requirements.txt
    ```

6. And finally, open up Jupyter Lab:

    ```
    (.venv)
    highcharts-for-python-demos/ (master)
    $ jupyter-lab
    ```

You should now see the set of notebooks included in the repo, along with relevant data files and other details.

For example, to see how **Highcharts Core for Python** generates a basic line chart, you can open the Notebook at ``highcharts-core/line-charts/basic-line.ipynb``.

Then just run the Notebook, and you should see the results.

## Contributing to the Demos

If you wish to contribute demos to this library:

1. First, clone this Github repo:

    ```
    $ git clone git@github.com:highcharts-for-python/highcharts-for-python-demos.git
    ```

2. Next, navigate to its directory:

    ```
    $ cd highcharts-for-python-demos

    highcharts-for-python-demos/ (master)
    $
    ````

3. Create a virtual environment:

    ```
    highcharts-for-python-demos/ (master)
    $ python -m venv .venv
    ```

4. Activate your virtual environment:

    ```
    highcharts-for-python-demos/ (master)
    $ source .venv/Scripts/activate

    (.venv)
    highcharts-for-python-demos/ (master)
    $
    ```

5. Install the requirements:

    ```
    (.venv)
    highcharts-for-python-demos/ (master)
    $ pip install -r requirements.txt
    ```

6. Install the pre-commit hook (which strips output from the Jupyter Notebooks on commit):

    ```
    (.venv)
    highcharts-for-python-demos/ (master)
    $ pre-commit install
    ```

7. Create a new branch in your repo that you will use for your changes.

8. Either edit the existing Jupyter Notebooks or add new ones using the basic conventions and pattern that you'll find in our other demos.

9. Commit your changes and push them to this Github repo.

10. File a Pull Request to merge changes from your branch to the ``develop`` branch.

And that's it! Thank you for your contributions, they are much appreciated.
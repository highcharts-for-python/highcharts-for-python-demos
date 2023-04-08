# Highcharts for Python Demos
This is a collection of demonstrations of the Highcharts for Python toolkit.
Fundamentally, they are a Python port of the fantastic demos that Highsoft has
already published for their 
[Highcharts JavaScript library](https://www.highcharts.com/demo).

## How to Use the Demos

### Using MyBinder.org
The easy way is to launch a MyBinder session using the repository: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/highcharts-for-python/highcharts-for-python-demos/HEAD)

Once the MyBinder launches, you will find yourself in a Jupyter Lab environment within a Docker image. You'll have this full repository available to you, and you can navigate the folders to find the demo you want to run. 

You will find that the folders are organized according to the Highcharts for Python library being demonstrated, e.g. ``highcharts-core`` for the **Highcharts Core for Python** library, and ``highcharts-stock`` for the **Highcharts Stock for Python** library, etc. And within each of those folders you will find additional folders organizing the demos by chart type or type of demo. 

For example, to see how **Highcharts Core for Python** generates a basic line chart, you can open the Notebook at ``highcharts-core/line-charts/basic-line.ipynb``.

Then just run the Notebook, and you should see the results.

### Using the Demos Locally
To use the demos locally, you need to take several additional steps:

First, clone this Github repo:

```
$ git clone git@github.com:highcharts-for-python/highcharts-for-python-demos.git
```

Next, navigate to its directory:

```
$ cd highcharts-for-python-demos

highcharts-for-python-demos/ (master)
$
````

Create a virtual environment:

```
highcharts-for-python-demos/ (master)
$ python -m venv .venv
```

Then activate your virtual environment:

```
highcharts-for-python-demos/ (master)
$ source .venv/Scripts/activate

(.venv)
highcharts-for-python-demos/ (master)
$
```

and install the requirements:

```
(.venv)
highcharts-for-python-demos/ (master)
$ pip install -r requirements.txt
```

And finally, open up Jupyter Lab:

```
(.venv)
highcharts-for-python-demos/ (master)
$ jupyter-lab
```

You should now see the set of notebooks included in the repo, along with relevant data files and other details.

You will find that the folders are organized according to the Highcharts for Python library being demonstrated, e.g. ``highcharts-core`` for the **Highcharts Core for Python** library, and ``highcharts-stock`` for the **Highcharts Stock for Python** library, etc. And within each of those folders you will find additional folders organizing the demos by chart type or type of demo. 

For example, to see how **Highcharts Core for Python** generates a basic line chart, you can open the Notebook at ``highcharts-core/line-charts/basic-line.ipynb``.

Then just run the Notebook, and you should see the results.
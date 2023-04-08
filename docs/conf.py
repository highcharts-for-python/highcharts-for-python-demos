# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__name__), '..'))


version_dict = {}
with open(os.path.join(os.path.dirname(__file__),
                       '../',
                       'src/',
                       '__version__.py')) as version_file:
    exec(version_file.read(), version_dict)                   # pylint: disable=W0122

__version__ = version_dict.get('__version__')

project = 'Highcharts for Python Demos'
copyright = '2022, HCP LLC'
author = 'Chris Modzelewski'

# The short X.Y version
version = __version__[:3]
# The full version, including alpha/beta/rc tags
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 3,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'style_nav_header_background': 'rgb(70, 70, 92)'
}

html_logo = '_static/highcharts-for-python-light-150x149.png'
html_favicon = '_static/highcharts-for-python-dark-32x32.png'

html_context = {
    "display_github": True,                 # Integrate GitHub
    "github_user": "highcharts-for-python",       # Username
    "github_repo": "highcharts-for-python-demos",     # Repo name
    "github_version": "master",             # Version
    "conf_py_path": "/docs/",               # Path in the checkout to the docs root
}

github_username = 'highcharts-for-python'
github_repository = 'highcharts-for-python-demos'

sphinx_tabs_disable_tab_closing = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.10', None),
    'validator-collection': ('http://validator-collection.readthedocs.io/en/latest/', None),
    'ipython': ('https://ipython.readthedocs.io/en/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'pyspark': ('https://spark.apache.org/docs/latest/api/python/', None),
}

todo_include_todos = True

# Inheritance Diagram configuration
inheritance_graph_attrs = {
    'rankdir': 'TB'
}


suppress_warnings = [
    # 'ref.term',
    'ref.ref',
    'toc.not_readable'
]


html_js_files = [
    'https://code.highcharts.com/highcharts.js',
    'https://code.highcharts.com/highcharts-more.js',
    'https://code.highcharts.com/highcharts-3d.js',
    'https://code.highcharts.com/modules/accessibility.js',
    'https://code.highcharts.com/modules/annotations.js',
    'https://code.highcharts.com/modules/boost.js',
    'https://code.highcharts.com/modules/broken-axis.js',
    'https://code.highcharts.com/modules/data.js',
    'https://code.highcharts.com/modules/exporting.js',
    'https://code.highcharts.com/modules/drilldown.js',
    'https://code.highcharts.com/modules/funnel.js',
    'https://code.highcharts.com/modules/heatmap.js',
    'https://code.highcharts.com/modules/no-data-to-display.js',
    'https://code.highcharts.com/modules/offline-exporting.js',
    'https://code.highcharts.com/modules/solid-gauge.js',
    'https://code.highcharts.com/modules/series-label.js',
    'https://code.highcharts.com/modules/treemap.js'
]
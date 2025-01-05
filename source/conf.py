# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = html_title = 'Jonas Care Guide'
author = 'Rob & Craig'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'myst_parser',
    'sphinx.ext.autosectionlabel',
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []
autosectionlabel_maxdepth = 3
autosectionlabel_prefix_document = True

myst_url_schemes = {
    "http": None,
    "https": None,
    "tel": {
        "url": "tel:{{path}}",
        "title": "{{path}}",
    },
    "mailto": {
        "url": "mailto:{{path}}",
        "title": "{{path}}",
    },
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_theme_options = {
    'body_max_width': 'none'
}

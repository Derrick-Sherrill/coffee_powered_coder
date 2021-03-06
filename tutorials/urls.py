from django.contrib import admin
from django.urls import path
from tutorials import views

urlpatterns = [
    path('', views.index, name='tutorials_home'),
    # Begin Arduino Links
    path('arduino/', views.arduino_home, name='arduino_home'),
    path('ardunio/hello-world/', views.arduino_hello_world, name='arduino_hello_world'),
    path('ardunio/blinking-light/', views.arduino_blinking_light, name='arduino_blinking_light'),
    # Begin Python Links
    path('python/', views.python_home, name='python_home'),
    path('whylearnpython/', views.whylearnpython, name='why_learn_python'),
    path('download/', views.python_download, name='python_download'),
    path('syntax/', views.python_syntax, name='python_syntax'),
    path('variables-and-data-types/', views.python_variables_dtypes, name='python_variables_dtypes'),
    path('composite-data-types/', views.python_composite_data_types, name='python_composite_dtypes'),
    path('strings/', views.python_strings, name='python_strings'),
    path('numbers/', views.python_numbers, name='python_numbers'),
    path('lists/', views.python_lists, name='python_lists'),
    path('tuples/', views.python_tuples, name='python_tuples'),
    path('sets/', views.python_sets, name='python_sets'),
    path('dictionaries/', views.python_dictionaries, name='python_dictionaries'),
    path('if-statements/', views.python_if_statements, name='python_if_statements'),
    path('while-loops/', views.python_while_loops, name='python_while_loops'),
    path('for-loops/', views.python_for_loops, name='python_for_loops'),
    # Begin NumPy Links
    path('numpy/', views.numpy_home, name='numpy_home'),
    path('numpy/arrays/', views.numpy_arrays, name='numpy_arrays'),
    path('numpy/indexing/', views.numpy_indexing, name='numpy_indexing'),
    path('numpy/array-math/', views.numpy_array_math, name='numpy_array_math'),
    path('numpy/broadcasting/', views.numpy_broadcasting, name='numpy_broadcasting'),
    # BEGIN TENSORFLOW LINKS BEGIN TENSORFLOW LINKS
    path('tensorflow/', views.tensorflow_home, name='tensorflow_home'),
    path('tensorflow/linear-regression/', views.tensorflow_linear_regression, name='tensorflow_linear_regression'),
    # Begin Pandas LINKS
    path('pandas/', views.pandas_home, name='pandas_home'),
    path('pandas/dataframes/', views.pandas_dataframes, name='pandas_dataframes'),
    path('pandas/select-data/', views.pandas_select_data, name='pandas_select_data'),
    path('pandas/multiindex/', views.pandas_multiindex, name='pandas_multiindex'),
    path('pandas/concat/', views.pandas_concat, name='pandas_concat'),
    # Begin Excel Python Automation LINKS
    path('automate-excel/', views.automate_excel_home, name='automate_excel_home'),
    path('automate-excel/calculations/', views.automate_excel_calculations, name='automate_excel_calculations'),
    # Begin REQUESTS LINKS
    path('requests/', views.requests_home, name='requests_home'),
    path('requests/real-time-stock-market-analysis/', views.requests_real_time_stock_analysis, name='requests_real_time_stock_analysis'),
    path('requests/cartesian-products/', views.requests_cartesian_products, name='requests_cartesian_products'),
]

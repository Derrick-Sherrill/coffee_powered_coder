from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tutorials/index.html')

def python_home(request):
    return render(request, 'tutorials/python.html')

def whylearnpython(request):
    return render(request, 'tutorials/python/WhyLearnPython.html')

def python_syntax(request):
    return render(request, 'tutorials/python/syntax.html')

def python_variables_dtypes(request):
    return render(request, 'tutorials/python/variables_datatypes.html')

def python_composite_data_types(request):
    return render(request, 'tutorials/python/composite_data_types.html')

def python_strings(request):
    return render(request, 'tutorials/python/strings.html')

def python_numbers(request):
    return render(request, 'tutorials/python/numbers.html')

def python_lists(request):
    return render(request, 'tutorials/python/lists.html')

def python_tuples(request):
    return render(request, 'tutorials/python/tuples.html')

def python_sets(request):
    return render(request, 'tutorials/python/sets.html')

def python_dictionaries(request):
    return render(request, 'tutorials/python/dictionaries.html')

def python_if_statements(request):
    return render(request, 'tutorials/python/if_statements.html')

def python_while_loops(request):
    return render(request, 'tutorials/python/while_loops.html')

def python_for_loops(request):
    return render(request, 'tutorials/python/for_loops.html')


### BEGIN NUMPY LINKS BEGIN NUMPY LINKS BEGIN NUMPY LINKS ####

def numpy_home(request):
    return render(request, 'tutorials/numpy.html')

def numpy_arrays(request):
    return render(request, 'tutorials/numpy/arrays.html')



### BEGIN PANDAS LINKS BEGIN PANDAS LINKS #####
def pandas_home(request):
    return render(request, 'tutorials/pandas.html')

def pandas_dataframes(request):
    return render(request, 'tutorials/pandas/dataframes.html')

def pandas_select_data(request):
    return render(request, 'tutorials/pandas/select_data.html')

def pandas_multiindex(request):
    return render(request, 'tutorials/pandas/multiindex.html')

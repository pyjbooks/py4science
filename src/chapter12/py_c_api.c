#include <Python.h>

static PyObject *
fact(PyObject *self, PyObject *args)
{
    int n;
    int i;
    int ret=1;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    for (i=n; i>0; i--) ret *= i;
    
    return Py_BuildValue("i", ret);
}

#include <Python.h>

/*
 * Implements an example function.
 */
PyDoc_STRVAR(PythonModule_example_doc, "example(obj, number)\
\
Example function");

PyObject *PythonModule_example(PyObject *self, PyObject *args, PyObject *kwargs) {
    /* Shared references that do not need Py_DECREF before returning. */
    PyObject *obj = NULL;
    int number = 0;

    /* Parse positional and keyword arguments */
    static char* keywords[] = { "obj", "number", NULL };
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "Oi", keywords, &obj, &number)) {
        return NULL;
    }

    /* Function implementation starts here */

    if (number < 0) {
        PyErr_SetObject(PyExc_ValueError, obj);
        return NULL;    /* return NULL indicates error */
    }

    Py_RETURN_NONE;
}

/*
 * List of functions to add to PythonModule in exec_PythonModule().
 */
static PyMethodDef PythonModule_functions[] = {
    { "example", (PyCFunction)PythonModule_example, METH_VARARGS | METH_KEYWORDS, PythonModule_example_doc },
    { NULL, NULL, 0, NULL } /* marks end of array */
};

/*
 * Initialize PythonModule. May be called multiple times, so avoid
 * using static state.
 */
int exec_PythonModule(PyObject *module) {
    PyModule_AddFunctions(module, PythonModule_functions);

    PyModule_AddStringConstant(module, "__author__", "cloud");
    PyModule_AddStringConstant(module, "__version__", "1.0.0");
    PyModule_AddIntConstant(module, "year", 2018);

    return 0; /* success */
}

/*
 * Documentation for PythonModule.
 */
PyDoc_STRVAR(PythonModule_doc, "The PythonModule module");


static PyModuleDef_Slot PythonModule_slots[] = {
    { Py_mod_exec, exec_PythonModule },
    { 0, NULL }
};

static PyModuleDef PythonModule_def = {
    PyModuleDef_HEAD_INIT,
    "PythonModule",
    PythonModule_doc,
    0,              /* m_size */
    NULL,           /* m_methods */
    PythonModule_slots,
    NULL,           /* m_traverse */
    NULL,           /* m_clear */
    NULL,           /* m_free */
};

PyMODINIT_FUNC PyInit_PythonModule() {
    return PyModuleDef_Init(&PythonModule_def);
}

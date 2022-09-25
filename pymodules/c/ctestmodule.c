#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject *
ctest_test(PyObject *self, PyObject *args)
{
  long int testint = 1;
  return args;
}

static PyMethodDef CtestMethods[] = {
    {"test",  ctest_test, METH_VARARGS,
     "Returns 1."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef ctestmodule = {
    PyModuleDef_HEAD_INIT,
    "ctest",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    CtestMethods
};

PyMODINIT_FUNC
PyInit_ctest(void)
{
    return PyModule_Create(&ctestmodule);
}

int
main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    if (PyImport_AppendInittab("ctest", PyInit_ctest) == -1) {
        fprintf(stderr, "Error: could not extend in-built modules table\n");
        exit(1);
    }

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required.
       If this step fails, it will be a fatal error. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyObject *pmodule = PyImport_ImportModule("ctest");
    if (!pmodule) {
        PyErr_Print();
        fprintf(stderr, "Error: could not import module 'ctest'\n");
    }

    PyMem_RawFree(program);
    return 0;
}

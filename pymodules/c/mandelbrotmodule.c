#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject *
mandelbrot_mandelbrot(PyObject *self, PyObject *args)
{
  int ok;
  long double bl, tl, br, tr;
  long double zn[2048][2048][2];
  
  for (long double i = 0; i < 2048; i++) {
    for (long double r = 0; r < 2048; r++) {
      zn[i][r][0] = r;
      zn[i][r][1] = i;
    }
  }
}

static PyMethodDef MandelbrotMethods[] = {
    {"mandelbrot",  mandelbrot_mandelbrot, METH_VARARGS,
     "Returns 1."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef mandelbrotmodule = {
    PyModuleDef_HEAD_INIT,
    "mandelbrot",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    MandelbrotMethods
};

PyMODINIT_FUNC
PyInit_mandelbrot(void)
{
    return PyModule_Create(&mandelbrotmodule);
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
    if (PyImport_AppendInittab("mandelbrot", PyInit_mandelbrot) == -1) {
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
    PyObject *pmodule = PyImport_ImportModule("mandelbrot");
    if (!pmodule) {
        PyErr_Print();
        fprintf(stderr, "Error: could not import module 'mandelbrot'\n");
    }

    PyMem_RawFree(program);
    return 0;
}

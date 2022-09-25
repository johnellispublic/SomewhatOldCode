from distutils.core import setup, Extension

module1 = Extension("ctest", sources=["ctestmodule.c"])
setup(name="CTest", version="1.0", description="Test module", ext_modules=[module1])

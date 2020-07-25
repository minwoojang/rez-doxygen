name = "doxygen"

version = "1.8.18"

authors = [
    "Dimitri van Heesch"
]

description = \
    """
    Doxygen is the de facto standard tool for generating documentation from annotated C++ sources, but it also supports
    other popular programming languages such as C, Objective-C, C#, PHP, Java, Python, IDL (Corba, Microsoft, and
    UNO/OpenOffice flavors), Fortran, VHDL, and to some extent D.
    """

requires = [
    "bison-3+",
    "cmake-3+",
    "flex-2+",
    "gcc-6+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

tools = [
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "doxygen-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    # env.LD_LIBRARY_PATH.prepend("{root}/lib")
    # env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")
    # env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/Alembic")

    # # Helper environment variables.
    # env.ALEMBIC_BINARY_PATH.set("{root}/bin")
    # env.ALEMBIC_INCLUDE_PATH.set("{root}/include")
    # env.ALEMBIC_LIBRARY_PATH.set("{root}/lib")

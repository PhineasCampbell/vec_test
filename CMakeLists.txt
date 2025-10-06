cmake_minimum_required(VERSION 3.28.3)
project(vec_test)

add_subdirectory(pybind11)
pybind11_add_module(vec_test src/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(vec_test PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})

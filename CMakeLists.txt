cmake_minimum_required(VERSION 3.15)
project(IronCircuit VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

pybind11_add_module(ironcircuit src/cpp/monitor.cpp src/cpp/bindings.cpp)

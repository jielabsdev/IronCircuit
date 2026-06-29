#include <pybind11/pybind11.h>
#include "monitor.hpp"

namespace py = pybind11;

PYBIND11_MODULE(ironcircuit, m) {
    py::class_<ironcircuit::Policy>(m, "Policy")
        .def(py::init<double, bool>());

    py::class_<ironcircuit::Monitor>(m, "Monitor")
        .def(py::init<ironcircuit::Policy, double>(), py::arg("policy"), py::arg("initial_usage") = 0.0)
        .def("check_usage", &ironcircuit::Monitor::check_usage)
        .def("get_usage", &ironcircuit::Monitor::get_usage);
}

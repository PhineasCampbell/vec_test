#include <vector>
#include <numeric>
#include <pybind11/pybind11.h>


class VecTest
{
public:
  VecTest(py::list & l){
    for (py::handle o : l) {
        double d = py::cast<double>(o);
        v.push_back(d);
    }
    return;
  }
  
  double SumV1(){
    double result = 0;
    result = std::accumulate(v.begin(), v.end(), 0.0);
    return result;
  }
  
  double SumV2(){
    double result = 0;
    for(int i = 0; i < v.size(); i++)
        result += v[i];
    return result;
  }
  

private:
  std::vector<double> v;
};

PYBIND11_MODULE(vec_test, m, py::mod_gil_not_used()){
  py::class_<vec_test>(m, "vec_test")
  .def(py::init<py::list & l>())
  .def("SumV1", &VecTest::SumV1)
  .def("SumV2", &VecTest::SumV2);
}

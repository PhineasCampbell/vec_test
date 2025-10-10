This is a project to test pybind build from the same source on both Windows and Linux environments
It requires cmake to be installed on the machine
To build and run the code git clone --recursive
cd to the build directory
cmake ..
This creates the project to build for either visual studio or gcc.
Copy the .so or .pyd file to the location where python looks for its libraries.
The vec_time_test.py file is a python script that compares the time taken to sum large lists, it requires numpy to be installed
This is a work in progress, I am working on improving the style.

Hope you find it interesting

Phineas


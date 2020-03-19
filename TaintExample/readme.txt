3/17/20 3:37 PM Dino Becaj

Cloned Pybind11 repository from git to Desktop. Installed cmake as well.

Pybind11 recommends testing pybind11 by running the included test files. 

Entered pybind11 directory:

Mkdir build
Cd build
cmake ..
Make -j4 pytest

304 test cases passed, 29 were skipped.

For the 29 that were skipped, they were skipped because of the following error: 
"Eigen and/or numpy are not installed". Numpy is installed. Am now finding a way to install Eigen.

Can't find solution to this problem right now so am going to skip.

I need to create my c++ matrix multiplier, javascript front end, and python backend.
#include "pybind11/include/pybind11.h"
#include "pybind11/include/stl.h"
#include <iostream>
#include <vector>

namespace py = pybind11;

std::vector<std::vector<int>> populateArray(py::list);
void printVec(std::vector<std::vector<int>>);
std::vector<std::vector<int>> matMult(std::vector<std::vector<int>>, std::vector<std::vector<int>>);

std::vector<std::vector<int>> multiply(py::list A, py::list B) {
	// I was unable to figure out a simpler way to unpack the Python
	// objects passed to C++, so I copied all the integers from each 
	// of the 2D Python lists to C++ vectors
	std::vector<std::vector<int>> vecA = populateArray(A);
	std::vector<std::vector<int>> vecB = populateArray(B);
	std::vector<std::vector<int>> vecC = matMult(vecA, vecB);

    // returns the result of the vector multiplication.
	return vecC;
}

/*
this is just for debugging purposes
void printVec(std::vector<std::vector<int>> vec) {
	for (auto row : vec) {
		for (auto val : row) {
			std::cout << val << " ";
		}
		std::cout << std::endl;
	}
}
*/

// this function accepts a Python list as an argument and converts it into a C++ vector.
std::vector<std::vector<int>> populateArray(py::list pyVec) {
	std::vector<std::vector<int>> vec;
	std::vector<int> vecRow;

	for (auto row : pyVec) {
                for (auto val : row) {
                        vecRow.push_back(val.cast<int>());
                        //std::cout << val.cast<int>() << " ";
                }
                vec.push_back(vecRow);
                vecRow.clear();
        }
	
	return vec;
}

// this function multiplies the 2 matrices given to it and returns the result.
std::vector<std::vector<int>> matMult(std::vector<std::vector<int>> A, std::vector<std::vector<int>> B) {
	std::vector<std::vector<int>> C;
	std::vector<int> row;
	int val = 0;

	for (int i = 0; i < A.size(); ++i) {
		for (int j = 0; j < B.size(); ++j) {
			for (int k = 0; k < A.size(); ++k) {
				val += A[i][k] * B[k][j];
			}
			row.push_back(val);
			val = 0;
		}
		C.push_back(row);
		row.clear();
	}
	return C;
}


// this code allows for the Pybind11 module to be created.
PYBIND11_MODULE(matMult, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("multiply", &multiply, "A function which multiplies two numbers");
}

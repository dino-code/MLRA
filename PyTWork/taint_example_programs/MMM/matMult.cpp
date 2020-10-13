//#include "pybind11/include/pybind11.h"
//#include <pybind11/include/stl.h>
#include <pybind11/pybind11.h>
#include <iostream>
#include <vector>

namespace py = pybind11;

std::vector<std::vector<int>> populateArray(py::list);
void printVec(std::vector<std::vector<int>>);
std::vector<std::vector<int>> matMult(std::vector<std::vector<int>>, std::vector<std::vector<int>>);
std::vector<int> convList (py::list);
std::vector<std::vector<int>> constr2DVec (std::vector<int>);

/*
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
*/

std::vector<std::vector<int>> multiply(py::list pyVec) {
    std::vector<int> data = convList(pyVec);
    
    std::vector<int> matOneBase;
    for (int i = 0; i < 9; ++i) matOneBase.push_back(data.at(i));
    //std::copy (matOneBase.begin(), data.begin(), data.begin() + 8);
    
    std::vector<int> matTwoBase;
    for (int i = 9; i < data.size(); ++i) matTwoBase.push_back(data.at(i));
    //std::copy (matTwoBase.begin(), data.begin() + 9, data.end()-1);
    
    std::vector<std::vector<int>> matOne = constr2DVec(matOneBase);
    std::vector<std::vector<int>> matTwo = constr2DVec(matTwoBase);
    
    //std::vector<std::vector<int>> matThree = matMult(matOne, matTwo);
    
    return matMult(matOne, matTwo);
    
}

std::vector<int> convList (py::list pyVec) {
    std::vector<int> data;
    
    for (auto element : pyVec) {
        data.push_back(element.cast<int>());
    }
    
    return data;
}

std::vector<std::vector<int>> constr2DVec (std::vector<int> vec) {
    std::vector<std::vector<int>> newVec;
    std::vector<int> row;
    
    int counter = 0;
    
    for (int i = 0; i < vec.size(); ++i) {
        
        row.push_back(vec.at(i));
        counter++;
        
        if (counter == 3) {
            newVec.push_back(row);
            row.clear();
            counter = 0;
        }
        
    }
        
    return newVec;
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


/*
std::vector<std::vector<int>> newPopArray(std::vector data) {
    std::vector<std::vector<int>> mat1;
    std::vector<std::vector<int>> mat2;
    std::vector<int> row;
    matSize = 9;
    currElement = 0;
    
    
    //for (int i = 0; i < matSize; ++i) {
        
    //}
    
    return pyVec[0]
}
*/

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
    //m.def("test", &test, "A test for search string")
}

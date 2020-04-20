4/8/2020

clang++ -std=c++11 -stdlib=libc++ -I/usr/local/opt/python/Frameworks/Python.framework/Versio
ns/3.7/include/python3.7m -L/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/lib -lpython3.7m main.cpp

This gets the c++ program to actually run. After encountering numerous errors, this finally gives me the result I'm looking for.
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

4/9/2020

For Pybind11, I need one .cpp file containing the function I want to import into my main_prog.py file (which is the file that runs my flask server). 

Tested the server and it still works. To run the server and test the Javascript/python frontend navigate to the directory containing main_prog.py via terminal.
Type:
export FLASK_APP=main_prog.py
flask run
Then copy the address from terminal into your browser.

clang++ -std=c++11 -stdlib=libc++ -c -I/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/include/python3.7m -L/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/lib -lpython3.7m matMult.cpp

c++ -O3 -Wall -shared -std=c++11 -I/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/include/python3.7m -L/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/lib -lpython3.7m -fPIC `python3 -m pybind11 --includes` matMult.cpp -o matMult`python3-config --extension-suffix`

Error returned: 

"Fatal Python error: PyMUTEX_LOCK(_PyRuntime.ceval.gil.mutex) failed

Abort trap: 6"


The error seems to happen at the import step. This was deduced via the following method:
- commented out matMult call to cpp function multiply within main_prog.py. The error was still reproduced.
- commented out multiply call and import matMult. Error ceased.

Now we know that the problem lies within the cpp file. So to test this:
- added a int main() {} function where I tested the multiply function by passing 3 and 4 to the function. This return 12 once compiled and worked perfectly. The following command was used to compile the new matMult.cpp:

c++ -std=c++11 -I/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/include/python3.7m -L/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/lib -lpython3.7m matMult.cpp


This means the problem lies in the created module.
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
4/10/2020

Met with Dr. Lyons today as usual during Friday meetings at 2PM. He read the Pybind11 documentation and it turns out the I was attempting to build based on a Linux system. For Mac OS, it's very important to add "-undefined dynamic_lookup" because without that, some symbols might not be recognized. This is why the error above was occurring.

Once we implemented that change, we used the following command:

c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup `python3 -m pybind11 --includes` matMult.cpp -o matMult`python3-config --extension-suffix`

The matMult.cpp source code then became a matMult Python package that can be imported into my main_prog.py program. Now I just need to implement the matrix multiplication and I will be good to go.
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

4/11/2020

Tonight I am working on applying the matrix multiplication algorithm to my matMult.cpp file and passing Python arguments to the file.

The current question I have is: will C++ be able to recognize the arrays I pass through Python? Let's test.

It did not work, but apparently, on the C++ side, I need to put the parameter type as py::list for each of the 2D lists that I'm going to be passing through to C++.

Now I am reading that I must include pybind11/stl.h to enable automatic conversion between python types and c++ vectors.

After some playing around with it, I figured it out. Basically, I am able to cast a Python object into a C++ type (https://pybind11.readthedocs.io/en/stable/advanced/pycpp/object.html). The code I've used is:

for (auto item : A) {
                std::cout << item.cast<int>() << " ";           
        }

In this, A is a list and each item within the list must be cast to a C++ type before it can be printed/utilized in C++. 

My plan is to now convert each row of each vector into a vector and then push them into vector<vector<int> that I constructed.

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

4/13/20

After putting together a few of the things I've learned, I came up with the following code:


for (auto row : A) {
                
                for (auto val : row) {
                        std::cout << val.cast<int>() << " ";
                }
        }  

This outputs all of the numbers in the matrix. Now I just need to put these numbers in a c++ 2d vector and then figure out how to return that 2d vector to Python. I will probably have to cast the c++ vector into a python object.

I have now managed to multiply the two lists within C++. I just have to convert the 2D vector into a python object and send it back.

Success! I managed to implement the C++ code and now the entire program multilingual program works. Now, I need to clean up the code and also work on figuring out how HTML forms are submitted.
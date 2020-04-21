4/20/20

Today, I begin working with PyT. The last thing I worked on was created a program that used a JavaScript frontend to collect user input that was then pushed to Python (where the Flask server was being run). From Python, the user input was carried into C++ via Pybind11 where an operation was performed. The result was then return to Python and then back to the JavaScript frontend.

The purpose of creating this program was so that we would have another example that we can run PyT on to generate a taint analysis. This brings me to my current purpose: get PyT working on my machine so that I can test it out on the example program I created.

I am going to begin by cloning the pyT repository to the PyTWork folder.

I ran all the tests by navigating to the pyt folder and typing "python3 -m pyt" and all the tests worked. I did hit a snag, though. Here's what I need to learn more about:
- What is output and where?
- Where is the trigger file?

I found a lead on the trigger files in this folder: /Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/PyTWork/pyt/pyt/vulnerability_definitions/

python3 -m pyt -t /Use
rs/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/PyTWork/pyt/pyt/vulnera
bility_definitions/all_trigger_words.pyt main_prog.py

yields "No vulnerabilities" 

------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------

4/21/20

Today I am going to start by looking at how PyT is used in the BitBucket MLRA repository.

Turns out that the BitBucket repository also yields "No vulnerabilities". Going to email Lyons and see.
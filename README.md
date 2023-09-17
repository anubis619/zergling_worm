# The Zergling worm
# NOTE: THIS IS FOR LEARNING PURPOSE ONLY!

![Zergling](Ch1Y0Z5.png)


The scope if this repository is not to create an actual malicious worm but rather to create a program that replicates itself as a worm would do to better understand how it functions.
At the same time it helps me apply and learn more about python.

Why did I call it the "Zergling Worm"?
 Well similar to how a zergling in StarCraft acts it will just do that it is ordered by the "hive mind", in this scenario the code. Also zerglings are a unit in StarCraft that can normally outrun you in terms of number as in the game from one egg two will spawn. So same as in the game this code will spawn another one that run the code and so on.


# TODO

* The actual code of the "worm"
    * The idea is to write to a file "Hello from Zergling Worm ran from <application_name>
* The code should do the following:
  * Create a file with a random name
  * Add the code from the script inside that file
  * Write to file the hello part
  * call to run the newly created application.
* Basically this would create an infinite loop as it is right now and will continue to create files and run then until either the system crashes, runs out of space, or machine is booted of.
  * Due to the above I will run this learning code inside a VM so it does not affect my main machine
* **Enhancements:**
  * Make the app reach out to a server.
  * Check if it can ping it
  * If it can ping it then try to authenticate in order to update a file there. 
    * See how that can be done
  * If it fails to authenticate or the server is unreachable stop the code from running the next part which is duplicating it's code to a new file and run that file.


---
# NOTE: THIS IS FOR LEARNING PURPOSE ONLY!
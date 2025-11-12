# Scope of variables

#
# All variables in a program may not be accessible at
# all locations in that program. This depends on where
# you have declared a variable.


# Global variables
# Local variables


total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)
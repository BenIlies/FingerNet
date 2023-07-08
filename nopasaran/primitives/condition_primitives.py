from nopasaran.decorators import parsing_decorator

class ConditionPrimitives:
    """
    Class containing condition primitives for the state machine.
    """

    @staticmethod
    @parsing_decorator(input_args=2, output_args=0)
    def equal(inputs, outputs, state_variables):
        """
        Check if two values in the state variables are equal.

        Number of input arguments: 2
        
        Number of output arguments: 0
        
        Optional input arguments: No
        
        Optional output arguments: No

        Args:
            inputs (List[str]): The list of input variable names. It contains two mandatory input arguments, which are the names of the variables to be compared.
            
            outputs (List[str]): The list of output variable names.
            
            state_variables (dict): The dictionary of state variables.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return state_variables[inputs[0]] == state_variables[inputs[1]]

    @staticmethod
    @parsing_decorator(input_args=2, output_args=0)
    def gt(inputs, outputs, state_variables):
        """
        Check if the first value in the state variables is greater than the second value.

        Number of input arguments: 2
        
        Number of output arguments: 0
        
        Optional input arguments: No
        
        Optional output arguments: No

        Args:
            inputs (List[str]): The list of input variable names. It contains two mandatory input arguments, which are the names of the variables to be compared.
            
            outputs (List[str]): The list of output variable names.
            
            state_variables (dict): The dictionary of state variables.

        Returns:
            bool: True if the first value is greater, False otherwise.
        """
        return state_variables[inputs[0]] > state_variables[inputs[1]]

    @staticmethod
    @parsing_decorator(input_args=2, output_args=0)
    def gte(inputs, outputs, state_variables):
        """
        Check if the first value in the state variables is greater than or equal to the second value.

        Number of input arguments: 2
        
        Number of output arguments: 0
        
        Optional input arguments: No
        
        Optional output arguments: No

        Args:
            inputs (List[str]): The list of input variable names. It contains two mandatory input arguments, which are the names of the variables to be compared.
            
            outputs (List[str]): The list of output variable names.
            
            state_variables (dict): The dictionary of state variables.

        Returns:
            bool: True if the first value is greater or equal, False otherwise.
        """
        return state_variables[inputs[0]] >= state_variables[inputs[1]]

    @staticmethod
    @parsing_decorator(input_args=2, output_args=0)
    def lt(inputs, outputs, state_variables):
        """
        Check if the first value in the state variables is less than the second value.

        Number of input arguments: 2
        
        Number of output arguments: 0
        
        Optional input arguments: No
        
        Optional output arguments: No

        Args:
            inputs (List[str]): The list of input variable names. It contains two mandatory input arguments, which are the names of the variables to be compared.
            
            outputs (List[str]): The list of output variable names.
            
            state_variables (dict): The dictionary of state variables.

        Returns:
            bool: True if the first value is less, False otherwise.
        """
        return state_variables[inputs[0]] < state_variables[inputs[1]]

    @staticmethod
    @parsing_decorator(input_args=2, output_args=0)
    def lte(inputs, outputs, state_variables):
        """
        Check if the first value in the state variables is less than or equal to the second value.

        Number of input arguments: 2
        
        Number of output arguments: 0
        
        Optional input arguments: No
        
        Optional output arguments: No

        Args:
            inputs (List[str]): The list of input variable names. It contains two mandatory input arguments, which are the names of the variables to be compared.
            
            outputs (List[str]): The list of output variable names.
            
            state_variables (dict): The dictionary of state variables.

        Returns:
            bool: True if the first value is less or equal, False otherwise.
        """
        return state_variables[inputs[0]] <= state_variables[inputs[1]]

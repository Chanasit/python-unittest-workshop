import logging
import time

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)


# Define a decorator that logs the input, output, and execution time of a function
def log(func):
    # Define a wrapper function that takes any number of arguments
    def wrapper(*args, **kwargs):
        # Get the current time before calling the function
        start = time.time()
        # Call the original function and store the output
        result = func(*args, **kwargs)
        # Get the current time after calling the function
        end = time.time()
        # Calculate the elapsed time
        elapsed = end - start
        # Log the input, output, and execution time
        logging.debug(f"func: {args}")
        logging.debug(f"input: {kwargs}")
        logging.debug(f"output: {result}")
        logging.debug(f"time: {elapsed} seconds")
        # Return the output
        return result

    # Return the wrapper function
    return wrapper

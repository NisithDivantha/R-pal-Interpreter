from CSEmachine.compiler import Evaluvator
import sys
import os

def main():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file_name = os.path.join(project_dir, "test program.txt")

    # Call the evaluate method to get the answer
    answer = Evaluvator.evaluate(input_file_name)


    print("Output of the above program is: ", answer)

if __name__ == "__main__":
    main()

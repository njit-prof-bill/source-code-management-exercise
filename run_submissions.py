import glob
import importlib.util
import os


def run_gcd_test(gcd_func, a, b, expected):
    """
    Runs a test case for the gcd function.
    """
    result = gcd_func(a, b)
    if result == expected:
        print(f"PASS: gcd({a}, {b}) = {result}")
    else:
        print(f"FAIL: gcd({a}, {b}) = {result}, expected {expected}")


def load_and_run():
    """
    Detect and run all student submissions from the students_submissions directory.
    Each student's submission is expected to be in a file named gcd_<GitHubUsername>.py.
    """
    # Find all the files in the students_submissions directory matching the pattern gcd_*.py
    student_files = glob.glob("students_submissions/gcd_*.py")

    for file in student_files:
        # Extract the student's GitHub username or identifier from the filename
        module_name = os.path.splitext(os.path.basename(file))[0]

        # Dynamically import the student's module
        spec = importlib.util.spec_from_file_location(module_name, file)
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)

        # Check if the gcd function exists in the student's submission
        if hasattr(student_module, "gcd"):
            print(f"Running {module_name}'s submission...")
            gcd_func = getattr(student_module, "gcd")

            # Run a set of test cases
            run_gcd_test(gcd_func, 54, 24, 6)
            run_gcd_test(gcd_func, 48, 18, 6)
            run_gcd_test(gcd_func, 101, 10, 1)
            run_gcd_test(gcd_func, 270, 192, 6)
            print()
        else:
            print(f"ERROR: {module_name}'s submission does not have a gcd function\n")


if __name__ == "__main__":
    load_and_run()

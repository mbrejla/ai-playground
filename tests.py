from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.call_function import call_function

# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "pkg"))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))
# print(get_files_info("calculator"))
# print(get_files_info("calculator", "main.py"))
# print(get_files_info(None, "main.py"))

# print(get_file_content("calculator", "lorem.txt"))
# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "/bin/cat"))
# print(get_file_content("calculator", "bin"))


# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
#
# print(run_python_file("calculator", "main.py"))
# print(run_python_file("calculator", "lorem.txt"))
# print(run_python_file("calculator", "exit_test.py"))
# print(run_python_file("calculator", "tests.py"))
# print(run_python_file("calculator", "../main.py"))
# print(run_python_file("calculator", "nonexistent.py"))
#
#
#


class Func:
    name = "get_files_info"
    args = {"directory": "."}


class Func01:
    name = "write_file"
    args = {"file_path": "test/main.txt", "content": "hello"}


class Func02:
    name = "get_f_content"
    args = {"file_path": "main.txt", "content": "hello"}


func = Func()
func01 = Func01()
func02 = Func02()
print(call_function(func02))
result = call_function(func01, True)
print(result.parts[0].function_response.response)
print(call_function(func))

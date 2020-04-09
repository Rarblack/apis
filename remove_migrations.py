import os
import glob

file_list = glob.glob("C:\\Users\\ABagiyev\\PycharmProjects\\apis\\**\\migrations\\*.py", recursive=True)
file_exact_path = glob.glob("C:\\Users\\ABagiyev\\PycharmProjects\\apis\\db.sqlite3")


# deleting migrations
if len(file_list) != 0:

    for file_path in file_list:

        try:

            file_path_split = file_path.split("\\")

            file_in_destination = file_path_split[-1]

            if "venv" in file_path_split or "Lib" in file_path_split:
                continue

            if file_in_destination == "__init__.py":
                continue

            os.remove(file_path)
            print("file removed %s" % file_in_destination)

        except OSError:
            print("Error while deleting %s" % file_path)

else:
    print('migrations are already deleted')

# deleting db.sqlite3 file
try:

    if len(file_exact_path) != 0:

        file_exact_split = file_exact_path[0].split("\\")
        file_exact = file_exact_split[-1]

        os.remove(file_exact)

        print('file removed %s' % file_exact)

    else:
        print('db.sqlite3 is already deleted')

except OSError:
    print("Error while deleting %s" % file_exact_path)


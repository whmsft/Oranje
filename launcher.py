import os
import yaml
from package.whmsft import oranje

CURRENT_WORKING_DIRECTORY = os.getcwd()
PROGRAM_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
GLOBAL = {}
PACKAGE = {}
"""
How the "PACKAGE" dict will look like:
PACKAGE = {
    'whmsft': {
        'oranje': {...} With all data in `data.yml` of the package
    }
}
"""

def packageLookout():
    print("(log) looking for packages")
    for author in os.listdir(f'{PROGRAM_DIRECTORY}/package'):
        if os.path.isdir(f'{PROGRAM_DIRECTORY}/package/{author}'):
            PACKAGE[author] = {}
    for author in PACKAGE.keys():
        for pack in os.listdir(f'{PROGRAM_DIRECTORY}/package/{author}'):
            if (os.path.isdir(f'{PROGRAM_DIRECTORY}/package/{author}/{pack}')):
                if not (author == "whmsft" and pack == "oranje"):
                    print(f"(log) PACKAGE: found {author}.{pack}")
                    package_data = yaml.safe_load(open(f'{PROGRAM_DIRECTORY}/package/{author}/{pack}/data.yml').read())
                    PACKAGE[author][pack] = package_data
                    import_statement = f'import package.{author}.{pack}'
                    exec(import_statement)
                    task_list = package_data['tasks']
                    if ('initialize' in task_list) and (task_list['initialize'] is not None):
                        print(f"(log) PACKAGE: initialize package {author}.{pack}")
                        initialize_statement = f'package.{author}.{pack}.{task_list["initialize"]}'
                        exec(initialize_statement)
                    del task_list

def packageInjectGLOBAL():
    for author in PACKAGE.keys():
        for pack in os.listdir(f'{PROGRAM_DIRECTORY}/package/{author}'):
            if not (author == "whmsft" and pack == "oranje"):
                if ('GLOBAL_dictionary' in PACKAGE[author][pack]) and (PACKAGE[author][pack]["GLOBAL_dictionary"] is not None):
                    global_inject_statement = f'package.{author}.{pack}.{PACKAGE[author][pack]["GLOBAL_dictionary"]} = PACKAGE'
                    print(f'(log) PACKAGE: Inject GLOBAL variable to package.{author}.{pack}.{PACKAGE[author][pack]["GLOBAL_dictionary"]}')
                    exec(global_inject_statement)

def checkoutBefore():
    for author in PACKAGE.keys():
        for pack in PACKAGE[author].keys():
            task_list = PACKAGE[author][pack]['tasks']
            if ('beforeLoop' in task_list) and (task_list['beforeLoop'] is not None):
                before_loop_statement = f'package.{author}.{pack}.{task_list["beforeLoop"]}'
                print(f"(log) PACKAGE: beforeLoop package {author}.{pack}")
                exec(before_loop_statement)
            del task_list

def checkoutAfter():
    for author in PACKAGE.keys():
        for pack in PACKAGE[author].keys():
            task_list = PACKAGE[author][pack]['tasks']
            if ('afterLoop' in task_list) and (task_list['afterLoop'] is not None):
                after_loop_statement = f'package.{author}.{pack}.{task_list["afterLoop"]}'
                print(f"(log) PACKAGE: afterLoop package {author}.{pack}")
                exec(after_loop_statement)
            del task_list

if __name__ == "__main__":
    packageLookout()
    packageInjectGLOBAL()
    checkoutBefore()
    oranje.editor.mainloop()
    checkoutAfter()

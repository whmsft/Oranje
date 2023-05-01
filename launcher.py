print("Welcome, This is Oranje Editor executable")
import os
import yaml
from package.whmsft import oranje

cwd = os.getcwd()
pdir = os.path.dirname(os.path.realpath(__file__))

PACKAGE = {}
"""
How the "PACKAGE" dict will look like:
PACKAGE = {
	'whmsft': {
		'oranje': {...} With all data in `data.yml` of the package
		}
	}
}
"""

if __name__ == "__main__":
	print("(log) looking for packages")
	for author in os.listdir(f'{pdir}/package'):
		if os.path.isdir(f'{pdir}/package/{author}'):
			PACKAGE[author] = {}
	for author in PACKAGE.keys():
		for pack in os.listdir(f'{pdir}/package/{author}'):
			if (os.path.isdir(f'{pdir}/package/{author}/{pack}')):
				if not (author == "whmsft" and pack == "oranje"):
					print(f"(log) PACKAGE: found {author}.{pack}")
					PACKAGE[author][pack] = yaml.safe_load(open(f'{pdir}/package/{author}/{pack}/data.yml').read())
					exec(f'import package.{author}.{pack}')
					taskList = PACKAGE[author][pack]['tasks']
					if ('initialize' in taskList) and (taskList['initialize'] != None):
						print(f"(log) PACKAGE: initialize package {author}.{pack}")
						exec(f'package.{author}.{pack}.{taskList["initialize"]}')
					del taskList
	GLOBAL["PACKAGE"] = PACKAGE
	for author in PACKAGE.keys():
		for pack in PACKAGE[author].keys():
			taskList = PACKAGE[author][pack]['tasks']
			if ('beforeLoop' in taskList) and (taskList['beforeLoop'] != None):
				print(f"(log) PACKAGE: beforeLoop package {author}.{pack}")
				exec(f'package.{author}.{pack}.{taskList["beforeLoop"]}')
			del taskList
	oranje.editor.mainloop()
	for author in PACKAGE.keys():
		for pack in PACKAGE[author].keys():
			taskList = PACKAGE[author][pack]['tasks']
			if ('afterLoop' in taskList) and (taskList['afterLoop'] != None):
				print(f"(log) PACKAGE: afterLoop package {author}.{pack}")
				exec(f'package.{author}.{pack}.{taskList["afterLoop"]}')
			del taskList

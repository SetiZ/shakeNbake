from PythonTools import *

package_name = 'shakeNbake'

setup(name='shakeNbake',
	  version='0.1',
	  description='Music hack day 2014',
	  author='Sovanski, Mehdilovski',
	  author_email='hak.sovannara@gmail.com',
	  package_dir={package_name:'src'},
	  packages=[package_name],
	  package_data={package_name: []},
	  cmdclass=cmdclass,

	  script_name=script_name,
	  script_args= script_args
	 )

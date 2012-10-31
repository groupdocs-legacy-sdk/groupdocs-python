from distutils.core import setup

if __name__ == '__main__':
	import sys

	setup(
		name = 'groupdocs-python',
		version = '1.1',

		author = "GroupDocs Team",
		author_email = "support@groupdocs.com",
		description = "A Python interface to the GroupDocs API",
		keywords = "groupdocs, document management, viewer, annotation, signature",
		license = "Python license",
		long_description = """This package implements an interface to the GroupDocs
		API, defined at http://groupdocs.com/api.""",
		platforms = 'any',
		packages = ['groupdocs', 'groupdocs.models'],
		url = "http://groupdocs.com/",
		download_url = "https://github.com/groupdocs/groupdocs-python",
		classifiers = [
			"Development Status :: 4 - Beta",
			"Intended Audience :: Developers",
			"Operating System :: OS Independent",
			"Programming Language :: Python",
			"Topic :: Software Development :: Libraries :: Python Modules",
		]
	)

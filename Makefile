# Copyright (C) 2012 Robert Fielding
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose with or without fee is hereby granted,
# provided that the above copyright notice and this permission notice
# appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND NOMINUM DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL NOMINUM BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

PYTHON=python

all:
	${PYTHON} ./setup.py build

install:
	${PYTHON} ./setup.py install

clean:
	${PYTHON} ./setup.py clean --all
	find . -name '*.pyc' -exec rm {} \;
	find . -name '*.pyo' -exec rm {} \;
	rm -f TAGS

distclean: clean docclean
	rm -rf build dist
	rm -f MANIFEST

doc:
	epydoc -v -n pyacter -u http://www.pyacter.org pyacter/*.py

dockits: doc
	mv html pyacter-html
	tar czf html.tar.gz pyacter-html
	zip -r html.zip pyacter-html
	mv pyacter-html html

docclean:
	rm -rf html.tar.gz html.zip html

kits:
	${PYTHON} ./setup.py sdist --formats=gztar,zip
#	${PYTHON} ./setup.py bdist_wininst
#	${PYTHON} ./setup.py bdist_rpm

tags:
	find . -name '*.py' -print | etags -

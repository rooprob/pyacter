# Copyright (c) 2012, Robert Fielding <rf@tamasi.org> 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.  
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.  
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

PYTHON=python

all:
	${PYTHON} ./setup.py build

install:
	${PYTHON} ./setup.py install

test:
	${PYTHON} -m unittest discover -s tests
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

# install the library into system python
setup:
	rm -fr ./dist
	# find the most recent wheel to install
	poetry build && pip3 install `ls -tr dist/*.whl | tail -1` --force-reinstall

.PHONY: setup 

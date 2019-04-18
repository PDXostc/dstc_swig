#
# Makefile to generate python interface code for DSTC
#

CFLAGS += -ggdb
DSTC_DIR ?= /usr/local/
dstc_swig_wrap.o: dstc_swig_wrap.c
	python3 setup.py build_ext --inplace  -I${DSTC_DIR}/include

dstc_swig_wrap.c: dstc_swig.i
	swig -I${DSTC_DIR}/include -python -includeall dstc_swig.i

clean:
	rm -rf _dstc*.so build dstc_swig.py dstc_swig_wrap.* __pycache__ \
	dist jlr_dstc.egg-info *~

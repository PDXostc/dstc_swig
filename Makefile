#
# Makefile to generate python interface code for DSTC
#
.PHONY: all clean 

CFLAGS += -ggdb
INC_DIRS ?= -I/usr/local/

OBJ = dstc_swig_wrap.o
SRC = dstc_swig_wrap.c
SWIG = dstc_swig.i

$(OBJ): $(SRC)
	python3 setup.py build_ext --inplace $(INC_DIRS)

$(SRC): $(SWIG)
	swig $(INC_DIRS) -python -includeall $(SWIG)

clean:
	rm -rf _dstc*.so build dstc_swig.py dstc_swig_wrap.* __pycache__ \
	dist jlr_dstc.egg-info *~

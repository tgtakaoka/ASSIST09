AS=asm -v -n -C 6809

%.S19:	%.ASM
	$(AS) -l $*.LST -o $*.S19 $^

.PHONY: clean distclean

all: ASSIST09.S19

clean:
	-rm -f *.LST
distclean: clean
	-rm -f *.S19

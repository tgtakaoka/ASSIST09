AS=asm -C 6809 -n -u

%.S19:	%.ASM
	$(AS) -l $*.LST -o $*.S19 $^

.PHONY: clean

all: ASSIST09.S19

clean:
	-rm -f *.p *.lst *.S19

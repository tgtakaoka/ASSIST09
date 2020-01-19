AS=asm6809

%.S19:	%.ASM
	$(AS) -s9 -o $*.S19 -l $*.LST $^

.PHONY: clean

all: ASSIST09.S19

clean:
	-rm -f *.S19 *.LST

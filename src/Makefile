AS=asl -gnuerrors -L +t 0x0c -q -cpu 6809
OBJCOPY=p2hex -l 32 -F Moto +5 -r '$$-$$'

%.p:	%.ASM
	$(AS) $^
%.S19:	%.p
	$(OBJCOPY) $^
	@mv $*.hex $*.S19

.PHONY: clean

all: ASSIST09.S19

clean:
	-rm -f *.p *.lst *.S19

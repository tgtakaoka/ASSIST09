AS=asl -gnuerrors -L +t 0x0c -q -cpu 6809
OBJCOPY=p2hex -k -l 32 -F Moto +5 -r '$$-$$'

%.p:	%.ASM
	$(AS) -olist $*.LST $^
%.S19:	%.p
	$(OBJCOPY) $^ $@

.PHONY: clean distclean

all: ASSIST09.S19

clean:
	-rm -f *.LST
distclean: clean
	-rm -f *.S19

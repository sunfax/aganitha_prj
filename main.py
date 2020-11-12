
from rules import get_rules

from front_last import check_front_last

from sp2wr import SpokenToWritten

def conv_sp2wr():
    spoken=SpokenToWritten()
    spoken.get_user_input()
    spoken.Convert()


    spoken.show_output()

conv_sp2wr()

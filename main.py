
from rules import get_rules

from front_last import check_front_last

from sp2wr import SpokenToWritten

def convert_sp_to_wr():
    spoken=SpokenToWritten()
    spoken.get_user_input()
    spoken.Convert()


    spoken.show_output()

convert_sp_to_wr()
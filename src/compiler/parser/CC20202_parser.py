"""Parser for CC-2020-2 language"""
import os

from utils.cfg_processor import CfgProcessor
from utils.data_structures import Token, SymbolsTable


class CC20202Parser:
    def __init__(self):
        curr_file_folder = os.path.basename(__file__)
        grammar_path = os.path.join(curr_file_folder,
                                    '..',
                                    'grammar',
                                    'ConvCC-2020-2.csf')

        cfg_proc = CfgProcessor()
        cfg_proc.read(grammar_path)

        self.mat = cfg_proc.generate_matrix()

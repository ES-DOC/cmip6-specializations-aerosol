# -*- coding: utf-8 -*-

"""
.. module:: generate_ids_level_2.py
   :platform: Unix, Windows
   :synopsis: Generates level 2 identifiers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from generate_ids import Generator as IdentifierGenerator



class Generator(IdentifierGenerator):
    """Specialization to mindmap generator.

    """
    def on_grid_parsed(self, grid):
        """On grid parsed event handler.

        """
        self.emit_null_row(grid)


    def on_keyproperties_parsed(self, key_properties):
        """On key_properties parsed event handler.

        """
        self.emit_null_row(key_properties)


    def on_process_parsed(self, process):
        """On process parsed event handler.

        """
        self.emit_null_row(process)


    def on_detailset_parse(self, detail_set):
        """On process detail set parse event handler.

        """
        self.set_id(detail_set)
"""
Note class
"""

from json_util import read_json


class Note:

    # This data was taken from:
    #   http://pages.mtu.edu/~suits/notefreqs.html
    # It considers A4 to be 440Hz as standard tunning
    __ranges = read_json("notes_freqs.json")

    @staticmethod
    def get_note_frequency(range, note):
        """
        Returns note frequency
        
        :param range: Piano scale range 
        :type range: str
        :param note: Piano note 
        :type note: str
        :return: Note frequency
        :rtype: float
        """
        return Note.__ranges[str(range)][note]

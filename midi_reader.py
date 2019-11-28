from mido import MidiFile, MidiTrack, Message, MetaMessage
from keras.callbacks import callbacks
import numpy as np
import os #to get current path

def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	getNoteRangeAndTicks("prueba.mid")

def getNoteRangeAndTicks(files_dir, res_factor=1):
	print("my path is: ", files_dir, "\n")
	ticks = []
	notes = []
	for file_dir in files_dir:
		file_path = "%s" %(file_dir)
		print("trying to open", files_dir)
		mid = MidiFile(files_dir)

		for track in mid.tracks: #preprocessing: Checking range of notes and total number of ticks
			num_ticks = 0
			for message in track:
				if not isinstance(message, MetaMessage):
					notes.append(message.note)  # aquí me dice que no hay un atributo llamado note
					print(message)
					num_ticks += int(message.time/res_factor)
			ticks.append(num_ticks)

	return min(notes), max(notes), max(ticks) 

if __name__ == "__main__":
	main()

from pytgress import indeterminate
import time

spinner = indeterminate.braille_spinner()

for i in range(100):
	spinner.update()        # update after each time-step
	time.sleep(0.1)			# sleep for 0.1seconds
	spinner.show()          # show current state
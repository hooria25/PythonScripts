import time

phrase = 'Hooria watches John Wick'
word_count = len(phrase.split())
begin = input('Please type: ' + phrase + '\n' + 'Press enter when you are ready.' + '\n')

# calling the time module below
t0 = time.time()
# Takes the input and puts it inside attempt
attempt = input('\n')
# This will track the end time
t1= time.time()

#calculating the lengths in seconds by subtracting start time and end time and dividing by 60
attempt_time = (t1 - t0)/60
wordsPerMinute = str(round(word_count / attempt_time, 1))

if attempt == phrase:
	print('\n' + 'Your words per minutes (wpm)' + wordsPerMinute)
else:
	print('\n'+ 'Typed incorrectly, Please try again')
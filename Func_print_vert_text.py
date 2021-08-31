def vertical_text(string):
	amount = len(string)
	to_print = iter(string)
	while amount:
		try: 
			print(next(to_print))
		except Exception as not_work:
			break
			
			
			
			
vertical_text('When they knew it was past the due date, it was still a question of how to effectively complete the task')


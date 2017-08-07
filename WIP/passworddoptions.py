def passwdopt():
	passw = list(raw_input())
	for i in range(len(passw)):
		print passw[i]
		for j in range(len(passw)):
			print j
			passw[i], passw[j] = passw[j], passw[i]
			print ' ' .join(passw)

			#print passw


passwdopt()

def calendario(mes, ano):
  import calendar
	from calendar import monthcalendar
	m = monthcalendar(ano,mes)
	m = map(str,m)
	encab = [['L','M','I','J','V','S','D'],['-','-','-','-','-','-','-']]
	l1 = "    ".join(encab[0])
	l2 = "    ".join(encab[1])
	l3 = "    ".join(list(map(str, m[0])))
	l4 = "    ".join(list(map(str, m[1])))
	l5 = "    ".join(list(map(str, m[2])))
	l6 = "    ".join(list(map(str, m[3])))
	l7 = "    ".join(list(map(str, m[4])))

	print(l1+"\n"+l2+"\n"+l3+"\n"+l4+"\n"+l5+"\n"+l6+"\n"+l7)

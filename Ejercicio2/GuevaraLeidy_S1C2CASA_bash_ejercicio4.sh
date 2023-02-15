mkdir Tolima
cp PlotsTolima.py Tolima
cp DatosTolima.dat Tolima
cd Tolima
awk  '{
	if (($1 =="2006") || ($1 =="2007") || ($1 =="2008")|| ($1 =="2009") || ($1 =="2010") || ($1 =="2011") || ($1 =="2012") || ($1 =="Year"))
		{print $2, $5, $7} 
	else {print $1, $4, $6}

	}' DatosTolima.dat > aux.txt 
awk '{
	if ($1 =="March")
		{print $2, $3} 
	}' aux.txt > DatosMarzo.txt
awk '{
	if ($1 != "Month")
		{print $2, $3} 
	}' aux.txt > GRS_vs_EQ.txt
rm aux.txt 
python3 PlotsTolima.py
rm DatosTolima.dat

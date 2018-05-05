import cgi

print "<html><body>"

form = cgi.FieldStorage()
choose_pattern = form["sentEpisode"].value

form_ok = 0

if form.has_key("name") and form.has_key("address") and form.has_key("episode"):
  form_ok = 1
if form_ok == 0 :
  print "<h1>ERROR</h1>"
else :
  print ("Content-type:episode.html")
  print() 

print "</body></html>

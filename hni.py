import webbrowser

message="""<html>
<head></head>
<body><p>Hello World</p><body>
<html>"""
with open('helloworld.html','w') as f:
    f.write(message)
    f.close()

webbrowser.open_new_tab('helloworld.html')
html_content = """
<!DOCTYPE html>
<html>
<head>
<title>My Web Page</title>
</head>
<body>
<h1>Welcome to My Web Page</h1>
<p>This is a paragraph on my web page!</p>
</body>
</html>
"""

# Write the HTML content to an HTML file
with open('my_web_page.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML page generated successfully!")

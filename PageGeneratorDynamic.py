from jinja2 import Template

template_content = """
<!DOCTYPE html>
<html>
<head>
<title>{{ title }}</title>
</head>
<body>
<h1>{{ heading }}</h1>
{% for paragraph in paragraphs %}
<p>{{ paragraph }}</p>
{% endfor %}
</body>
</html>
"""

data = {
    "title": "My Web Page",
    "heading": "Welcome to My Web Page",
    "paragraphs": [
        "This is the first paragraph on my web page!",
        "Here's another paragraph, full of content.",
    ]
}

template = Template(template_content)
html_content = template.render(data)

with open('my_web_page.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML page with dynamic content generated successfully!")

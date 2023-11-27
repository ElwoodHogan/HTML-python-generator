import random
from jinja2 import Template

def generate_random_rgb():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Function to convert RGB tuple to a string suitable for CSS
def rgb_to_string(rgb_tuple):
    return "rgb({0}, {1}, {2})".format(*rgb_tuple)

# Generate random RGB values for text and background colors
text_color_rgb = generate_random_rgb()
background_color_rgb = generate_random_rgb()

# Convert the RGB tuples to strings for CSS
text_color_css = rgb_to_string(text_color_rgb)
background_color_css = rgb_to_string(background_color_rgb)

template_content = """
<!DOCTYPE html>
<html>
<head>
<title>{{ title }}</title>
<style>
body {
    background-color: {{ background_color }};
    color: {{ text_color }};
}
</style>
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
    ],
    "text_color": text_color_css,
    "background_color": background_color_css
}

template = Template(template_content)
html_content = template.render(data)

with open('my_web_page.html', 'w') as html_file:
    html_file.write(html_content)

# Now you can use `text_color_rgb` and `background_color_rgb` later in your code
# For example, you might want to print them
print("Text Color RGB:", text_color_rgb)
print("Background Color RGB:", background_color_rgb)
print("HTML page with random RGB text and background colors generated successfully!")

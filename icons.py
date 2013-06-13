#This scripts read the icons.txt file to update the example page
tpl = """<li><i class="%s"></i> <span class="icon-name">%s</span></li>"""
html = ""
icons = open('icons.txt').read()
for icon in icons.split('\n'):
    html += tpl%(icon, icon) + "\n"

print html

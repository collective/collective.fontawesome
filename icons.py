#This scripts read the icons.txt file to update the example page
tpl = """<li><i class="fa %s"></i> <span class="icon-name">%s</span></li>"""
html = ""
icons = open('icons.txt').read().splitlines()
for icon in icons:
    html += tpl%(icon, icon) + "\n"

print html

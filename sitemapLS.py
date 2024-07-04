# -*- coding: utf-8 -*-
"""
@author: lovro
@version 0.1.0
"""

import xml.etree.ElementTree as ET


def load_sitemap(file_path):
    tree = ET.parse(file_path)
    return tree


def iterate_url(tree):
    canonical = ["Music", "Utilities", "Assets"]
    root = tree.getroot()
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for url in root.findall('ns:url', namespace):
        loc = url.find('ns:loc', namespace)
        priority = url.find('ns:priority', namespace)
        loc_text = loc.text

        for can in canonical:
            if can in loc_text and 'index.php' in loc_text:
                new_loc = loc_text.replace('index.php', '')
                loc.text = new_loc
                priority.text = '1.00'

        print(f"loc: {loc.text} priority: {priority.text}")


def save_sitemap(tree, file_path):
    tree.write(file_path, encoding='utf-8', xml_declaration=True)


def main():
    file_path = 'sitemap.xml'
    tree = load_sitemap(file_path)
    iterate_url(tree)
    save_sitemap(tree, file_path)


if __name__ == "__main__":
    main()

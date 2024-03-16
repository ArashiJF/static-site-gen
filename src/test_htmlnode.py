import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_props_empty(self):
        node = HTMLNode(None, None, None, None)
        props_string = ""
        self.assertEqual(node.props_to_html(), props_string)

    def test_to_props_eq(self):
        node = HTMLNode(None, None, None, { "href": "https://www.google.com" })
        props_string = '''href="https://www.google.com"'''
        self.assertEqual(node.props_to_html(), props_string)

        node2 = HTMLNode(None, None, None, { "href": "https://www.google.com", "target": "_blank" })
        props_string2 = '''href="https://www.google.com" target="_blank"'''
        self.assertEqual(node2.props_to_html(), props_string2)

    def test_to_props_uneq(self):
        node = HTMLNode(None, None, None, { "href": "https://www.google.com" })
        props_string = ''' href="https://www.google.com" '''
        self.assertNotEqual(node.props_to_html(), props_string)

if __name__ == "__main__":
    unittest.main()

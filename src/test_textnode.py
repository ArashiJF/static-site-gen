import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", "bold")

        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a link node", "link")
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)

if __name__ == "__main__":
    unittest.main()

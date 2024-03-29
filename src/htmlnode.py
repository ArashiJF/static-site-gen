class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop_string = ""

        if not self.props:
            return ""

        for prop in self.props:
            prop_string += f'''{prop}="{self.props[prop]}"\n'''

        return " ".join(
            prop_string.split("\n")[:-1]
        )
    
    def __repr__(self):
        return f'''HTMLNode
tag: {self.tag}
value: {self.value}
children: {self.children}
props: {self.props}'''
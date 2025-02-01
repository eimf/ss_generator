class HTMLNode:
    def __init__(self, tag: str, value: str, children: list, props: dict):
        self.tag = tag or None
        self.value = value or None
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError
        # return f"<{self.tag} {self.props}>{self.value}</{self.tag}>"

    def props_to_html(self):
        return "".join([f' {k}="{v}"' for k, v in self.props.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict):
        super().__init__(tag, value, [], props)

    # If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
    # If there is no tag (e.g. it's None), the value should be returned as raw text.
    # Otherwise, it should render an HTML tag.
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
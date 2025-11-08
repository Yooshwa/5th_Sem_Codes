from graphviz import Digraph

# Create ER diagram using Graphviz
er = Digraph('ER', filename='sweetkart_er_diagram', format='png')
er.attr(rankdir='LR', size='10')

# Entity function
def entity(name, attributes):
    with er.subgraph(name='cluster_' + name) as c:
        c.attr(label=name, shape='box')
        for attr in attributes:
            if "(PK)" in attr:
                c.node(name + "_" + attr, attr, shape="ellipse", color="red")  # Primary key in red
            elif "(FK" in attr:
                c.node(name + "_" + attr, attr, shape="ellipse", color="blue") # Foreign key in blue
            else:
                c.node(name + "_" + attr, attr, shape="ellipse")

# Define entities with attributes
entity("Admin", ["admin_id (PK)", "name", "email", "password"])
entity("Vendor", ["vendor_id (PK)", "name", "shop_name", "email", "password", "status"])
entity("User", ["user_id (PK)", "name", "email", "password", "address", "phone"])
entity("Category", ["category_id (PK)", "name", "description"])
entity("Product", ["product_id (PK)", "vendor_id (FK)", "category_id (FK)", "name", "description", "price", "availability_status"])
entity("Order", ["order_id (PK)", "user_id (FK)", "order_date", "status", "total_amount"])
entity("Order_Items", ["order_item_id (PK)", "order_id (FK)", "product_id (FK)", "quantity", "customization_details"])
entity("Payment", ["payment_id (PK)", "order_id (FK)", "amount", "method", "status", "payment_date"])
entity("Feedback", ["feedback_id (PK)", "user_id (FK)", "product_id (FK)", "rating", "comment", "feedback_date"])

# Define relationships (diamonds)
def relation(name, from_entity, to_entity):
    er.node(name, name, shape="diamond")
    er.edge(from_entity, name)
    er.edge(name, to_entity)

# Relationships
relation("manages", "Admin_admin_id (PK)", "Vendor_vendor_id (PK)")
relation("manages", "Vendor_vendor_id (PK)", "Product_product_id (PK)")
relation("belongs_to", "Product_product_id (PK)", "Category_category_id (PK)")
relation("places", "User_user_id (PK)", "Order_order_id (PK)")
relation("contains", "Order_order_id (PK)", "Order_Items_order_item_id (PK)")
relation("refers_to", "Order_Items_order_item_id (PK)", "Product_product_id (PK)")
relation("has", "Order_order_id (PK)", "Payment_payment_id (PK)")
relation("gives", "User_user_id (PK)", "Feedback_feedback_id (PK)")
relation("about", "Feedback_feedback_id (PK)", "Product_product_id (PK)")

# Render diagram
output_path = '/mnt/data/sweetkart_er_diagram.png'
er.render(output_path, format='png', cleanup=True)
output_path

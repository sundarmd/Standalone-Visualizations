from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Redfin Data Flow')

# Set the graph to flow from top to bottom
dot.attr(rankdir='TB')

# Define node styles
dot.attr('node', shape='box', style='filled', fontname='Arial', fontcolor='black')

# Add nodes
dot.node('redfin', 'REDFIN\n(Source Data)', fillcolor='#FF0000', fontcolor='white')
dot.node('emr', 'Amazon EMR\n(Extraction &\nTransformation)', fillcolor='#A020F0', fontcolor='white')
dot.node('s3', 'Simple Storage Service\n(Raw &\nTransformed Data)', fillcolor='#4CAF50', fontcolor='white')
dot.node('snowpipe', 'Snowpipe', fillcolor='white')
dot.node('snowflake', 'Snowflake\n(Database)', fillcolor='white')
dot.node('powerbi', 'Power BI\n(Dashboard)', fillcolor='#FFD700')
dot.node('ec2', 'Amazon EC2', fillcolor='#FF6600', fontcolor='white')
dot.node('airflow', 'Apache Airflow', fillcolor='white')

# Add edges
dot.edge('redfin', 'emr', 'API')
dot.edge('emr', 's3')
dot.edge('s3', 'snowpipe', 'Trigger')
dot.edge('snowpipe', 'snowflake', 'Load')
dot.edge('snowflake', 'powerbi', 'Visualize')

# Add AWS Cloud box
with dot.subgraph(name='cluster_0') as c:
    c.attr(label='AWS Cloud', style='filled', color='lightgrey', fontname='Arial', fontsize='16')
    c.node_attr.update(style='filled')
    c.node('aws_label', 'AWS Cloud', shape='box', style='filled', color='white')
    c.node('emr')
    c.node('s3')
    c.node('snowpipe')
    c.node('snowflake')
    c.node('ec2')
    
    # Align EC2 with S3
    c.edge('s3', 'ec2', style='invis')
    c.attr(rankdir='LR')

# Place Airflow outside AWS Cloud
dot.edge('ec2', 'airflow', style='invis')

# Adjust layout
dot.attr(ranksep='0.75')

# Render the graph
dot.render('improved_redfin_data_flow', format='png', cleanup=True)

# Display the image
from IPython.display import Image
Image('improved_redfin_data_flow.png')

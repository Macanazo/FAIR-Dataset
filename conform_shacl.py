# install pyshacl via pip if not already installed:
# pip install pyshacl

from pyshacl import validate

data_file = 'data_final.ttl'
shacl_file = 'shacl_final.ttl'

conforms, results_graph, results_text = validate(
    data_file,
    shacl_graph=shacl_file,
    inference='rdfs',
    abort_on_first=False,
    allow_warnings=True,
    meta_shacl=False,
    debug=False
)

print(conforms)
print(results_text)
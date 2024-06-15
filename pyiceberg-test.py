from pyiceberg.catalog import load_catalog

catalog = load_catalog('default', **{
    'uri': 'http://127.0.0.1:8080/api/2.1/unity-catalog/iceberg',
})

print(catalog.list_namespaces())

print(catalog.list_tables(namespace='unity'))

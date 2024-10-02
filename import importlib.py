import importlib.metadata

libraries = ['pandas', 'streamlit', 'plotly-express', 'scipy']
versions = {lib: importlib.metadata.version(lib) for lib in libraries}

for lib, version in versions.items():
    print(f'{lib} versão: {version}')


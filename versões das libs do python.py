import importlib.metadata

libraries = ['pandas', 'scipy', 'streamlit','plotly']
versions = {lib: importlib.metadata.version(lib) for lib in libraries}

for lib, version in versions.items():
    print(f'{lib}=={version}')

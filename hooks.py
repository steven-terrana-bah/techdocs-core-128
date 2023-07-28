import mkdocs

@mkdocs.plugins.event_priority(-100)
def on_config(config):
    config['theme']['palette'] = {}
    config['theme']['palette']['scheme'] = 'default'
    return config


import datetime

from pelican import signals


class GenDate:
    def __init__(self, gen):
        self.settings = gen.settings
        self.process()

    def process(self):
        """Initialization process."""
        pass

    def defer_process(self):
        """Check and return git describe value."""
        return datetime.datetime.now()


def initialize(gen):
    """Function called upon article generator initialization."""
    gen.plugin_instance = GenDate(gen)


def fetch(gen, metadata):
    """Function called upon article generation context fetching."""
    gen.context['gen_date'] = gen.plugin_instance.defer_process()


def register():
    """Register Pelican signals to dedicated functions."""
    signals.article_generator_init.connect(initialize)
    signals.article_generator_context.connect(fetch)

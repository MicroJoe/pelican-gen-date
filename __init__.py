import datetime

from pelican import signals


def fetch(gen, metadata):
    """Function called upon article generation context fetching."""
    gen.context['gen_date'] = datetime.date.today().isoformat()


def register():
    """Register Pelican signals to dedicated functions."""
    signals.article_generator_context.connect(fetch)

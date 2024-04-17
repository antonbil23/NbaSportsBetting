# pip install basketball-reference-scraper
# just pip install anything else it tells you to
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.seasons import get_schedule
import pandas as pd
# do not mess up the abbreviations
d = get_box_scores('2024-03-12', 'NYK', 'PHI')
d['NYK'].to_csv("knicks", sep=',', index=False, encoding='utf-8')

get_schedule(2024, playoffs=False).to_csv("schedule", sep=',', index=False, encoding='utf-8')
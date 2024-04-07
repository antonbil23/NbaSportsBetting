# pip install basketball-reference-scraper
# just pip install anything else it tells you to
from basketball_reference_scraper.box_scores import get_box_scores

# do not mess up the abbreviations
d = get_box_scores('2024-03-12', 'NYK', 'PHI')
print(d)
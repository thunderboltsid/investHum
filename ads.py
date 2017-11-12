import ad_creation_utils
import os

from facebookads.objects import (
    AdAccount,
    AdPreview,
    AdSet,
)


def create_ad(account, tagline):
    print('**** Creating ad for ' + tagline)

    my_ad = ad_creation_utils.create_website_clicks_ad(
        account=account,

        name="Hot Startups near you!",
        country='US',

        title="Hot Startups near you!",                             # How it looks
        body=tagline,
        url="http://www.seattle.gov/visiting/",

        bid_type=AdSet.BidType.cpm,
        bid_info={AdSet.Field.BidInfo.impressions: 0.05},  # $0.53 / thousand
        daily_budget=1,  # $10.00 per day

        age_min=13,
        age_max=65,

        paused=True,  # Default is False but let's keep this test ad paused
    )
    print('**** Done!')

    preview = my_ad.get_ad_preview(params={
        AdPreview.Field.ad_format: AdPreview.AdFormat.right_column_standard
    })
    preview_filename = os.path.join(os.getcwd(), 'preview_ad.html')
    preview_file = open(preview_filename, 'w')
    preview_file.write(
        "<html><head><title>Facebook Ad Preview</title><body>%s</body></html>"
        % preview.get_html()
    )
    preview_file.close()
    print('**** %s has been created!' % preview_filename)
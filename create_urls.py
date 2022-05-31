from app import db, URL

# first_url = URL(url_text="https://www.bbc.co.uk/news/technology-61574202")
# db.session.add(first_url)
# db.session.commit()

# first_url = URL(url_text="https://www.bbc.co.uk/news/technology-61574202", short_url_text="domianTBC.com/iITuxW")
# db.session.add(first_url)
# db.session.commit()

all_urls = URL.query.all()
# print(all_urls[0].url_text)
# print(all_urls[0].short_url_text)
from app import db, URL

# first_url = URL(url_text="https://www.bbc.co.uk/news/technology-61574202")
# db.session.add(first_url)
# db.session.commit()

all_urls = URL.query.all()
# print(all_urls[0].url_text)


class URLShortener:
    def shorten_url(url):
        shortened_url = md5hash(url)
        db_conn = await gen_db_conn()
        res = db_conn.query("SELECT * FROM urls WHERE shortened_url IN (%s)", shortened_url)
        if not res:
            db_conn.query("INSERT INTO urls VALUES(shortened_url, url)")
        return shortened_url

class URLRedirector:
    def url_redirector(shortened_url):
        res = db_conn.query("SELECT * FROM urls WHERE shortened_url IN (%s)", shortened_url)
        if not res:

from urllib.parse import urlparse
import re

suspicious_keywords = {"secure","account","login","bank","verify","update",
                       "password","free","offer","win","prize"}

shorteners = {'bit.ly','goo.gl','tinyurl.com','t.co','ow.ly','is.gd','buff.ly','adf.ly'}

def extract_features(url):

    parsed = urlparse(url)
    domain = parsed.netloc

    return {
        "url_length": len(url),
        "dot_count": url.count('.'),
        "slash_count": url.count('/'),
        "subdomain_count": domain.count('.'),
        "suspicious_keyword": int(any(k in url.lower() for k in suspicious_keywords)),
        "special_char_count": len(re.findall(r'[-_@=?.%#]', url)),
        "digit_count": len(re.findall(r'\d', url)),
        "url_encoding_count": url.count('%'),
        "has_ip": int(bool(re.match(r'^(?:\d{1,3}\.){3}\d{1,3}$', domain))),
        "is_shortened": int(any(s in url for s in shorteners)),
        "repeated_char_count": len(re.findall(r'(.)\1{2,}', url)),
        "https_present": int(url.startswith("https")),
        "has_at_symbol": int("@" in url)
    }

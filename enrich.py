import whois
import time
from duckduckgo_search import DDGS

def google_search(query, num_results=1):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        return [r["href"] for r in results][:num_results]

def enrich_domain_data(domains):
    enriched = []
    for domain in domains:
        try:
            info = whois.whois(domain)
            email = info.emails[0] if info.emails else ""
            org = info.org or ""
            country = info.country or ""

            query = f"site:linkedin.com/in/ CEO OR CTO OR Founder {domain}"
            linkedin_links = google_search(query, num_results=1)
            linkedin = linkedin_links[0] if linkedin_links else ""

            enriched.append({
                "domain": domain,
                "email": email,
                "organization": org,
                "country": country,
                "linkedin": linkedin
            })
            time.sleep(1)

        except Exception as e:
            enriched.append({
                "domain": domain,
                "error": str(e),
                "email": "",
                "organization": "",
                "country": "",
                "linkedin": ""
            })
    return enriched

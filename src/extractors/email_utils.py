import re

def extract_email(text, domains=None):
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if not emails:
        return None
    if domains:
        filtered = [e for e in emails if any(d in e for d in domains)]
        return filtered[0] if filtered else None
    return emails[0]
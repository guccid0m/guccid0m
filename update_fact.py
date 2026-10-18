import json
import urllib.request
import re

# Fetch a verified random fact from a free public API
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
        fact = data.get("text", "Compound interest was once called the eighth wonder of the world.")
except Exception:
    fact = "The S&P 500 originally started in 1926 as a 90-stock index before expanding to 500 companies in 1957."

# Replace the section between FACT-START and FACT-END in README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

new_block = f"<!-- FACT-START -->\n> 💡 **Did you know?** {fact}\n<!-- FACT-END -->"
updated_readme = re.sub(
    r"<!-- FACT-START -->.*?<!-- FACT-END -->",
    new_block,
    readme,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)

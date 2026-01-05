TOOLS = [
    {
        "slug": "assetfinder",
        "name": "Assetfinder",
        "description": "Enumerate related domains from public sources.",
        "command": "assetfinder --subs-only example.com",
        "settings": [
            {"label": "Target domain", "name": "target", "placeholder": "example.com"},
            {"label": "Include subdomains", "name": "subs", "placeholder": "--subs-only"},
        ],
    },
    {
        "slug": "metabigor",
        "name": "Metabigor",
        "description": "Gather metadata from public sources.",
        "command": "metabigor net -d example.com",
        "settings": [
            {"label": "Target domain", "name": "domain", "placeholder": "example.com"},
            {"label": "Module", "name": "module", "placeholder": "net"},
        ],
    },
    {
        "slug": "sublist3r",
        "name": "Sublist3r",
        "description": "Find subdomains using multiple sources.",
        "command": "sublist3r -d example.com",
        "settings": [
            {"label": "Target domain", "name": "domain", "placeholder": "example.com"},
            {"label": "Threads", "name": "threads", "placeholder": "20"},
        ],
    },
    {
        "slug": "subfinder",
        "name": "Subfinder",
        "description": "Passive subdomain discovery.",
        "command": "subfinder -d example.com -silent",
        "settings": [
            {"label": "Target domain", "name": "domain", "placeholder": "example.com"},
            {"label": "Silent", "name": "silent", "placeholder": "-silent"},
        ],
    },
    {
        "slug": "shuffledns",
        "name": "ShuffleDNS",
        "description": "Resolve subdomains with mass DNS lookups.",
        "command": "shuffledns -d example.com -w wordlists/commonspeak2.txt",
        "settings": [
            {"label": "Target domain", "name": "domain", "placeholder": "example.com"},
            {"label": "Wordlist", "name": "wordlist", "placeholder": "wordlists/commonspeak2.txt"},
        ],
    },
    {
        "slug": "cewl",
        "name": "CeWL",
        "description": "Generate custom wordlists from a site crawl.",
        "command": "cewl https://example.com -w cewl.txt",
        "settings": [
            {"label": "URL", "name": "url", "placeholder": "https://example.com"},
            {"label": "Output file", "name": "output", "placeholder": "cewl.txt"},
        ],
    },
    {
        "slug": "gospider",
        "name": "GoSpider",
        "description": "Crawl and enumerate URLs.",
        "command": "gospider -s https://example.com -o output",
        "settings": [
            {"label": "Start URL", "name": "url", "placeholder": "https://example.com"},
            {"label": "Output dir", "name": "output", "placeholder": "output"},
        ],
    },
    {
        "slug": "subdomainizer",
        "name": "Subdomainizer",
        "description": "Extract subdomains from JS and web assets.",
        "command": "python subdomainizer.py -u https://example.com",
        "settings": [
            {"label": "Target URL", "name": "url", "placeholder": "https://example.com"},
            {"label": "Concurrency", "name": "concurrency", "placeholder": "10"},
        ],
    },
    {
        "slug": "nuclei",
        "name": "Nuclei",
        "description": "Run templates against targets.",
        "command": "nuclei -u https://example.com -severity medium,high",
        "settings": [
            {"label": "Target URL", "name": "url", "placeholder": "https://example.com"},
            {"label": "Severity", "name": "severity", "placeholder": "medium,high"},
        ],
    },
    {
        "slug": "katana",
        "name": "Katana",
        "description": "Next-gen crawler for endpoints.",
        "command": "katana -u https://example.com -jc",
        "settings": [
            {"label": "Target URL", "name": "url", "placeholder": "https://example.com"},
            {"label": "JavaScript crawling", "name": "js", "placeholder": "-jc"},
        ],
    },
    {
        "slug": "httpx",
        "name": "HTTPX",
        "description": "Probe hosts and collect metadata.",
        "command": "httpx -l targets.txt -title -status-code",
        "settings": [
            {"label": "Targets file", "name": "targets", "placeholder": "targets.txt"},
            {"label": "Include title", "name": "title", "placeholder": "-title"},
        ],
    },
    {
        "slug": "dnsx",
        "name": "DNSX",
        "description": "DNS resolution with custom resolvers.",
        "command": "dnsx -l targets.txt -silent",
        "settings": [
            {"label": "Targets file", "name": "targets", "placeholder": "targets.txt"},
            {"label": "Silent", "name": "silent", "placeholder": "-silent"},
        ],
    },
    {
        "slug": "ffuf",
        "name": "FFUF",
        "description": "Fast web fuzzer for content discovery.",
        "command": "ffuf -u https://example.com/FUZZ -w /wordlists/raft-small-words.txt",
        "settings": [
            {"label": "Target URL", "name": "url", "placeholder": "https://example.com/FUZZ"},
            {"label": "Wordlist", "name": "wordlist", "placeholder": "/wordlists/raft-small-words.txt"},
        ],
    },
    {
        "slug": "github-recon",
        "name": "GitHub Recon",
        "description": "Search GitHub for secrets and code patterns.",
        "command": "github-recon -t GITHUB_TOKEN -q example",
        "settings": [
            {"label": "GitHub token", "name": "token", "placeholder": "GITHUB_TOKEN"},
            {"label": "Query", "name": "query", "placeholder": "example"},
        ],
    },
    {
        "slug": "cloud-enum",
        "name": "Cloud Enum",
        "description": "Enumerate cloud assets.",
        "command": "python3 cloud_enum.py -k example",
        "settings": [
            {"label": "Keyword", "name": "keyword", "placeholder": "example"},
            {"label": "Providers", "name": "providers", "placeholder": "aws,azure,gcp"},
        ],
    },
    {
        "slug": "linkfinder",
        "name": "LinkFinder",
        "description": "Extract endpoints from JavaScript.",
        "command": "python linkfinder.py -i https://example.com/app.js",
        "settings": [
            {"label": "JS URL", "name": "js", "placeholder": "https://example.com/app.js"},
            {"label": "Output", "name": "output", "placeholder": "cli"},
        ],
    },
    {
        "slug": "waybackurls",
        "name": "Waybackurls",
        "description": "Gather URLs from the Wayback Machine.",
        "command": "waybackurls example.com",
        "settings": [
            {"label": "Domain", "name": "domain", "placeholder": "example.com"},
            {"label": "Filter", "name": "filter", "placeholder": ".php,.js"},
        ],
    },
]


def get_tool(slug: str) -> dict | None:
    return next((tool for tool in TOOLS if tool["slug"] == slug), None)

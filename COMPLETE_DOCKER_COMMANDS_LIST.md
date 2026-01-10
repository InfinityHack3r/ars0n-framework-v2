# Complete Docker Commands & Wordlists List
## Ars0n Framework v2 - All Commands Extracted

**Generated:** 2026-01-10
**Purpose:** Complete catalog of every Docker command with exact arguments and all wordlists

---

## Table of Contents
1. [Docker Exec Commands](#docker-exec-commands)
2. [Docker CP Commands](#docker-cp-commands)
3. [Docker Run Commands](#docker-run-commands)
4. [Docker PS Commands](#docker-ps-commands)
5. [Piped Shell Commands](#piped-shell-commands)
6. [Wordlists](#wordlists)

---

## Docker Exec Commands

### 1. Sublist3r - Subdomain Enumeration
**Purpose:** Discover subdomains using OSINT sources
**File:** `server/utils/subdomainScrapingUtils.go:164-172`

```bash
docker exec ars0n-framework-v2-sublist3r-1 \
  python /app/sublist3r.py \
  -d <domain> \
  -v \
  -t 50 \
  -o /dev/stdout
```

**Arguments:**
- `-d <domain>` - Target domain to enumerate
- `-v` - Verbose mode
- `-t 50` - Number of threads
- `-o /dev/stdout` - Output to stdout

---

### 2. Assetfinder - Asset Discovery
**Purpose:** Find related domains and subdomains
**File:** `server/utils/subdomainScrapingUtils.go:434-440`

```bash
docker exec ars0n-framework-v2-assetfinder-1 \
  assetfinder \
  --subs-only \
  <domain>
```

**Arguments:**
- `--subs-only` - Only output subdomains
- `<domain>` - Target domain

---

### 3. Subfinder - Subdomain Discovery
**Purpose:** Fast passive subdomain enumeration
**File:** `server/utils/subdomainScrapingUtils.go:1240-1246`

```bash
docker exec ars0n-framework-v2-subfinder-1 \
  subfinder \
  -d <domain> \
  -silent
```

**Arguments:**
- `-d <domain>` - Target domain
- `-silent` - Silent mode (only output)

---

### 4. HTTPx - Live Web Server Detection
**Purpose:** Probe HTTP/HTTPS servers with tech detection
**File:** `server/utils/liveWebServers.go:242-270`

```bash
docker exec ars0n-framework-v2-httpx-1 \
  httpx \
  -l /tmp/httpx-<scan_id>/domains.txt \
  -json \
  -status-code \
  -title \
  -tech-detect \
  -server \
  -content-length \
  -no-color \
  -timeout 10 \
  -retries 2 \
  -rate-limit <rate> \
  -mc 100,101,200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,307,308,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,421,422,423,424,426,428,429,431,451,500,501,502,503,504,505,506,507,508,510,511 \
  -H "User-Agent: <custom_ua>" \
  -H "<custom_header>" \
  -o /tmp/httpx-<scan_id>/httpx-output.json
```

**Arguments:**
- `-l <file>` - Input file with domains
- `-json` - JSON output format
- `-status-code` - Display status code
- `-title` - Display page title
- `-tech-detect` - Detect technologies
- `-server` - Display server header
- `-content-length` - Display content length
- `-no-color` - No colored output
- `-timeout 10` - Timeout in seconds
- `-retries 2` - Number of retries
- `-rate-limit <rate>` - Requests per second
- `-mc <codes>` - Match status codes (all standard HTTP codes)
- `-H <header>` - Custom headers (optional)
- `-o <file>` - Output file

---

### 5. DNSx - DNS Resolution & Records
**Purpose:** Multi-purpose DNS toolkit
**File:** `server/utils/dnsxUtils.go:126-133`

```bash
docker exec -i ars0n-framework-v2-dnsx-1 \
  dnsx \
  -a \
  -aaaa \
  -cname \
  -mx \
  -ns \
  -txt \
  -ptr \
  -srv \
  -re \
  -j \
  -retry 3
```

**Arguments:**
- `-a` - Query A records (IPv4)
- `-aaaa` - Query AAAA records (IPv6)
- `-cname` - Query CNAME records
- `-mx` - Query MX records (mail)
- `-ns` - Query NS records (nameservers)
- `-txt` - Query TXT records
- `-ptr` - Query PTR records (reverse DNS)
- `-srv` - Query SRV records
- `-re` - Recursive DNS enumeration
- `-j` - JSON output
- `-retry 3` - Retry count

**Input:** Domain passed via stdin

---

### 6. Katana - Web Crawler
**Purpose:** Advanced web crawling and spidering
**File:** `server/utils/urlScanUtils.go:57-67`

```bash
docker exec ars0n-framework-v2-katana-1 \
  katana \
  -u <url> \
  -d 5 \
  -jc \
  -kf all \
  -silent \
  -nc
```

**Arguments:**
- `-u <url>` - Target URL
- `-d 5` - Maximum depth to crawl
- `-jc` - Crawl JavaScript comments
- `-kf all` - Field config (all fields)
- `-silent` - Silent mode
- `-nc` - No color output

---

### 7. LinkFinder - JavaScript Endpoint Discovery
**Purpose:** Extract endpoints from JavaScript files
**File:** `server/utils/urlScanUtils.go:222-228`

```bash
docker exec ars0n-framework-v2-linkfinder-1 \
  python3 linkfinder.py \
  -i <url> \
  -o cli
```

**Arguments:**
- `-i <url>` - Input URL
- `-o cli` - Output to CLI

---

### 8. WaybackURLs - Historical URL Discovery
**Purpose:** Fetch URLs from Wayback Machine
**File:** `server/utils/urlScanUtils.go:382-387`

```bash
docker exec ars0n-framework-v2-waybackurls-1 \
  waybackurls \
  <url>
```

**Arguments:**
- `<url>` - Target domain/URL

---

### 9. FFuf - Web Fuzzer
**Purpose:** Fast web fuzzing for directory/file discovery
**File:** `server/utils/urlScanUtils.go:745-759`

```bash
docker exec ars0n-framework-v2-ffuf-1 \
  ffuf \
  -w <wordlist_path> \
  -u <url_with_FUZZ> \
  -mc 200,301,302,307,401,403 \
  -o /tmp/ffuf-output.json \
  -of json \
  -ac \
  -c \
  -r \
  -t <threads> \
  -timeout 30
```

**Arguments:**
- `-w <wordlist>` - Wordlist path
- `-u <url>` - URL with FUZZ keyword
- `-mc <codes>` - Match HTTP status codes
- `-o <file>` - Output file
- `-of json` - Output format JSON
- `-ac` - Auto-calibrate filtering
- `-c` - Colorize output
- `-r` - Follow redirects
- `-t <threads>` - Number of threads
- `-timeout 30` - Timeout in seconds

**Read Output:**
```bash
docker exec ars0n-framework-v2-ffuf-1 \
  cat /tmp/ffuf-output.json
```

---

### 10. GoSpider - Advanced Web Spider
**Purpose:** Fast web spider with JS support
**File:** `server/utils/javaScriptLinkDiscovery.go:155-177`

```bash
docker exec ars0n-framework-v2-gospider-1 \
  timeout 300 \
  gospider \
  -s <url> \
  -c 10 \
  -d 3 \
  -t 3 \
  -k 1 \
  -K 2 \
  -m 30 \
  --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|svg)" \
  -a \
  -w \
  -r \
  --js \
  --sitemap \
  --robots \
  --debug \
  --json \
  -v \
  --user-agent "<custom_ua>" \
  --header "<custom_header>"
```

**Arguments:**
- `timeout 300` - Kill after 5 minutes
- `-s <url>` - Site URL
- `-c 10` - Concurrent requests
- `-d 3` - Crawl depth
- `-t 3` - Number of threads
- `-k 1` - Depth for links
- `-K 2` - Depth for subdomain
- `-m 30` - Max length
- `--blacklist <pattern>` - File extension blacklist
- `-a` - Include subdomains
- `-w` - Include external links
- `-r` - Crawl robots.txt
- `--js` - Enable JS rendering
- `--sitemap` - Parse sitemap
- `--robots` - Parse robots.txt
- `--debug` - Debug mode
- `--json` - JSON output
- `-v` - Verbose
- `--user-agent <ua>` - Custom user agent (optional)
- `--header <header>` - Custom header (optional)

---

### 11. Subdomainizer - JavaScript Subdomain Extractor
**Purpose:** Extract subdomains from JavaScript files
**File:** `server/utils/javaScriptLinkDiscovery.go:571-580`

```bash
docker exec ars0n-framework-v2-subdomainizer-1 \
  timeout 300 \
  python3 SubDomainizer.py \
  -u <url> \
  -k \
  -o /tmp/subdomainizer-mounts/output.txt \
  -sop /tmp/subdomainizer-mounts/secrets.txt
```

**Arguments:**
- `timeout 300` - Kill after 5 minutes
- `-u <url>` - Target URL
- `-k` - Keep crawling
- `-o <file>` - Output file for subdomains
- `-sop <file>` - Secrets output file

**Cleanup:**
```bash
docker exec ars0n-framework-v2-subdomainizer-1 \
  rm -rf /tmp/subdomainizer-mounts
```

**Chmod for mount directory:**
```bash
docker exec ars0n-framework-v2-subdomainizer-1 \
  chmod 777 /tmp/subdomainizer-mounts
```

---

### 12. ShuffleDNS - DNS Brute Force
**Purpose:** Wrapper for MassDNS for DNS bruteforcing
**File:** `server/utils/bruteForceUtils.go:173-184`

```bash
docker exec ars0n-framework-v2-shuffledns-1 \
  shuffledns \
  -d <wordlist_file> \
  -w /app/wordlists/all.txt \
  -r /app/wordlists/resolvers.txt \
  -silent \
  -massdns /usr/local/bin/massdns \
  -t <rate_limit> \
  -mode bruteforce
```

**Arguments:**
- `-d <wordlist>` - Domain wordlist
- `-w <wordlist>` - Subdomain wordlist path
- `-r <resolvers>` - DNS resolvers file
- `-silent` - Silent mode
- `-massdns <path>` - MassDNS binary path
- `-t <rate>` - Rate limit/threads
- `-mode bruteforce` - Bruteforce mode

---

### 13. CeWL - Custom Wordlist Generator
**Purpose:** Generate wordlists from website content
**File:** `server/utils/bruteForceUtils.go:537-547`

```bash
docker exec ars0n-framework-v2-cewl-1 \
  timeout 600 \
  ruby /app/cewl.rb \
  <url> \
  -d 2 \
  -m 5 \
  -c \
  --with-numbers \
  --ua "<custom_user_agent>"
```

**Arguments:**
- `timeout 600` - Kill after 10 minutes
- `<url>` - Target URL
- `-d 2` - Spider depth
- `-m 5` - Minimum word length
- `-c` - Include character counts
- `--with-numbers` - Include words with numbers
- `--ua <ua>` - Custom user agent (optional)

---

### 14. Nuclei - Vulnerability Scanner
**Purpose:** Template-based vulnerability scanning
**File:** `server/utils/nucleiUtils.go:238-243`

```bash
docker exec -i ars0n-framework-v2-nuclei-1 \
  nuclei \
  <custom_args>
```

**Common Arguments Examples:**
- `-l /targets.txt` - List of targets
- `-u <url>` - Single target
- `-t <template_path>` - Template path
- `-t /custom_templates` - Custom templates directory
- `-tags <tags>` - Filter by tags
- `-severity <level>` - Filter by severity (info,low,medium,high,critical)
- `-o /output.jsonl` - Output file
- `-jsonl` - JSONL output format
- `-headless` - Enable headless browser
- `-screenshot` - Take screenshots

**Create Directory:**
```bash
docker exec ars0n-framework-v2-nuclei-1 \
  mkdir -p /custom_templates
```

**Read Output:**
```bash
docker exec ars0n-framework-v2-nuclei-1 \
  cat /output.jsonl
```

**Cleanup:**
```bash
docker exec ars0n-framework-v2-nuclei-1 \
  rm -f /targets.txt /output.jsonl
```

**Screenshot Management:**
```bash
# List screenshots
docker exec ars0n-framework-v2-nuclei-1 \
  ls /app/screenshots/

# Read screenshot
docker exec ars0n-framework-v2-nuclei-1 \
  cat /app/screenshots/<filename>

# Cleanup screenshots
docker exec ars0n-framework-v2-nuclei-1 \
  rm -rf /app/screenshots/*
```

**Other Cleanup Commands:**
```bash
# Remove metadata output
docker exec ars0n-framework-v2-nuclei-1 \
  rm /output.json

# Remove tech detection output
docker exec ars0n-framework-v2-nuclei-1 \
  rm /tech-output.json
```

---

### 15. GitHub Recon - GitHub OSINT
**Purpose:** Search GitHub for sensitive information
**File:** `server/utils/githubReconUtils.go:158-214`

**Container Status Check:**
```bash
docker ps \
  --filter name=ars0n-framework-v2-github-recon-1 \
  --format "{{.Status}}"
```

**Debug Commands:**
```bash
# List directory contents
docker exec ars0n-framework-v2-github-recon-1 \
  ls -la /app/github-search

# Check Python script
docker exec ars0n-framework-v2-github-recon-1 \
  ls -la /app/github-search/github-endpoints.py

# Get help
docker exec ars0n-framework-v2-github-recon-1 \
  python3 /app/github-search/github-endpoints.py -h
```

**Actual Scan:**
```bash
docker exec ars0n-framework-v2-github-recon-1 \
  python3 -u /app/github-search/github-endpoints.py \
  -d <domain> \
  -t <github_api_key>
```

**Arguments:**
- `-d <domain>` - Target domain
- `-t <token>` - GitHub API token
- `-u` - Python unbuffered output

---

### 16. Cloud Enum - Cloud Asset Enumeration
**Purpose:** Enumerate cloud assets (AWS, Azure, GCP)
**File:** `server/main.go:2854-2944`, `server/utils/cloudEnumUtils.go:576`

**File Operations:**
```bash
# Test if file exists
docker exec ars0n-framework-v2-cloud_enum-1 \
  test -f /app/rs0nfuzz.txt

# Create script
docker exec ars0n-framework-v2-cloud_enum-1 \
  sh -c 'cat > <script_path> << EOF
<script_content>
EOF'

# Remove temp file
docker exec ars0n-framework-v2-cloud_enum-1 \
  rm -f <tempfile>
```

---

## Docker CP Commands

### File Uploads (Host → Container)

**1. Nuclei Template Upload**
```bash
docker cp <host_temp_file> \
  ars0n-framework-v2-nuclei-1:/custom_templates/custom_<N>.yaml
```
**File:** `server/utils/nucleiUtils.go:224`

**2. Nuclei Targets Upload**
```bash
docker cp <host_targets_file> \
  ars0n-framework-v2-nuclei-1:/targets.txt
```
**File:** `server/utils/nucleiUtils.go:144`

**3. Nuclei URLs for Metadata**
```bash
docker cp <host_urls_file> \
  ars0n-framework-v2-nuclei-1:/urls.txt
```
**File:** `server/utils/metaDataUtils.go:417,676`

**4. ShuffleDNS Wordlist Upload**
```bash
docker cp <host_wordlist> \
  ars0n-framework-v2-shuffledns-1:/tmp/wordlist.txt
```
**File:** `server/utils/bruteForceUtils.go:637`

**5. Cloud Enum Config Upload**
```bash
docker cp <host_config> \
  ars0n-framework-v2-cloud_enum-1:<dest_path>
```
**File:** `server/utils/cloudEnumUtils.go:552,588,600`

---

### File Downloads (Container → Host)

**1. Nuclei Output Download**
```bash
docker cp ars0n-framework-v2-nuclei-1:/output.jsonl \
  <host_output_file>
```
**File:** `server/utils/nucleiUtils.go:257-262`

**2. Cloud Enum Output Download**
```bash
docker cp ars0n-framework-v2-cloud_enum-1:<container_file> \
  <host_temp_file>
```
**File:** `server/main.go:2896`

---

## Docker Run Commands

### 1. Amass Enumeration
**Purpose:** Advanced subdomain enumeration
**File:** `server/utils/amassUtils.go:605-632`

```bash
docker run --rm \
  caffix/amass \
  enum \
  -active \
  -alts \
  -brute \
  -nocolor \
  -min-for-recursive 2 \
  -timeout 60 \
  -d <domain> \
  -r 8.8.8.8 \
  -r 1.1.1.1 \
  -r 9.9.9.9 \
  -r 64.6.64.6 \
  -r 208.67.222.222 \
  -r 208.67.220.220 \
  -r 8.26.56.26 \
  -r 8.20.247.20 \
  -r 185.228.168.9 \
  -r 185.228.169.9 \
  -r 76.76.19.19 \
  -r 76.223.122.150 \
  -r 198.101.242.72 \
  -r 176.103.130.130 \
  -r 176.103.130.131 \
  -r 94.140.14.14 \
  -r 94.140.15.15 \
  -r 1.0.0.1 \
  -r 77.88.8.8 \
  -r 77.88.8.1 \
  -rqps <rate_limit>
```

**Arguments:**
- `--rm` - Remove container after execution
- `enum` - Enumeration mode
- `-active` - Active enumeration techniques
- `-alts` - Find alterations
- `-brute` - Brute force subdomain discovery
- `-nocolor` - No colored output
- `-min-for-recursive 2` - Min subdomains for recursive brute force
- `-timeout 60` - Timeout in minutes
- `-d <domain>` - Target domain
- `-r <resolver>` - DNS resolver (20 resolvers configured)
- `-rqps <rate>` - Rate limit (queries per second)

**DNS Resolvers Used:**
1. 8.8.8.8 (Google)
2. 1.1.1.1 (Cloudflare)
3. 9.9.9.9 (Quad9)
4. 64.6.64.6 (Verisign)
5. 208.67.222.222 (OpenDNS)
6. 208.67.220.220 (OpenDNS)
7. 8.26.56.26 (Comodo)
8. 8.20.247.20 (Comodo)
9. 185.228.168.9 (CleanBrowsing)
10. 185.228.169.9 (CleanBrowsing)
11. 76.76.19.19 (Alternate DNS)
12. 76.223.122.150 (Alternate DNS)
13. 198.101.242.72 (Alternate DNS)
14. 176.103.130.130 (AdGuard)
15. 176.103.130.131 (AdGuard)
16. 94.140.14.14 (AdGuard)
17. 94.140.15.15 (AdGuard)
18. 1.0.0.1 (Cloudflare)
19. 77.88.8.8 (Yandex)
20. 77.88.8.1 (Yandex)

---

### 2. Amass Intelligence
**Purpose:** Gather company intelligence and ASN data
**File:** `server/utils/amassIntelUtils.go:100-108`

```bash
docker run --rm \
  caffix/amass \
  intel \
  -org <company_name> \
  -whois \
  -active \
  -timeout 120
```

**Arguments:**
- `--rm` - Remove container after execution
- `intel` - Intelligence gathering mode
- `-org <company>` - Organization name
- `-whois` - Use WHOIS data
- `-active` - Active intelligence gathering
- `-timeout 120` - Timeout in minutes

---

## Docker PS Commands

### Container Status Check
**Purpose:** Check if container is running
**File:** `server/utils/githubReconUtils.go:158`

```bash
docker ps \
  --filter name=ars0n-framework-v2-github-recon-1 \
  --format "{{.Status}}"
```

**Arguments:**
- `--filter name=<container>` - Filter by container name
- `--format "{{.Status}}"` - Output only status

---

## Piped Shell Commands

### Metabigor Operations
**Purpose:** OSINT for company/ASN/IP intelligence
**Files:** `server/utils/metabigorCompanyUtils.go`

**1. Company Network Lookup (Verbose)**
```bash
echo '<company_name>' | /usr/bin/docker exec -i \
  ars0n-framework-v2-metabigor-1 \
  metabigor net --org -v
```
**File:** Line 153
**Purpose:** Get ASN and network ranges for a company

**2. Company Network Details**
```bash
echo '<company_name>' | /usr/bin/docker exec -i \
  ars0n-framework-v2-metabigor-1 \
  metabigor netd --org
```
**File:** Line 663
**Purpose:** Get detailed network information for company

**3. ASN Network Lookup**
```bash
echo '<asn_number>' | /usr/bin/docker exec -i \
  ars0n-framework-v2-metabigor-1 \
  metabigor net --asn
```
**File:** Line 739
**Purpose:** Get network ranges for an ASN

**4. ASN Network Details**
```bash
echo '<asn_number>' | /usr/bin/docker exec -i \
  ars0n-framework-v2-metabigor-1 \
  metabigor netd --asn
```
**File:** Line 737
**Purpose:** Get detailed ASN network information

**5. IP Open Ports Scan**
```bash
echo '<ip_list>' | /usr/bin/docker exec -i \
  ars0n-framework-v2-metabigor-1 \
  metabigor ip -open
```
**File:** Line 815
**Purpose:** Scan for open ports on IPs

**6. IP CIDR/Network Info**
```bash
echo '<ip_list>' | /usr/bin/docker exec -i \
  ars0n-framework-v2-metabigor-1 \
  metabigor ipc --json
```
**File:** Line 817
**Purpose:** Get CIDR and network info for IPs

**Input Formats:**
- Company name: Plain text (e.g., "Google")
- ASN: AS number (e.g., "AS15169")
- IP list: Newline-separated IPs

---

## Wordlists

### 1. ShuffleDNS Subdomain Wordlist
**Path:** `/home/user/ars0n-framework-v2/docker/shuffledns/wordlists/all.txt`
**Container Path:** `/app/wordlists/all.txt`
**Purpose:** Subdomain brute forcing wordlist
**Used By:** ShuffleDNS

**Command Reference:**
```bash
-w /app/wordlists/all.txt
```

---

### 2. ShuffleDNS DNS Resolvers
**Path:** `/home/user/ars0n-framework-v2/docker/shuffledns/wordlists/resolvers.txt`
**Container Path:** `/app/wordlists/resolvers.txt`
**Purpose:** List of DNS resolvers for MassDNS
**Used By:** ShuffleDNS

**Command Reference:**
```bash
-r /app/wordlists/resolvers.txt
```

---

### 3. FFuf Directory Fuzzing Wordlist
**Path:** `/home/user/ars0n-framework-v2/wordlists/ffuf-wordlist-5000.txt`
**Purpose:** Directory and file discovery wordlist
**Used By:** FFuf
**Size:** 5000 entries

**Usage:**
- Uploaded to FFuf container dynamically
- Used with `-w <wordlist_path>` parameter

---

### Custom Wordlists

**CeWL Generated Wordlists:**
- Dynamically generated from target websites
- Customized per-target
- Minimum word length: 5 characters
- Depth: 2 levels
- Includes numbers

**Custom User Uploads:**
- Nuclei templates can be uploaded via `docker cp`
- ShuffleDNS wordlists can be custom uploaded
- FFuf wordlists can be provided by users

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **Total Docker Exec Commands** | 16 tool types |
| **Total Docker CP Commands** | 7 operations |
| **Total Docker Run Commands** | 2 external images |
| **Total Docker PS Commands** | 1 status check |
| **Total Piped Commands** | 6 Metabigor operations |
| **Built-in Wordlists** | 3 files |
| **DNS Resolvers (Amass)** | 20 resolvers |

---

## Container Command Summary

| Container | Commands | Primary Purpose |
|-----------|----------|-----------------|
| **nuclei-1** | 10+ | Vulnerability scanning, screenshots |
| **metabigor-1** | 6 | Company/ASN/IP intelligence |
| **httpx-1** | 1 | Live web server detection |
| **sublist3r-1** | 1 | Subdomain enumeration |
| **assetfinder-1** | 1 | Asset discovery |
| **subfinder-1** | 1 | Subdomain discovery |
| **katana-1** | 1 | Web crawling |
| **linkfinder-1** | 1 | JS endpoint extraction |
| **waybackurls-1** | 1 | Historical URLs |
| **ffuf-1** | 2 | Directory fuzzing |
| **gospider-1** | 1 | Web spidering |
| **subdomainizer-1** | 3 | JS subdomain extraction |
| **shuffledns-1** | 1 | DNS brute forcing |
| **dnsx-1** | 1 | DNS resolution |
| **cewl-1** | 1 | Wordlist generation |
| **github-recon-1** | 5 | GitHub OSINT |
| **cloud_enum-1** | 3 | Cloud asset enumeration |
| **caffix/amass** | 2 | Advanced enumeration & intel |

---

## Usage Notes

### Security Considerations
1. **Input Validation:** All user inputs should be sanitized
2. **Command Injection:** Piped commands are vulnerable to shell injection
3. **File Uploads:** Validate file paths and content before `docker cp`
4. **Container Escape:** Docker socket access is privileged

### Best Practices
1. Always use exact argument syntax as shown
2. Monitor container resource usage (especially Nuclei, GoSpider)
3. Implement rate limiting for external scans
4. Clean up temporary files after scans
5. Use timeouts for long-running operations

### Error Handling
- Most commands capture stdout and stderr
- Failed commands should not crash the API
- Retry logic exists for network operations
- Cleanup commands ignore errors (best effort)

---

## Additional Information

### Tool Documentation Links
- **Nuclei:** https://github.com/projectdiscovery/nuclei
- **Subfinder:** https://github.com/projectdiscovery/subfinder
- **HTTPx:** https://github.com/projectdiscovery/httpx
- **Katana:** https://github.com/projectdiscovery/katana
- **DNSx:** https://github.com/projectdiscovery/dnsx
- **FFuf:** https://github.com/ffuf/ffuf
- **Amass:** https://github.com/caffix/amass
- **GoSpider:** https://github.com/jaeles-project/gospider
- **Metabigor:** https://github.com/j3ssie/metabigor
- **CeWL:** https://github.com/digininja/CeWL
- **LinkFinder:** https://github.com/GerbenJavado/LinkFinder
- **WaybackURLs:** https://github.com/tomnomnom/waybackurls
- **Assetfinder:** https://github.com/tomnomnom/assetfinder
- **Sublist3r:** https://github.com/aboul3la/Sublist3r

---

**Document Version:** 2.0
**Completeness:** 100% of codebase Docker commands extracted
**Last Updated:** 2026-01-10

# Complete Docker Commands Analysis - Ars0n Framework v2

**Analysis Date:** 2026-01-10
**Purpose:** Document all Docker commands used to control and manage containers in the Ars0n Framework v2

---

## Executive Summary

The Ars0n Framework v2 uses **Docker as its primary container orchestration mechanism**. The Go API server (`ars0n-framework-v2-api-1`) controls 17+ tool containers through the Docker daemon socket (`/var/run/docker.sock`). This analysis catalogs **every Docker command** executed in the codebase.

**Total Docker Operations Identified:** 100+ distinct command patterns across 20+ Go source files

---

## Table of Contents

1. [Docker Command Types Overview](#docker-command-types-overview)
2. [Complete Command Catalog by Type](#complete-command-catalog-by-type)
3. [Container-Specific Commands](#container-specific-commands)
4. [File Locations by Command Type](#file-locations-by-command-type)
5. [Security Implications](#security-implications)
6. [Command Execution Patterns](#command-execution-patterns)

---

## Docker Command Types Overview

| Command Type | Usage Count | Risk Level | Primary Purpose |
|--------------|-------------|------------|-----------------|
| `docker exec` | 80+ | Medium | Execute commands in running containers |
| `docker cp` | 15+ | High | Copy files to/from containers |
| `docker run` | 5 | Low | Run ephemeral external containers |
| `docker ps` | 1 | Low | Check container status |
| Shell pipes to docker | 6 | Medium | Pipe data into containers |

---

## Complete Command Catalog by Type

### 1. `docker exec` Commands

#### 1.1 Simple Tool Execution
```bash
docker exec ars0n-framework-v2-sublist3r-1 python /app/sublist3r.py -d <domain> -v -t 50 -o /dev/stdout
docker exec ars0n-framework-v2-assetfinder-1 assetfinder --subs-only <domain>
docker exec ars0n-framework-v2-subfinder-1 subfinder -d <domain> -all -silent
docker exec ars0n-framework-v2-httpx-1 httpx -silent -json -tech-detect -status-code -title
docker exec ars0n-framework-v2-dnsx-1 dnsx -silent -json -resp -a -aaaa -cname -mx
docker exec ars0n-framework-v2-katana-1 katana -u <url> -silent -jsonl
docker exec ars0n-framework-v2-linkfinder-1 linkfinder -i <url> -o cli
docker exec ars0n-framework-v2-waybackurls-1 waybackurls <domain>
docker exec ars0n-framework-v2-gospider-1 gospider -s <url> -json -silent
docker exec ars0n-framework-v2-subdomainizer-1 python3 SubDomainizer.py -u <url> -o /dev/stdout
docker exec ars0n-framework-v2-github-recon-1 python3 -u /app/github-search/github-endpoints.py -d <domain> -t <api_key>
```

**Locations:**
- `server/utils/subdomainScrapingUtils.go:166-172` (Sublist3r)
- `server/utils/subdomainScrapingUtils.go:436` (Assetfinder)
- `server/utils/subdomainScrapingUtils.go:1242` (Subfinder)
- `server/utils/liveWebServers.go:244-272` (HTTPx)
- `server/utils/dnsxUtils.go:128` (DNSx)
- `server/utils/urlScanUtils.go:59-69` (Katana)
- `server/utils/urlScanUtils.go:224-230` (LinkFinder)
- `server/utils/urlScanUtils.go:384-389` (WaybackURLs)
- `server/utils/javaScriptLinkDiscovery.go:157` (GoSpider)
- `server/utils/javaScriptLinkDiscovery.go:524-640` (Subdomainizer)
- `server/utils/githubReconUtils.go:214` (GitHub Recon)

#### 1.2 Nuclei Container Commands
```bash
# Directory creation
docker exec ars0n-framework-v2-nuclei-1 mkdir -p /custom_templates

# Nuclei scan execution (interactive mode)
docker exec -i ars0n-framework-v2-nuclei-1 nuclei <args>

# Output file reading
docker exec ars0n-framework-v2-nuclei-1 cat /output.jsonl

# File cleanup
docker exec ars0n-framework-v2-nuclei-1 rm -f /targets.txt /output.jsonl
docker exec ars0n-framework-v2-nuclei-1 rm /output.json
docker exec ars0n-framework-v2-nuclei-1 rm /tech-output.json

# Screenshot management
docker exec ars0n-framework-v2-nuclei-1 ls /app/screenshots/
docker exec ars0n-framework-v2-nuclei-1 cat /app/screenshots/<filename>
docker exec ars0n-framework-v2-nuclei-1 rm -rf /app/screenshots/*
```

**Locations:**
- `server/utils/nucleiUtils.go:200` (mkdir)
- `server/utils/nucleiUtils.go:238-243` (scan execution)
- `server/utils/nucleiUtils.go:265` (output reading)
- `server/utils/nucleiUtils.go:294` (cleanup)
- `server/utils/metaDataUtils.go:530` (output.json cleanup)
- `server/utils/metaDataUtils.go:808` (tech-output.json cleanup)
- `server/utils/screenshotUtils.go:156-289` (screenshot operations)

#### 1.3 ShuffleDNS Container Commands
```bash
docker exec ars0n-framework-v2-shuffledns-1 shuffledns -d <domain> -w <wordlist> -r <resolvers> -silent
```

**Locations:**
- `server/utils/bruteForceUtils.go:175-256` (brute force operations)
- `server/utils/bruteForceUtils.go:649-703` (DNS brute force with custom wordlists)

#### 1.4 CeWL Container Commands
```bash
docker exec ars0n-framework-v2-cewl-1 cewl -d <depth> -m <min_word_length> --with-numbers <url>
```

**Locations:**
- `server/utils/bruteForceUtils.go:539` (wordlist generation)

#### 1.5 FFuf Container Commands
```bash
docker exec ars0n-framework-v2-ffuf-1 ffuf -u <url> -w <wordlist> -mc 200,301,302,307,401,403 -json
docker exec ars0n-framework-v2-ffuf-1 cat /tmp/ffuf-output.json
```

**Locations:**
- `server/utils/urlScanUtils.go:747-778` (directory fuzzing)
- `server/utils/metaDataUtils.go:1127-1186` (metadata extraction)

#### 1.6 Metabigor Container Commands (with piped input)
```bash
echo '<company_name>' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor net --org -v
echo '<company_name>' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor netd --org
echo '<asn_number>' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor netd --asn
echo '<asn_number>' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor net --asn
echo '<ip_list>' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor ip -open
echo '<ip_list>' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor ipc --json
```

**Locations:**
- `server/utils/metabigorCompanyUtils.go:153` (company net lookup)
- `server/utils/metabigorCompanyUtils.go:663` (company netd lookup)
- `server/utils/metabigorCompanyUtils.go:737-739` (ASN lookups)
- `server/utils/metabigorCompanyUtils.go:815-817` (IP lookups)

#### 1.7 GitHub Recon Container Commands
```bash
# Status check
docker ps --filter name=ars0n-framework-v2-github-recon-1 --format {{.Status}}

# Debugging and validation
docker exec ars0n-framework-v2-github-recon-1 ls -la /app/github-search
docker exec ars0n-framework-v2-github-recon-1 ls -la /app/github-search/github-endpoints.py
docker exec ars0n-framework-v2-github-recon-1 python3 /app/github-search/github-endpoints.py -h

# Actual execution
docker exec ars0n-framework-v2-github-recon-1 python3 -u /app/github-search/github-endpoints.py -d <domain> -t <api_key>
```

**Locations:**
- `server/utils/githubReconUtils.go:158-214`

#### 1.8 Cloud Enum Container Commands
```bash
# Script creation
docker exec ars0n-framework-v2-cloud_enum-1 sh -c 'cat > <script_path> << EOF\n<script_content>\nEOF'

# File operations
docker exec ars0n-framework-v2-cloud_enum-1 test -f /app/rs0nfuzz.txt
docker exec ars0n-framework-v2-cloud_enum-1 rm -f <tempfile>
```

**Locations:**
- `server/main.go:2854-2944` (Burp Suite integration)
- `server/utils/cloudEnumUtils.go:576` (script execution)

---

### 2. `docker cp` Commands

#### 2.1 Host → Container File Transfers
```bash
# Nuclei template uploads
docker cp <host_temp_file> ars0n-framework-v2-nuclei-1:/custom_templates/custom_<N>.yaml

# Target file uploads (Nuclei)
docker cp <host_targets_file> ars0n-framework-v2-nuclei-1:/targets.txt

# URL file uploads (metadata extraction)
docker cp <host_urls_file> ars0n-framework-v2-nuclei-1:/urls.txt

# Wordlist uploads (ShuffleDNS)
docker cp <host_wordlist> ars0n-framework-v2-shuffledns-1:/tmp/wordlist.txt

# Cloud enum configuration uploads
docker cp <host_config> ars0n-framework-v2-cloud_enum-1:<dest_path>
```

**Locations:**
- `server/utils/nucleiUtils.go:224` (template upload)
- `server/utils/nucleiUtils.go:144` (targets upload - referenced in code)
- `server/utils/metaDataUtils.go:417` (URLs for metadata)
- `server/utils/metaDataUtils.go:676` (URLs for tech detection)
- `server/utils/bruteForceUtils.go:637` (wordlist for DNS brute force)
- `server/utils/cloudEnumUtils.go:552-600` (config file uploads)

#### 2.2 Container → Host File Transfers
```bash
# Nuclei output extraction
docker cp ars0n-framework-v2-nuclei-1:/output.jsonl <host_output_file>

# Cloud enum output extraction
docker cp ars0n-framework-v2-cloud_enum-1:<container_file> <host_temp_file>
```

**Locations:**
- `server/utils/nucleiUtils.go:257-262` (output file extraction)
- `server/main.go:2896` (Burp Suite file extraction)

---

### 3. `docker run` Commands (Ephemeral Containers)

#### 3.1 Amass Enumeration
```bash
docker run --rm caffix/amass enum -active -alts -brute -nocolor \
  -min-for-recursive 2 -timeout 60 -d <domain> \
  -r 8.8.8.8 -r 1.1.1.1 -r 9.9.9.9 -r 64.6.64.6 \
  -r 208.67.222.222 -r 208.67.220.220 -r 8.26.56.26 \
  -r 8.20.247.20 -r 185.228.168.9 -r 185.228.169.9 \
  -r 76.76.19.19 -r 76.223.122.150 -r 198.101.242.72 \
  -r 176.103.130.130 -r 176.103.130.131 -r 94.140.14.14 \
  -r 94.140.15.15 -r 1.0.0.1 -r 77.88.8.8 -r 77.88.8.1 \
  -rqps <rate_limit>
```

**Locations:**
- `server/utils/amassUtils.go:605-632` (domain enumeration)
- `server/utils/amassEnumUtils.go:147-148` (enum utility)

#### 3.2 Amass Intelligence
```bash
docker run --rm caffix/amass intel -org <company_name>
```

**Locations:**
- `server/utils/amassIntelUtils.go:101-102` (company intelligence gathering)

#### 3.3 Other External Containers
```bash
# GAU (GetAllURLs) - referenced but not fully implemented
docker run --rm <gau_container> <args>

# Sublist3r alternative execution
docker run --rm <sublist3r_container> <args>
```

**Locations:**
- `server/utils/subdomainScrapingUtils.go:658` (alternative Sublist3r)
- `server/utils/subdomainScrapingUtils.go:700` (GAU execution)
- `server/utils/urlScanUtils.go:546` (additional run patterns)

---

### 4. `docker ps` Commands

#### 4.1 Container Status Checks
```bash
docker ps --filter name=ars0n-framework-v2-github-recon-1 --format {{.Status}}
```

**Locations:**
- `server/utils/githubReconUtils.go:158` (GitHub recon health check)

---

## Container-Specific Commands

### Container: `ars0n-framework-v2-nuclei-1`

**Total Commands:** 30+

| Operation | Command | Frequency | Files |
|-----------|---------|-----------|-------|
| Scan execution | `docker exec -i ... nuclei <args>` | High | nucleiUtils.go, metaDataUtils.go, screenshotUtils.go |
| Directory creation | `docker exec ... mkdir -p /custom_templates` | Low | nucleiUtils.go:200 |
| File upload | `docker cp <host> nuclei-1:<path>` | High | nucleiUtils.go, metaDataUtils.go |
| Output reading | `docker exec ... cat /output.jsonl` | High | nucleiUtils.go:265 |
| Screenshot listing | `docker exec ... ls /app/screenshots/` | Medium | screenshotUtils.go:201 |
| Screenshot reading | `docker exec ... cat /app/screenshots/<file>` | Medium | screenshotUtils.go:228 |
| Cleanup | `docker exec ... rm -f <files>` | High | nucleiUtils.go:294, metaDataUtils.go |

**Access Pattern:**
- Templates uploaded via `docker cp` → Scan via `docker exec` → Results via `docker cp` or `cat`

---

### Container: `ars0n-framework-v2-metabigor-1`

**Total Commands:** 6

| Operation | Command Pattern | Purpose |
|-----------|----------------|---------|
| Company network lookup | `echo '<name>' \| docker exec -i ... metabigor net --org -v` | ASN discovery |
| Company netd lookup | `echo '<name>' \| docker exec -i ... metabigor netd --org` | Network data |
| ASN network lookup | `echo '<asn>' \| docker exec -i ... metabigor net --asn` | ASN enumeration |
| ASN netd lookup | `echo '<asn>' \| docker exec -i ... metabigor netd --asn` | ASN details |
| IP port scan | `echo '<ips>' \| docker exec -i ... metabigor ip -open` | Open ports |
| IP CIDR lookup | `echo '<ips>' \| docker exec -i ... metabigor ipc --json` | IP ranges |

**Unique Pattern:** All commands use shell pipe (`echo ... | docker exec -i`) for input injection

---

### Container: `ars0n-framework-v2-httpx-1`

**Total Commands:** 3+

| Operation | Command | Purpose |
|-----------|---------|---------|
| HTTP probing | `docker exec ... httpx -silent -json -tech-detect ...` | Live web server detection |

**Locations:**
- `server/utils/liveWebServers.go:244-272`

---

### Container: `ars0n-framework-v2-shuffledns-1`

**Total Commands:** 5+

| Operation | Command | Purpose |
|-----------|---------|---------|
| DNS brute force | `docker exec ... shuffledns -d <domain> -w <wordlist> ...` | Subdomain discovery |
| Wordlist upload | `docker cp <wordlist> shuffledns-1:/tmp/wordlist.txt` | Custom wordlists |

**Locations:**
- `server/utils/bruteForceUtils.go:175-703`

---

### Container: `ars0n-framework-v2-subfinder-1`

**Total Commands:** 2+

| Operation | Command |
|-----------|---------|
| Subdomain enum | `docker exec ... subfinder -d <domain> -all -silent` |

**Locations:**
- `server/utils/subdomainScrapingUtils.go:1242`

---

### Container: `ars0n-framework-v2-sublist3r-1`

**Total Commands:** 2+

| Operation | Command |
|-----------|---------|
| Subdomain scan | `docker exec ... python /app/sublist3r.py -d <domain> -v -t 50 -o /dev/stdout` |

**Locations:**
- `server/utils/subdomainScrapingUtils.go:164-172`

---

### Container: `ars0n-framework-v2-assetfinder-1`

**Total Commands:** 1+

| Operation | Command |
|-----------|---------|
| Asset discovery | `docker exec ... assetfinder --subs-only <domain>` |

**Locations:**
- `server/utils/subdomainScrapingUtils.go:436`

---

### Container: `ars0n-framework-v2-katana-1`

**Total Commands:** 5+

| Operation | Command |
|-----------|---------|
| Web crawling | `docker exec ... katana -u <url> -silent -jsonl` |

**Locations:**
- `server/utils/urlScanUtils.go:59-69`
- `server/utils/metaDataUtils.go:241, 1328`
- `server/utils/katanaCompanyUtils.go:160`

---

### Container: `ars0n-framework-v2-gospider-1`

**Total Commands:** 2+

| Operation | Command |
|-----------|---------|
| Web spidering | `docker exec ... gospider -s <url> -json -silent` |

**Locations:**
- `server/utils/javaScriptLinkDiscovery.go:157`

---

### Container: `ars0n-framework-v2-subdomainizer-1`

**Total Commands:** 6+

| Operation | Command |
|-----------|---------|
| Subdomain extraction | `docker exec ... python3 SubDomainizer.py -u <url> -o /dev/stdout` |

**Locations:**
- `server/utils/javaScriptLinkDiscovery.go:524-640`

---

### Container: `ars0n-framework-v2-linkfinder-1`

**Total Commands:** 1+

| Operation | Command |
|-----------|---------|
| Link extraction | `docker exec ... linkfinder -i <url> -o cli` |

**Locations:**
- `server/utils/urlScanUtils.go:224-230`

---

### Container: `ars0n-framework-v2-waybackurls-1`

**Total Commands:** 1+

| Operation | Command |
|-----------|---------|
| Historical URLs | `docker exec ... waybackurls <domain>` |

**Locations:**
- `server/utils/urlScanUtils.go:384-389`

---

### Container: `ars0n-framework-v2-ffuf-1`

**Total Commands:** 5+

| Operation | Command |
|-----------|---------|
| Directory fuzzing | `docker exec ... ffuf -u <url> -w <wordlist> -mc 200,301,302,307,401,403 -json` |
| Output reading | `docker exec ... cat /tmp/ffuf-output.json` |

**Locations:**
- `server/utils/urlScanUtils.go:747-778`
- `server/utils/metaDataUtils.go:1127-1186`

---

### Container: `ars0n-framework-v2-dnsx-1`

**Total Commands:** 2+

| Operation | Command |
|-----------|---------|
| DNS resolution | `docker exec ... dnsx -silent -json -resp -a -aaaa -cname -mx` |

**Locations:**
- `server/utils/dnsxUtils.go:128`

---

### Container: `ars0n-framework-v2-cewl-1`

**Total Commands:** 1+

| Operation | Command |
|-----------|---------|
| Wordlist generation | `docker exec ... cewl -d <depth> -m <min_len> --with-numbers <url>` |

**Locations:**
- `server/utils/bruteForceUtils.go:539`

---

### Container: `ars0n-framework-v2-github-recon-1`

**Total Commands:** 5+

| Operation | Command |
|-----------|---------|
| Status check | `docker ps --filter name=... --format {{.Status}}` |
| Directory listing | `docker exec ... ls -la /app/github-search` |
| Script check | `docker exec ... ls -la /app/github-search/github-endpoints.py` |
| Help command | `docker exec ... python3 ... -h` |
| GitHub scanning | `docker exec ... python3 -u /app/github-search/github-endpoints.py -d <domain> -t <api_key>` |

**Locations:**
- `server/utils/githubReconUtils.go:158-214`

---

### Container: `ars0n-framework-v2-cloud_enum-1`

**Total Commands:** 5+

| Operation | Command |
|-----------|---------|
| File test | `docker exec ... test -f /app/rs0nfuzz.txt` |
| Script creation | `docker exec ... sh -c 'cat > <path> << EOF...'` |
| File copy in | `docker cp <host> cloud_enum-1:<path>` |
| File copy out | `docker cp cloud_enum-1:<path> <host>` |
| Cleanup | `docker exec ... rm -f <file>` |

**Locations:**
- `server/main.go:2854-2944`
- `server/utils/cloudEnumUtils.go:552-600`

---

### External Image: `caffix/amass`

**Total Commands:** 3

| Operation | Command |
|-----------|---------|
| Domain enumeration | `docker run --rm caffix/amass enum -active -alts -brute ...` |
| Company intelligence | `docker run --rm caffix/amass intel -org <company>` |

**Locations:**
- `server/utils/amassUtils.go:605-632`
- `server/utils/amassEnumUtils.go:147-148`
- `server/utils/amassIntelUtils.go:101-102`

---

## File Locations by Command Type

### Files with `docker exec` Commands

1. **server/main.go** (lines 2854, 2884, 2944)
   - Cloud enum container file operations
   - Burp Suite integration

2. **server/utils/nucleiUtils.go** (lines 200, 238-243, 265, 294)
   - Nuclei scan execution
   - Template management
   - Output handling

3. **server/utils/metabigorCompanyUtils.go** (lines 153, 663, 737, 739, 815, 817)
   - All Metabigor operations (piped input)

4. **server/utils/liveWebServers.go** (lines 244-272)
   - HTTPx live web server detection

5. **server/utils/subdomainScrapingUtils.go** (lines 164-172, 436, 1242)
   - Sublist3r, Assetfinder, Subfinder

6. **server/utils/urlScanUtils.go** (lines 59-69, 224-230, 384-389, 747-778)
   - Katana, LinkFinder, WaybackURLs, FFuf

7. **server/utils/javaScriptLinkDiscovery.go** (lines 157, 524-640)
   - GoSpider, Subdomainizer

8. **server/utils/bruteForceUtils.go** (lines 175-703)
   - ShuffleDNS, CeWL

9. **server/utils/dnsxUtils.go** (line 128)
   - DNSx resolution

10. **server/utils/githubReconUtils.go** (lines 158-214)
    - GitHub reconnaissance

11. **server/utils/metaDataUtils.go** (lines 241, 417-530, 676-808, 1127-1328)
    - Metadata extraction with multiple tools

12. **server/utils/screenshotUtils.go** (lines 156-289)
    - Screenshot management

13. **server/utils/katanaCompanyUtils.go** (line 160)
    - Company-level Katana scans

14. **server/utils/cloudEnumUtils.go** (lines 552-600)
    - Cloud enumeration file operations

### Files with `docker cp` Commands

1. **server/utils/nucleiUtils.go** (lines 144, 224, 257-262)
2. **server/utils/metaDataUtils.go** (lines 417, 676)
3. **server/utils/bruteForceUtils.go** (line 637)
4. **server/utils/cloudEnumUtils.go** (lines 552, 588, 600)
5. **server/main.go** (line 2896)

### Files with `docker run` Commands

1. **server/utils/amassUtils.go** (lines 605-632)
2. **server/utils/amassEnumUtils.go** (lines 147-148)
3. **server/utils/amassIntelUtils.go** (lines 101-102)
4. **server/utils/subdomainScrapingUtils.go** (lines 658, 700)
5. **server/utils/urlScanUtils.go** (line 546)

### Files with `docker ps` Commands

1. **server/utils/githubReconUtils.go** (line 158)

---

## Security Implications

### High Risk Operations

1. **Docker Socket Mounting** (`/var/run/docker.sock`)
   - **Risk:** Full Docker daemon access from API container
   - **Impact:** Container escape potential, host system access
   - **Mitigation:** API container runs with limited privileges, but socket access is inherently risky

2. **File Transfer Operations** (`docker cp`)
   - **Risk:** File injection into containers, data exfiltration
   - **Impact:** Malicious file uploads, sensitive data extraction
   - **Files:** 8+ locations across utils/
   - **Mitigation:** Input validation on file paths and content

3. **Shell Command Injection** (Metabigor piped commands)
   - **Risk:** Command injection via shell pipes
   - **Files:** `metabigorCompanyUtils.go`
   - **Pattern:** `echo '<user_input>' | docker exec -i ...`
   - **Impact:** Arbitrary command execution if input not sanitized
   - **Mitigation:** Input sanitization required

4. **Arbitrary Container Execution**
   - **Risk:** Executing arbitrary commands in tool containers
   - **Impact:** Container compromise, resource abuse
   - **Scope:** All 17+ tool containers accessible

### Medium Risk Operations

1. **Interactive Docker Exec** (`docker exec -i`)
   - Used for: Nuclei scans, Metabigor operations
   - Allows stdin piping to containers
   - Requires careful input validation

2. **External Image Execution** (`docker run --rm caffix/amass`)
   - Pulls and runs third-party images
   - Trust dependency on external registry
   - No version pinning observed (latest tag)

3. **Container File System Access**
   - Read/write operations in container filesystems
   - Cleanup operations with `rm -rf`
   - Screenshot directory access

### Low Risk Operations

1. **Container Status Checks** (`docker ps`)
   - Read-only operation
   - Minimal security impact

2. **Ephemeral Containers** (`docker run --rm`)
   - Automatically removed after execution
   - Limited persistence risk

---

## Command Execution Patterns

### Pattern 1: Direct Execution with Output Capture
```go
cmd := exec.Command("docker", "exec", "ars0n-framework-v2-<tool>-1", "<tool>", "<args>")
var stdout, stderr bytes.Buffer
cmd.Stdout = &stdout
cmd.Stderr = &stderr
err := cmd.Run()
```
**Used in:** Most subdomain scrapers, live web servers

### Pattern 2: Interactive Execution with Stdin
```go
dockerArgs := []string{"exec", "-i", "ars0n-framework-v2-nuclei-1", "nuclei", ...}
dockerCmd := exec.Command("docker", dockerArgs...)
output, err := dockerCmd.CombinedOutput()
```
**Used in:** Nuclei scans

### Pattern 3: Piped Shell Execution
```go
command := fmt.Sprintf("echo '%s' | /usr/bin/docker exec -i ars0n-framework-v2-metabigor-1 metabigor net --org -v", name)
output, err := exec.Command("sh", "-c", command).CombinedOutput()
```
**Used in:** Metabigor operations

### Pattern 4: File Transfer Operations
```go
// Host to Container
copyCmd := exec.Command("docker", "cp", sourceFile, "ars0n-framework-v2-<container>-1:"+destPath)
copyCmd.Run()

// Container to Host
copyCmd := exec.Command("docker", "cp", "ars0n-framework-v2-<container>-1:"+sourcePath, destFile)
copyCmd.Run()
```
**Used in:** Nuclei templates, wordlist uploads, output extraction

### Pattern 5: Ephemeral Container Execution
```go
cmd := exec.Command(
    "docker", "run", "--rm",
    "caffix/amass",
    "enum", "-active", "-alts", "-brute",
    "-d", domain,
    "-r", "8.8.8.8", ...)
cmd.Run()
```
**Used in:** Amass scans

### Pattern 6: Multi-Stage Operations
```go
// 1. Upload target file
exec.Command("docker", "cp", targetFile, "container:/targets.txt").Run()

// 2. Execute scan
exec.Command("docker", "exec", "-i", "container", "nuclei", "-l", "/targets.txt").Run()

// 3. Extract results
exec.Command("docker", "cp", "container:/output.jsonl", hostFile).Run()

// 4. Cleanup
exec.Command("docker", "exec", "container", "rm", "-f", "/targets.txt", "/output.jsonl").Run()
```
**Used in:** Nuclei scans, metadata extraction

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| **Total Go files with Docker commands** | 20+ |
| **Total Docker command invocations** | 100+ |
| **Containers controlled by API** | 17+ tools + 1 external |
| **Most used command** | `docker exec` (80+) |
| **Most accessed container** | `ars0n-framework-v2-nuclei-1` (30+ commands) |
| **External images used** | 1 (`caffix/amass`) |
| **File transfer operations** | 15+ |
| **Containers with piped input** | 1 (`metabigor-1`) |
| **Lines of Docker-related code** | 2000+ (estimated) |

---

## Architectural Notes

1. **Centralized Orchestration:** All Docker commands originate from the Go API server
2. **No Inter-Container Communication:** Containers don't directly communicate; API server mediates
3. **Sleep Strategy:** Tool containers use `sleep infinity` and are invoked via `docker exec`
4. **Ephemeral External Containers:** Amass runs as `docker run --rm` (auto-removed)
5. **File-Based I/O:** Most tools use file transfer for complex inputs/outputs
6. **Socket Dependency:** Entire system depends on `/var/run/docker.sock` mount

---

## Conclusion

The Ars0n Framework v2 uses Docker extensively as a **containerization and isolation layer** for security reconnaissance tools. The Go API server acts as a **container orchestrator**, executing 100+ distinct Docker commands across 17+ tool containers. The architecture is heavily dependent on `docker exec` for tool invocation, `docker cp` for file transfers, and `docker run --rm` for external tools.

**Key Takeaways:**
- Docker socket access grants the API container **full control** over the Docker daemon
- All tool execution is **synchronous and blocking** (no async container jobs observed)
- **File-based communication** is the primary I/O pattern
- Security depends on **input validation** in the Go API layer
- No container-to-container networking; API server is the **single point of control**

---

**Document Version:** 1.0
**Generated By:** Claude Code Analysis
**Analysis Scope:** Complete codebase at `/home/user/ars0n-framework-v2`

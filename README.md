# public-sources
collect IPv6 address from public sources

## Domain Lists: 
resolved for AAAA records on a daily basis, yielding about 9.8 M unique IP addresses. This source also includes domains extracted from blacklists provided by Spamhaus, APWG, and Phishtank, which leverage 8.5 M, 376 k, and 170 k domains, respectively.

# FDNS: 
A comprehensive set of forward DNS (FDNS) ANY lookups performed by Rapid7. CT: DNS domains extracted from TLS certificates logged in
Certificate Transparency (CT), and not already part of domain lists, which yields another 16.2 M addresses.

# AXFR and TLDR: 
IPv6 addresses obtained from DNS zone transfers (AXFR) from the TLDR project and our own AXFR transfers. Obtained domain names are also resolved for AAAA
records daily.

# Bitnodes: 
To gather client IPv6 addresses, we use the Bitnodes API, that provides current peers of the Bitcoin network. Although this is the smallest source, we still find it valuable as it also adds client addresses.

# RIPE Atlas: 
We extract all IPv6 addresses found in RIPE Atlas traceroutes, as well as all IPv6 addresses from RIPE’s ipmap project. These are highly disjoint from previous sources, likely due to their nature as routers.

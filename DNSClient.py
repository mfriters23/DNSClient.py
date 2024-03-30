import dns.resolver

# Set the IP address of the local DNS server and a public DNS server
local_host_ip = '192.168.1.1'  # Placeholder IP for a local DNS server
real_name_server = '8.8.8.8'  # Google's public DNS server

# Create a list of domain names to query
domainList = ['example.com.', 'safebank.com.', 'google.com.', 'nyu.edu.', 'legitsite.com.']

def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    answers = resolver.resolve(domain, question_type)
    ip_address = answers[0].to_text()
    return ip_address   

def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answers = resolver.resolve(domain, question_type)
    ip_address = answers[0].to_text()
    return ip_address

def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        local_ip_address = query_local_dns_server(domain_name, question_type)
        public_ip_address = query_dns_server(domain_name, question_type)
        if local_ip_address != public_ip_address:
            return False
    return True    

def local_external_DNS_output(question_type):    
    print("Local DNS Server")
    for domain_name in domainList:
        ip_address = query_local_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {ip_address}")

    print("\nPublic DNS Server")
    for domain_name in domainList:
        ip_address = query_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {ip_address}")

def exfiltrate_info(domain_name, question_type):
    data = query_local_dns_server(

if __name__ == '__main__':
    question_type = 'A'  # The type of DNS query to be performed

    # Call the function to print the results from querying both DNS servers
    local_external_DNS_output(question_type)
    
    # Call the function to compare the results from both DNS servers and print the result
    result = compare_dns_servers(domainList, question_type)
    result = query_local_dns_server('nyu.edu', question_type)
    print (result)
       

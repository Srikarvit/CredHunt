from core.scanner import CredentialScanner
from core.reporter import ReportGenerator


if __name__ == "__main__":
    path = input("Enter path to scan for credentials: ")
    scanner = CredentialScanner(path)
    findings = scanner.scan()


if findings:
    report = ReportGenerator(findings)
    report.create_html_report()
    print("Scan complete. Report saved as credhunt_report.html")
else:
    print("No sensitive credentials found.")
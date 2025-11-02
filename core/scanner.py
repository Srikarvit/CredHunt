import os
import re
from .utils import hash_string


class CredentialScanner:
    def __init__(self, root_path):
        self.root_path = root_path
        self.patterns = [
            (r'[A-Za-z0-9+/=]{40,}', 'Possible API Key'),
            (r'AKIA[0-9A-Z]{16}', 'AWS Access Key'),
            (r'-----BEGIN PRIVATE KEY-----', 'Private Key'),
            (r'password\s*=\s*["\'].*?["\']', 'Password String')
        ]

    def scan(self):
        results = []
        for root, _, files in os.walk(self.root_path):
            for file in files:
                if file.endswith(('.py', '.env', '.txt', '.cfg', '.json')):
                    path = os.path.join(root, file)
                    with open(path, 'r', errors='ignore') as f:
                        content = f.read()
                    for pattern, desc in self.patterns:
                        for match in re.finditer(pattern, content):
                            snippet = match.group(0)[:80]
                            results.append({
                                'file': path,
                                'type': desc,
                                'hash': hash_string(snippet),
                                'snippet': snippet
                            })
        return results

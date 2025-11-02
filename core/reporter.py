from jinja2 import Environment, FileSystemLoader
import pdfkit
import os


class ReportGenerator:
    def __init__(self, findings):
        self.findings = findings


    def create_html_report(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report_template.html')
        output_html = template.render(findings=self.findings)
        with open('credhunt_report.html', 'w', encoding='utf-8') as f:
            f.write(output_html)


        # Convert HTML to PDF (optional)
        if os.path.exists('C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'):
            pdfkit.from_file('credhunt_report.html', 'credhunt_report.pdf')
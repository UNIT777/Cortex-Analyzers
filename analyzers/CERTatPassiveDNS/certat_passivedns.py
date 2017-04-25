#!/usr/bin/env python
from cortexutils.analyzer import Analyzer
from whois_wrapper import query


class CERTatPassiveDNSAnalyzer(Analyzer):
    """Very simple passive dns wrapper for pdns.cert.at. Needs no credentials because access is controlled through
    firewall rules. If you want to get access, you have to contact CERT.AT, but:
    
    CERT.AT pDNS is not a public service. It is only available for national / governmental CERTs in good standing with
    CERT.AT. For access, you have to get in contact with CERT.AT.
    """
    def __init__(self):
        Analyzer.__init__(self)
        self.limit = self.get_param('config.limit', '100')

    def run(self):
        self.report({'results': query(self.getData(), int(self.limit))})

    def summary(self, raw):
        results = raw.get('results')
        return {'hits': len(results)}

if __name__ == '__main__':
    CERTatPassiveDNSAnalyzer().run()

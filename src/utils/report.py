

class Report:

    @staticmethod
    def get_report_summary(terminalreporter):
        """
            获取所有的测试用例结果
        """
        passed, failed, skipped = [], [], []
        for status, reports in terminalreporter.stats.items():
            if status == 'passed':
                for report in reports:
                    nodeid = report.nodeid
                    passed.append({nodeid: ""})
            elif status == 'failed':
                for report in reports:
                    nodeid = report.nodeid
                    reason = report.longreprtext
                    failed.append({nodeid: reason})
            elif status == 'skipped':
                for report in reports:
                    nodeid = report.nodeid
                    reason = report.longreprtext
                    skipped.append({nodeid: reason})

        return passed, failed, skipped

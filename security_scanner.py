def scan_vulnerabilities(code_str):
    findings = []
    if "eval(" in code_str or "exec(" in code_str:
        findings.append("CRITICAL: Arbitrary code execution vulnerability (eval/exec detected).")
    if "SELECT *" in code_str and "f"" in code_str:
        findings.append("HIGH: Potential SQL Injection vulnerability detected in query formatting.")
    return findings

# SAST and DAST

- both are application security Testing approaches used in DevSecOps pipelines.

## SAST - Static Application Security Testing

- White Box Testing
- Scans source code, byte code, binaries.
- find vulnerabilities without running application.

### What we can detect

- Harcoded passwords (secrets) in application
- insecure auth logic
- Buffer overflow
- code level security problems
- SQL ibjection

### Tools

- SonarQube
- Fortify

### Advantages

- find issues early
- exact line of code with problem
- no need to run application

### Disadvantage

- cannot detect problems runtime
- cannot fine any confiuration issues.

# DAST - Dynamic App security Testing
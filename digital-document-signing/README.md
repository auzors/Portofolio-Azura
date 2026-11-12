# Digital Document Signing Automation Using Bash Script

## Overview

Digital Document Signing Automation is a Linux-based project that utilizes Bash scripting to automate the process of generating digital certificates and signing PDF documents.

The system was developed to simplify PDF document signing through a command-line interface using OpenSSL and OpenPSFSign.

## Project Objectives

- Automate the generation of RSA-based digital certificates.
- Simplify PDF document signing through Bash scripting.
- Implement input validation and file handling to minimize user errors.
- Verify digitally signed PDF documents.

## Key Features

- **Operating System Verification:** Checks whether the system runs on a supported Debian-based Linux distribution.
- **Certificate Generation:** Generates self-signed RSA certificates using OpenSSL.
- **PDF File Validation:** Validates PDF file extensions and MIME types.
- **Digital Signing:** Applies digital signatures to PDF documents using OpenPSFSign.
- **Certificate Reuse:** Allows users to select an existing certificate.
- **Output Management:** Provides options for selecting output locations and handling existing files.

## Technologies & Tools

- Bash Script
- Linux (Debian/Ubuntu)
- OpenSSL
- RSA Digital Certificates
- OpenPSFSign

## Testing & Results

The system was tested through the Ubuntu terminal, including certificate generation, PDF signing, and certificate reuse.

The resulting signed PDF was also tested using the TTE Kominfo verification website. According to the project report, the verification process recognized the digital signature.

## Project Type

Academic Group Project

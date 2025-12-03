# AI-Based Classification of Certificate Validation Errors
#Comp 3106 Project
#Ben Kyd 101167318

## Overview
This project applies artificial intelligence methods to simplify the interpretation of OpenSSL error messages.  
Instead of parsing certificates directly, the problem is reframed as a **text classification task**: given an error message, predict its category.  
The classifier provides structured, human-friendly categories such as:
- `expired`
- `name_mismatch`
- `untrusted_root`
- `signature_failure`
- `other`

The implementation uses a Naïve Bayes classifier trained on synthetic OpenSSL-style error messages.

---

## Repository Structure


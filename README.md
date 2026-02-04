# Eton College Investment Challenge Certificates

This project contains Python scripts to generate SVG certificates for the Eton College Investment Challenge 2026.

## Scripts

### 1. Participation Certificate (`certificates.py`)
Generates the standard participation certificate with a gold/yellow color scheme.

**Usage:**
```bash
python certificates.py --name "Student Name"
```
*Note: If no name is provided, it defaults to "Sample Student".*

**Options:**
- `--name`: Name of the participant (Optional, defaults to "Sample Student").
- `--date`: Date string to display (Optional, defaults to today's date).
- `--output`: Output filename (Optional, defaults to `eton_certificate.svg`).

**Example:**
```bash
python certificates.py --name "Alice Smith" --date "22 January 2026"
```

### 2. Finalist Certificate (`finalists.py`)
Generates the finalist certificate with an emerald/green color scheme.

**Usage:**
```bash
python finalists.py --name "Student Name"
```
*Note: If no name is provided, it defaults to "Sample Student".*

**Options:**
- `--name`: Name of the finalist (Required).
- `--date`: Date string to display (Optional, defaults to today's date).
- `--output`: Output filename (Optional, defaults to `eton_finalist_certificate.svg`).

**Example:**
```bash
python finalists.py --name "Bob Jones" --output "finalist_bob.svg"
```

## Requirements
- Python 3.x
- Standard libraries only (no external `pip` packages required).

## Assets
The scripts require the following image assets in the `Assets` folder:
- `etonlogo.png`
- `ECHCIC.png`
- `fminstitute_logo.png`

## Output
Each script generates an `.svg` file.

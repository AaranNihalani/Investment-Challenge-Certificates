# Eton College Investment Challenge Certificates

This project contains Python scripts to generate SVG certificates for the Eton College Investment Challenge 2026.

## Scripts

### 1. Participation Certificate (`certificates.py`)
Generates standard participation certificates with a gold/yellow color scheme.

**Usage:**
1. Ensure `participants.csv` exists in the same directory. The CSV should contain names in the first column (no header required).
2. Run the script:
   ```bash
   python certificates.py
   ```
3. Certificates will be generated in the `participants/` folder as `Name_certificate.svg`.

### 2. Finalist Certificate (`finalists.py`)
Generates finalist certificates with an emerald/green color scheme.

**Usage:**
1. Ensure `finalists.csv` exists in the same directory. The CSV should contain names in the first column (no header required).
2. Run the script:
   ```bash
   python finalists.py
   ```
3. Certificates will be generated in the `finalists/` folder as `Name_certificate.svg`.

## Requirements
- Python 3.x
- Standard libraries only (no external `pip` packages required).

## Assets
The scripts require the following image assets in the `Assets` folder:
- `etonlogo.png`
- `ECHCIC.png`
- `fminstitute_logo.png`
- `koyfin_logo.png`

## Output
Each script generates `.svg` files in their respective folders (`participants/` and `finalists/`).

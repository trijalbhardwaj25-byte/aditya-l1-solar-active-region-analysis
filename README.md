# 🌞 Aditya-L1 Solar Active Region Analysis

## Overview

This project was completed as part of the **ISA (Indian Space Academy) Aditya-L1 Internship Program**.

The objective of this project was to analyze solar active regions using observations from the **Solar Ultraviolet Imaging Telescope (SUIT)** onboard **Aditya-L1**. The project involved image preprocessing, segmentation, temporal analysis, correlation analysis, and an independent multi-wavelength investigation.

---

## Student Information

**Name:** Trijal Bhardwaj

**Program:** B.Tech Computer Science & Engineering (AI & ML)

**Institution:** Manipal University Jaipur

**Internship:** ISA (Indian Space Academy) Aditya-L1 Internship Program

---

## Project Components

### Part 1: Active Region Detection

* FITS image processing using SunPy
* Image normalization
* Threshold-based segmentation
* Active region detection
* Contour visualization
* NOAA validation
* Solar activity animation

### Part 2: Advanced Analysis

#### Question A: Temporal Evolution

* Multi-date active region tracking
* Area measurement
* Growth and decay analysis
* Area vs Time visualization

#### Question B: Correlation Analysis

* Active region intensity extraction
* Pearson correlation analysis
* Spearman correlation analysis
* Statistical interpretation

#### Question C: Segmentation Comparison

* Fixed Thresholding
* Otsu Thresholding
* Adaptive Thresholding
* NOAA comparison
* Evaluation metrics analysis

### Part 3: Independent Exploration

**Research Question:**

> How does the visibility, apparent area, and intensity of solar active regions vary across different SUIT ultraviolet filters?

Features:

* Multi-wavelength analysis
* NB02, NB03, NB04 and NB05 comparison
* Active region measurements
* Dashboard visualization
* Heatmap visualization
* Quantitative analysis

---

## Technologies Used

* Python
* SunPy
* Astropy
* NumPy
* Matplotlib
* Scikit-Image
* Jupyter Notebook

---

## Repository Structure

```text
NOTEBOOKS/
REPORT/
RESULTS/
DATA/
src/
part 2/
part 3/
```

---

## Key Results

### Temporal Analysis

* Active region evolution tracked across multiple observation dates.
* Growth and decay patterns quantified using area measurements.

### Correlation Analysis

* Pearson Correlation: -0.1347
* Spearman Correlation: 0.0000

No statistically significant correlation was observed for the analyzed dataset.

### Multi-Wavelength Investigation

| Filter | Regions | Largest Area | Mean Intensity |
| ------ | ------: | -----------: | -------------: |
| NB02   |       4 |        39154 |         0.7772 |
| NB03   |       4 |         2042 |         0.7954 |
| NB04   |       3 |         2070 |         0.7890 |
| NB05   |       2 |        62860 |         0.7784 |

The analysis demonstrated that active-region appearance varies significantly across different SUIT ultraviolet filters.

---

## References

* ISRO Aditya-L1 Mission Documentation
* SUIT Instrument Documentation
* SunPy Documentation
* Astropy Documentation
* NOAA Solar Region Reports

---

## Acknowledgement

This work was completed as part of the ISA Aditya-L1 Internship Program using data obtained from the Solar Ultraviolet Imaging Telescope (SUIT) onboard India's Aditya-L1 solar mission.

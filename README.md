# Cell Tracking App

![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-orange)

A professional, modular Python application for robust cell tracking and analysis in microscopy videos.

## 🚀 Features

### Core Tracking
- **Kalman Filtering:** Robust state estimation for occlusion handling.
- **Hungarian Algorithm:** Optimal frame-to-frame association.
- **Multi-Object Tracking:** Efficiently tracks hundreds of cells simultaneously.

### User Interface
- **Interactive Player:** Play, pause, and scrub through processed videos.
- **Real-time Visualization:** View tracks and IDs overlaid on the video.

### Analysis & Export
- **Metrics:** Automated calculation of cell velocity, displacement, and MSD.
- **Data Export:** Export trajectories to CSV for downstream analysis.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdullah-tauqeer-0/CELL_Tracking_APP.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the main application:
```bash
python src/main.py
```

1. Click **Load Video** to select a microscopy recording.
2. The tracking will initialize automatically.
3. Use the playback controls to review the results.

## 📊 Project Structure
```
src/
├── gui/         # UI components (PyQt5)
├── tracking/    # Tracking algorithms (Kalman, Hungarian)
├── analysis/    # Metrics and plotting
└── utils/       # Video I/O helpers
```

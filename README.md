# E-Paper Display Library

A modernized version of the [Waveshare e-Paper library](https://github.com/waveshareteam/e-Paper.git) that uses `python-periphery` for hardware interface and `uv` for package management.

## What's Different

- Uses `python-periphery` instead of direct GPIO/SPI access
- Uses `uv` for fast Python package management
- Updated to modern Python practices
- Better error handling and logging
- Simplified project structure

## Quick Start

1. Install dependencies:
```bash
uv sync
```

2. Run the simple demo:
```bash
python demo.py
```

3. Or run the full demo with animations:
```bash
python start.py
```

## Project Structure

```
waveshare_epaper/
├── epd/                   # E-paper display modules
├── demo.py               # Simple demo script
├── start.py              # Full demo with animations
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## Supported Displays

Works with various e-paper displays: 1.54", 2.13", 2.7", 2.9", 4.2", 5.83", and 7.5" models.

## Demo Features

The demo scripts showcase:
- Text and graphics rendering
- Image display
- 4-gray mode
- Partial update animations
- Perimeter box animation with center text counter

## Requirements

- Python 3.8+
- `uv` package manager
- `python-periphery`
- PIL/Pillow

## License

Based on the original Waveshare e-Paper library. See the [original repository](https://github.com/waveshareteam/e-Paper.git) for licensing details.
# STAC Ingestion for Zeno

## Set up

Set up environment variables in a `.env` file by making a copy
of the example env and edit the variables there.

```bash
cp .env.example .env
```

## Usage

### Running the ingestion scripts

1. Activate the virtual environment
2. Run the main script:

   ```bash
   ./ingest_all.sh
   ```

This script ingests the following datasets:
- DIST-ALERTS
- GLOBAL LAND COVER
- GRASSLANDS
- NATURAL LANDS
- TREE COVER LOSS

## COG Creation Scripts

These scripts only have been used once to create global COG files for
Land cover and natural lands. Re-run manually when new data updates
are available.

### merge_global_land_cover.sh

Creates global Cloud-Optimized GeoTIFF (COG) files from Global Land Cover
data for years 2015-2024.

**Usage:** `./merge_global_land_cover.sh <local_dir>`

**What it does:**

- Downloads tiles from Google Cloud Storage (`gs://lcl_tiles/LCL_landCover/v3/`)
- Creates VRT files combining all tiles for each year
- Converts to COG format with LZW compression
- Outputs: `global_land_cover_YYYY.tif` files

#### Command to sync data

Command to upload land cover data from the output folder to S3.

```bash
uv run aws s3 sync global_land_cover/ s3://lcl-cogs/global-land-cover/ --exclude "*" --include "*.tif" --exclude "**/*.tif"
```

### merge_natural_lands.sh

Creates a global COG file from Natural Lands classification data.

**Usage:** `./merge_natural_lands.sh`

**What it does:**

- Downloads Natural Lands classification tiles from `gs://lcl_public/SBTN_NaturalLands/v1_1/classification`
- Creates a VRT file combining all tiles
- Converts to COG format with LZW compression
- Outputs: `natural_lands.tif`

## Utility Scripts

### delete_all_stac_data.py

Utility script to delete all STAC data (items and collections) from the database.
Requires confirmation before deletion.

**Usage:** `uv run python delete_all_stac_data.py`

### generate_tile_urls.py

Utility script for generating tile URLs (used for visualization/testing purposes).

**Usage:** `uv run python generate_tile_urls.py`

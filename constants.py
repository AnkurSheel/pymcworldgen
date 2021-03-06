#!/usr/bin/env python

"""

pyMCWorldGen Constants and assumptions

"""

CHUNK_WIDTH_IN_BLOCKS = 16
CHUNK_HEIGHT_IN_BLOCKS = 128
REGION_WIDTH_IN_CHUNKS = 32

# Block ID constants
try:
    from pymclevel import materials
    MAT_AIR = materials.alphaMaterials.Air.ID
    MAT_STONE = materials.alphaMaterials.Stone.ID
    MAT_DIRT = materials.alphaMaterials.Dirt.ID
    MAT_WOOD = materials.alphaMaterials.Wood.ID
    MAT_WATER = materials.alphaMaterials.WaterActive.ID
    MAT_SNOW = materials.alphaMaterials.Snow.ID
    MAT_BEDROCK = materials.alphaMaterials.Bedrock.ID
    MAT_LEAVES = materials.alphaMaterials.Leaves.ID
    MAT_GRASS = materials.alphaMaterials.Grass.ID
    MAT_DIAMONDORE = materials.alphaMaterials.DiamondOre.ID
    MAT_REDSTONEORE = materials.alphaMaterials.RedstoneOre.ID
    MAT_LAPISORE = materials.alphaMaterials.LapisLazuliOre.ID
    MAT_GOLDORE = materials.alphaMaterials.GoldOre.ID
    MAT_IRONORE = materials.alphaMaterials.IronOre.ID
    MAT_COALORE = materials.alphaMaterials.CoalOre.ID
except ImportError:
    MAT_AIR = 0
    MAT_STONE = 1
    MAT_DIRT = 3
    MAT_WOOD = 17
    MAT_WATER = 8
    MAT_SNOW = 78
    MAT_BEDROCK = 7
    MAT_LEAVES = 18
    MAT_GRASS = 2
    MAT_DIAMONDORE = 56
    MAT_REDSTONEORE = 73
    MAT_LAPISORE = 21
    MAT_GOLDORE = 14
    MAT_IRONORE = 15
    MAT_COALORE = 16
MAT_TRANSPARENT = -1

# LayerMask height constants
MASK_HEIGHT_MAX = 1.0
MASK_HEIGHT_MIN = 0.0
MASK_HEIGHT_TRANSPARENT = -1.0

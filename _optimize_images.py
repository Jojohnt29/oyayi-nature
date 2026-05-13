# -*- coding: utf-8 -*-
"""Compress and resize all critical site images in place.

Targets:
- assets/distinctions/*.jpg (8 photos up to 1.2 MB each)  →  1400px max, q78
- assets/catalog/*.png      (36 photos up to 700 KB each)  →  PNG optimize
- assets/products/*.png     (13 bottles ~500 KB each)      →  PNG optimize

Mirrored to v2/assets/* (same files, same paths)."""

import os, sys, io
from PIL import Image
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))

TOTAL_BEFORE = 0
TOTAL_AFTER = 0
COUNT = 0

def shrink_jpg(path, max_side=1400, quality=78):
    """Resize JPG so longest side <= max_side and re-save with given quality."""
    global TOTAL_BEFORE, TOTAL_AFTER, COUNT
    before = os.path.getsize(path)
    img = Image.open(path)
    img = img.convert('RGB')
    w, h = img.size
    if max(w, h) > max_side:
        if w > h:
            new_w = max_side
            new_h = int(h * max_side / w)
        else:
            new_h = max_side
            new_w = int(w * max_side / h)
        img = img.resize((new_w, new_h), Image.LANCZOS)
    img.save(path, 'JPEG', quality=quality, optimize=True, progressive=True)
    after = os.path.getsize(path)
    TOTAL_BEFORE += before
    TOTAL_AFTER += after
    COUNT += 1
    pct = 100 * (1 - after / before)
    print(f'  {os.path.relpath(path, ROOT):60s}  {before//1024:>5}KB  →  {after//1024:>5}KB  (-{pct:4.0f}%)')

def shrink_png(path, max_side=1400):
    """Resize PNG so longest side <= max_side and re-save with optimize."""
    global TOTAL_BEFORE, TOTAL_AFTER, COUNT
    before = os.path.getsize(path)
    img = Image.open(path)
    w, h = img.size
    resized = False
    if max(w, h) > max_side:
        if w > h:
            new_w = max_side
            new_h = int(h * max_side / w)
        else:
            new_h = max_side
            new_w = int(w * max_side / h)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        resized = True
    img.save(path, 'PNG', optimize=True)
    after = os.path.getsize(path)
    TOTAL_BEFORE += before
    TOTAL_AFTER += after
    COUNT += 1
    pct = 100 * (1 - after / before)
    mark = '(resized)' if resized else '(optimized only)'
    print(f'  {os.path.relpath(path, ROOT):60s}  {before//1024:>5}KB  →  {after//1024:>5}KB  (-{pct:4.0f}%)  {mark}')

print('=== Distinctions (JPG resize to 1400px, q78) ===')
for root_dir in [os.path.join(ROOT, 'assets', 'distinctions'),
                  os.path.join(ROOT, 'v2', 'assets', 'distinctions')]:
    if not os.path.exists(root_dir): continue
    for fname in sorted(os.listdir(root_dir)):
        if fname.lower().endswith(('.jpg', '.jpeg')):
            shrink_jpg(os.path.join(root_dir, fname), max_side=1400, quality=78)

print()
print('=== Catalog (PNG resize to 1200px + optimize) ===')
for root_dir in [os.path.join(ROOT, 'assets', 'catalog'),
                  os.path.join(ROOT, 'v2', 'assets', 'catalog')]:
    if not os.path.exists(root_dir): continue
    for fname in sorted(os.listdir(root_dir)):
        if fname.lower().endswith('.png'):
            shrink_png(os.path.join(root_dir, fname), max_side=1200)
        elif fname.lower().endswith(('.jpg', '.jpeg')):
            shrink_jpg(os.path.join(root_dir, fname), max_side=1200, quality=80)

print()
print('=== Products (PNG bottles — resize to 1024px + optimize) ===')
for root_dir in [os.path.join(ROOT, 'assets', 'products'),
                  os.path.join(ROOT, 'v2', 'assets', 'products')]:
    if not os.path.exists(root_dir): continue
    for fname in sorted(os.listdir(root_dir)):
        if fname.lower().endswith('.png'):
            shrink_png(os.path.join(root_dir, fname), max_side=1024)

print()
print(f'=== TOTAL : {COUNT} files ===')
print(f'  Before : {TOTAL_BEFORE//1024//1024} MB ({TOTAL_BEFORE:,} bytes)')
print(f'  After  : {TOTAL_AFTER//1024//1024} MB ({TOTAL_AFTER:,} bytes)')
print(f'  Saved  : {(TOTAL_BEFORE-TOTAL_AFTER)//1024//1024} MB  (-{100*(1-TOTAL_AFTER/TOTAL_BEFORE):.1f}%)')

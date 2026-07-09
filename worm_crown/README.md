# Worm → Crown (Worm Wheel) Calculator & Drawing

Corrected geometry for drawing **WW-150T-2.0-01**, driven from the existing mating worm as entry data.

## What was wrong (Rev A)

Center distance used the worm **major** diameter:

```
a = (da1 + d) / 2 = (28.00 + 303.15) / 2 = 165.58 mm
```

That overstates `a` by one addendum (~2 mm) and disagrees with the stated lead angle (~4.9°), which implies a worm pitch diameter near 24 mm, not 28 mm.

## Fix (Rev B)

```
m  = Px / π
d1 = da1 − 2·m          # worm pitch diameter (ha1 = m)
d  = m · z2             # wheel pitch diameter
a  = (d1 + d) / 2       # center distance
λ  = arctan(L / (π·d1))
```

| Quantity | Rev A | Rev B |
|----------|------:|------:|
| Worm pitch dia `d1` | (implicitly 28) | **23.96 mm** |
| Wheel pitch dia `d` | 303.15 mm | **303.19 mm** |
| Outside dia `da` | 307.19 mm | **307.23 mm** |
| Root dia `df` | 298.30 mm | **298.34 mm** |
| Center distance `a` | 165.58 mm | **163.57 mm** |
| Lead angle `λ` | ≈ 4.9° | **≈ 4.8°** |

## Usage

```bash
cd worm_crown
python3 calculate_crown.py            # JSON results → output/
python3 generate_drawing.py           # PDF + SVG + PNG → drawings/
```

### Entry data (mating worm)

| Symbol | Value |
|--------|------:|
| `da1` major diameter | 28.00 mm |
| `df1` root diameter | 19.33 mm |
| `Px` axial pitch | 6.35 mm |
| `z1` starts | 1 |
| `z2` wheel teeth | 150 |
| Pressure angle | 20° |

Blank features (bore Ø60 H7, hub Ø120, face 35 mm, CuSn12) are unchanged.

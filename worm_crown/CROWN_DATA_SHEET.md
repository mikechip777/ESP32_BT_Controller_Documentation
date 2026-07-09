# Crown (Worm Wheel) — Filled Data Sheet

Drawing: **WW-150T-2.0-01 Rev B**  
Source: mating worm as entry data · Wheel teeth **z₂ = 150**

---

## 1. Mating worm (entry / given)

| Parameter | Symbol | Value |
|-----------|--------|------:|
| Major diameter | *dₐ₁* | **28.00 mm** |
| Inner / root diameter | *dբ₁* | **19.33 mm** |
| Step (axial pitch) | *Pₓ* | **6.35 mm** |
| Starts | *z₁* | **1** (single-start, assumed) |
| Pressure angle | *α* | **20°** (standard) |

---

## 2. Worm (derived from entry)

| Parameter | Symbol | Formula | Value |
|-----------|--------|---------|------:|
| Module | *m* | *Pₓ* / π | **2.021 mm** |
| Pitch diameter | *d₁* | *dₐ₁* − 2*m* | **23.96 mm** |
| Addendum | *hₐ₁* | *m* | **2.02 mm** |
| Dedendum | *hբ₁* | (*d₁* − *dբ₁*)/2 | **2.31 mm** |
| Lead | *L* | *z₁* · *Pₓ* | **6.35 mm** |
| Lead angle | *λ* | arctan(*L* / (π·*d₁*)) | **≈ 4.8°** |
| Diameter quotient | *q* | *d₁* / *m* | **11.853** |

---

## 3. Crown / worm wheel (filled)

| Parameter | Symbol | Formula | Value |
|-----------|--------|---------|------:|
| Number of teeth | *z₂* | given | **150** |
| Module | *m* | *Pₓ* / π | **2.021 mm** |
| Axial pitch | *Pₓ* | = worm step | **6.350 mm** |
| Circular pitch | *p* | = *Pₓ* | **6.350 mm** |
| Pitch diameter | *d* | *m* · *z₂* | **303.19 mm** |
| Outside diameter | *dₐ* | *d* + 2*hₐ* | **307.23 mm** |
| Root diameter | *dբ* | *d* − 2*hբ* | **298.34 mm** |
| Addendum | *hₐ* | *m* | **2.02 mm** |
| Dedendum | *hբ* | 1.2 · *m* | **2.43 mm** |
| Whole depth | *h* | *hₐ* + *hբ* | **4.45 mm** |
| Tooth thickness (pitch circle) | *s* | *p* / 2 | **3.175 mm** |
| Center distance | *a* | (*d₁* + *d*) / 2 | **163.57 mm** |
| Reduction ratio | *i* | *z₂* / *z₁* | **150:1** |
| Worm lead | *L* | *z₁* · *Pₓ* | **6.35 mm** |
| Lead angle | *λ* | arctan(*L* / (π·*d₁*)) | **≈ 4.8°** |
| Pressure angle | *α* | standard | **20°** |

---

## 4. Recommended blank (before cutting teeth)

| Feature | Value |
|---------|------:|
| Outside diameter | **307.2 mm** |
| Face width | **35 mm** (+0.20 / 0) |
| Total width (with hub) | **65 mm** |
| Hub diameter | **Ø 120 mm** |
| Hub length | **30 mm** |
| Bore | **Ø 60 H7** (+0.03 / 0) |
| Keyway | **18 × 11 × 70 DIN 6885-1** (18 P9 × 11 P9) |
| Material | **Bronze / CuSn12** |

---

## 5. Key formulas used

```
m  = Px / π
d1 = da1 − 2·m          ← worm pitch diameter (not major diameter)
d  = m · z2
da = d + 2·m
df = d − 2·(1.2·m)
a  = (d1 + d) / 2       ← center distance
λ  = arctan(L / (π·d1))
```

**Note:** Center distance must use worm **pitch** diameter *d₁* (23.96 mm), not major diameter *dₐ₁* (28 mm). Using *dₐ₁* would incorrectly give *a* = 165.58 mm.

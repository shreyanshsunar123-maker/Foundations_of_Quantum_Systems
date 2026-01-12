# Importing Necessary Libraries.
from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
import argparse

import numpy as np
from scipy.special import genlaguerre, sph_harm as sph_harm_y
import math
import plotly.graph_objects as go


# -----------------------------
# Quantum Orbital Math: Radial Part
# -----------------------------
def radial_part(n: int, l: int, r: np.ndarray, a0: float) -> np.ndarray:
    if n<0:
        raise ValueError("Value should be n>0")
    if l<0 or l>=n:
        raise ValueError("value should be 0>=l<n")
    rho = 2*r/(n*a0)
    
    # The lageurre polynomial
    k = n - l - 1
    alpha = 2*l + 1
    Lpoly = genlaguerre(k, alpha)
    L = Lpoly(rho)
    
    # Normalizing the angular part
    norm = math.sqrt(
        (2/(n*a0))**3 * math.factorial(k) / (2*n*math.factorial(n+l))
    )

    return norm* np.exp(-rho/2.0) * (rho**l) * L


# -----------------------------
# Quantum Orbital Math: Angular Part
# -----------------------------
def Y_lm_complex(l: int, m: int, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    if l<0:
        raise ValueError("l should be > 0")
    if abs(m)>l:
        raise ValueError(" Require |m|<=l ")

    return sph_harm_y(m,l,theta,phi)

def Y_lm_real(l: int, name: str, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    nm = name.lower().strip()
    if l==1:
        Yp = sph_harm_y(1, 1, theta, phi) 
        Ym = sph_harm_y(-1,1,theta, phi)
            
        if nm == 'pz':
            return sph_harm_y(0,1,theta,phi)
        if nm == 'px':
            return (Ym - Yp)/np.sqrt(2.0)
        if nm == 'py':
            return (Ym + Yp)/(1j*np.sqrt(2.0))
        raise ValueError("For l = 1, use Px,Py,Pz")
        
    if l==2:
        Y0 = sph_harm_y(0,2,theta,phi)
        Y1 = sph_harm_y(1,2,theta,phi)
        Y1m = sph_harm_y(-1,2,theta,phi)
        Y2 = sph_harm_y(2,2,theta,phi)
        Y2m = sph_harm_y(-2,2,theta,phi)
        
        if nm in ('dz2', 'dz^2', 'dz.2'):
            return Y0
        if nm == "dxz":
            return (Y1m-Y1)/np.sqrt(2.0)
        if nm == "dyz":
            return (Y1m+Y1)/(1J*np.sqrt(2.0))
        if nm in ('dx^2-y^2', 'dx2-y2', 'dx^2y^2'):
            return (Y2+Y2m)/np.sqrt(2.0)
        if nm == "dxy":
            return (Y2m-Y2)/np.sqrt(2.0)
        raise ValueError("Use value dz^2,dxy,dyz,dxz,dx^2-y^2")
    

# -----------------------------
# Dataclass Structure for Sampled Points
# -----------------------------
@dataclass
class structure:
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    theta: np.ndarray
    phi: np.ndarray
    r: np.ndarray
    

# -----------------------------
# Sampling Uniform Random Points in 3D Space (Spherical Coordinates)
# -----------------------------
def sample_uniform_inspace(r_max:float, N:int, rng:np.random.Generator) -> structure:
    a = rng.random(N)
    b = rng.random(N)
    c = rng.random(N)
    
    r = r_max*(a**(1/3))
    theta = 2.0 * np.pi * b
    phi = np.arccos(1-(2*c))

    sinphi = np.sin(phi)
    x = r * np.cos(theta) * sinphi
    y = r * np.sin(theta) * sinphi
    z = r * np.cos(phi)

    return structure(x=x, y=y, z=z, theta=theta, phi=phi, r=r)



# -----------------------------
# Constructing the Orbital Cloud Using Weighted Sampling
# -----------------------------
def orbital_cloud (
    n:int,
    l:int,
    m:int,
    *,
    orbital: Optional[str]=None,
    points: int=500000,
    candidates: Optional[int]=None,
    a0: float=1.0,
    r_max: Optional[float]=None,
    seed: Optional[int]=None
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    
    if l<0 or l>=n:
        raise ValueError(" Require Value 0≤l<n ")
    if abs(m)>l:
        raise ValueError(" Require value |m|≤l ")
    
    rng = np.random.default_rng(seed)

    if r_max is None:
        r_max = 8.0 * (n**2) * a0

    if candidates is None:
        candidates = max(points*10,1000000)
    
    S = sample_uniform_inspace(r_max, candidates, rng)

    R = radial_part(n, l, S.r, a0=a0)

    if orbital is not None:
        Y = Y_lm_real(l, orbital, S.theta, S.phi)
        title_tag = f"{orbital.lower()},"
    else:
        Y = Y_lm_complex(l, m, S.theta, S.phi)
        title_tag = f"l={l}, m={m}"
    
    psi = R * Y
    w = np.abs(psi)**2

    w_sum = float(np.sum(w))
    if not np.isfinite(w_sum) or w_sum <=0:
        raise RuntimeError("Non-finite or zero total weight, check n,l and m parameters")
    
    p = w/w_sum
    idx = rng.choice(len(p), size=points, replace=True, p=p)

    X = S.x[idx]
    Y = S.y[idx]
    Z = S.z[idx]
    W = w[idx]

    return X, Y, Z, W


# -----------------------------
# Plotting the 3D Orbital Structure with Plotly
# -----------------------------
def plot_orbital(
    x:np.ndarray,
    y:np.ndarray,
    z:np.ndarray,
    w:np.ndarray,
    *,
    title:str
):
    fig = go.Figure(
        data=go.Scatter3d(
            x=x, y=y, z=z,
            mode="markers",
            marker=dict(
                size=2,
                color=w,
                colorscale='plasma',
                opacity=0.1,
                showscale=True,
                colorbar=dict(title="|ψ|^2")
            )
        )
    )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=24, color='white'), x=0.5),
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='black',
          aspectmode='cube', # Prevents "squishing"
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5) # Better starting angle
            )
        ),
        paper_bgcolor='black',
        margin=dict(l=0, r=0, b=0, t=40)
    )

    fig.show()


# -----------------------------
# Command Line Interface via Argparse
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Hydrogen Orbital Cloud Visualizer")
    parser.add_argument("--n", type=int, default=2)
    parser.add_argument("--l", type=int, default=1)
    parser.add_argument("--m", type=int, default=0)
    parser.add_argument("--orbital", type=str, default=None,
                        help="Real orbital name recommended"
                            "l=1: pz, px, py; l=2: dz2, dxz, dyz, dx2y2, dxy")
    parser.add_argument("--candidates", type=int, default=1000000)
    parser.add_argument("--points", type=int, default=500000)
    parser.add_argument("--a0", type=float, default=1.0)
    parser.add_argument("--rmax", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)

    args = parser.parse_args()
    
    if args.orbital is None and args.n == 2 and args.l == 1:
        for orb in ("px", "pz", "py"):
            x, y, z, w = orbital_cloud(
                n=2, l=args.l, m=args.m,
                orbital=orb,
                points=args.points,
                candidates=args.candidates,
                a0=args.a0,
                r_max=args.rmax,
                seed=args.seed
            )
            plot_orbital(
                x, y, z, w,
                title=f"Hydrogen Orbital Cloud (n=2, {orb})"
            )
    else:
        x, y, z, w = orbital_cloud(
            n=args.n,
            l=args.l,
            m=args.m,
            orbital=args.orbital,
            points=args.points,
            candidates=args.candidates,
            a0=args.a0,
            r_max=args.rmax,
            seed=args.seed,
        )

        tag = args.orbital.lower() if args.orbital else f"l={args.l}, m={args.m}"

        plot_orbital(
            x, y, z, w,
            title=f"Hydrogen Orbital Cloud (n={args.n}, {tag})"
        )


# -----------------------------
# Script Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

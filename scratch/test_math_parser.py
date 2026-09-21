#!/usr/bin/env python3
import re

def render_formula(raw):
    f = raw.strip()

    # Double-bar norm \| or \lVert / \rVert
    f = f.replace(r"\|", "‖").replace(r"\lVert", "‖").replace(r"\rVert", "‖")

    # Greek letters
    greek = {
        r"\alpha": "α", r"\beta": "β", r"\gamma": "γ", r"\delta": "δ", r"\Delta": "Δ",
        r"\epsilon": "ε", r"\zeta": "ζ", r"\eta": "η", r"\theta": "θ", r"\Theta": "Θ",
        r"\kappa": "κ", r"\lambda": "λ", r"\Lambda": "Λ", r"\mu": "μ", r"\nu": "ν", r"\xi": "ξ",
        r"\pi": "π", r"\Pi": "Π", r"\rho": "ρ", r"\sigma": "σ", r"\Sigma": "Σ",
        r"\tau": "τ", r"\phi": "φ", r"\Phi": "Φ", r"\chi": "χ", r"\psi": "ψ",
        r"\omega": "ω", r"\Omega": "Ω"
    }
    for k, v in greek.items():
        f = f.replace(k, v)

    # Bold vectors / matrices: \mathbf{v}, \mathbf{u}, \mathbf{x}
    f = re.sub(r"\\mathbf\s*\{([^{}]+)\}", r'<strong class="math-bf">\1</strong>', f)
    f = re.sub(r"\\mathbf\s+([a-zA-Z0-9])", r'<strong class="math-bf">\1</strong>', f)

    # Hat unit vectors: \hat{i}, \hat{j}, \hat{v}, \hat{\mathbf{x}}
    f = re.sub(r"\\hat\s*\{<strong class=\"math-bf\">([^{}]+)</strong>\}", r'<strong class="math-bf">\1̂</strong>', f)
    f = re.sub(r"\\hat\s*\{([^{}]+)\}", r"\1̂", f)
    f = re.sub(r"\\hat\s+([a-zA-Z0-9])", r"\1̂", f)

    # Dots & ellipsis: \dots, \cdots, \ldots, \vdots, \ddots
    f = re.sub(r"\\(dots|cdots|ldots)", "…", f)
    f = f.replace(r"\vdots", "⋮").replace(r"\ddots", "⋱")

    # Functions
    ops = ["cos", "sin", "tan", "det", "dim", "ker", "ln", "log", "exp", "max", "min", "lim", "proj", "span", "rank", "tr", "diag"]
    for op in ops:
        f = re.sub(r"\\" + op + r"(?![a-zA-Z])", f'<span class="math-op">{op}</span>', f)

    # Symbols
    symbols = {
        r"\sum": "∑", r"\int": "∫", r"\prod": "∏",
        r"\le": "≤", r"\leq": "≤", r"\ge": "≥", r"\geq": "≥",
        r"\neq": "≠", r"\ne": "≠", r"\approx": "≈", r"\sim": "∼",
        r"\implies": "⟹", r"\iff": "⟺",
        r"\to": "→", r"\rightarrow": "→", r"\leftarrow": "←", r"\leftrightarrow": "↔",
        r"\infty": "∞", r"\cdot": "·", r"\times": "×", r"\pm": "±",
        r"\in": "∈", r"\subset": "⊂", r"\subseteq": "⊆",
        r"\perp": "⟂", r"\angle": "∠", r"\circ": "°",
        r"\langle": "⟨", r"\rangle": "⟩", r"\nabla": "∇", r"\partial": "∂",
        r"\mathbb{R}": "ℝ", r"\mathbb{Z}": "ℤ", r"\mathbb{C}": "ℂ", r"\mathbb{N}": "ℕ",
        r"\mathcal{Z}": "𝒵", r"\mathcal{F}": "ℱ",
        r"\circledast": "⊛", r"\ast": "*",
        r"\top": "T",
        r"\text": "", r"\mathrm": "", r"\operatorname": "", r"\textbf": "",
        r"\left": "", r"\right": ""
    }
    for k, v in symbols.items():
        f = f.replace(k, v)

    # Fractions: \frac{A}{B}
    f = re.sub(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}", r'<span class="math-frac"><span class="math-num">\1</span><span class="math-den">\2</span></span>', f)

    # Square root: \sqrt{A}
    f = re.sub(r"\\sqrt\s*\{([^{}]+)\}", r'√<span class="math-sqrt">\1</span>', f)

    # Subscripts & Superscripts
    f = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", f)
    f = re.sub(r"_([a-zA-Z0-9])", r"<sub>\1</sub>", f)
    f = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", f)
    f = re.sub(r"\^([a-zA-Z0-9\+\-T])", r"<sup>\1</sup>", f)

    f = re.sub(r"[{}]", "", f)
    return f

if __name__ == "__main__":
    test1 = r"\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \dots + u_n v_n = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)"
    test2 = r"\hat{i} = [1, 0], \hat{j} = [0, 1]"
    test3 = r"\operatorname{proj}_{\mathbf{a}}(\mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|^2} \mathbf{a}"
    test4 = r"A \mathbf{v} = \lambda \mathbf{v}"
    test5 = r"\det(A - \lambda I) = 0"

    print("Test 1:", render_formula(test1))
    print("Test 2:", render_formula(test2))
    print("Test 3:", render_formula(test3))
    print("Test 4:", render_formula(test4))
    print("Test 5:", render_formula(test5))

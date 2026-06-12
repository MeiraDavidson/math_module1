"""Generate the five companion notebooks for Book 1.

Each notebook is short (one concept), self-contained, runs top-to-bottom with no
setup beyond standard Colab libraries. Markdown cells carry the teaching; code
stays readable. Predict-first notebooks have explicit "predict before you run"
prompts.
"""
import os
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "MeiraDavidson/math_module1"   # placeholder GitHub repo


def badge(path):
    url = f"https://colab.research.google.com/github/{REPO}/blob/main/{path}"
    return (f"[![Open In Colab](https://colab.research.google.com/assets/"
            f"colab-badge.svg)]({url})")


def write(nb, name):
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3"},
        "colab": {"provenance": []},
    }
    path = os.path.join(HERE, name)
    with open(path, "w") as f:
        nbf.write(nb, f)
    print("wrote", name)


# =====================================================================
# Notebook 2.1 — "The number your computer can't hold"  [WALKTHROUGH]
# =====================================================================
def nb_2_1():
    c = []
    c.append(new_markdown_cell(
f"""# The number your computer can't hold
### Chapter 2 · finite precision · **[WALKTHROUGH]**

{badge('notebook_2_1_finite_precision.ipynb')}

**What you'll see:** your own computer insist that `0.1 + 0.2` is *not* `0.3` — and
then watch it run out of room while trying to hold π and ⅓. Reading about this is a
curiosity. Watching your *own machine* do it is unforgettable.

Run the cells in order. No libraries, no setup — just press play."""))

    c.append(new_markdown_cell(
"""## 1. The one-line detonation

Here is the whole shock in a single line. Run it."""))
    c.append(new_code_cell("0.1 + 0.2"))

    c.append(new_markdown_cell(
"""That trailing `...0004` should not be there. In real arithmetic, $0.1+0.2$ is
*exactly* $0.3$. So let's ask the computer the question directly:"""))
    c.append(new_code_cell("0.1 + 0.2 == 0.3"))

    c.append(new_markdown_cell(
"""**`False`.** The computer is telling you, to your face, that it does not believe
$0.1+0.2$ equals $0.3$.

It isn't broken. Remember from the chapter: $0.1$ written in *binary* (the
computer's native twos) is a **repeating** decimal — it never ends. So the machine
can't store $0.1$ exactly, or $0.2$ exactly. It rounds each one to the nearest dot
it can hold, and the two tiny roundings don't quite cancel. A speck of error, left
over, made visible."""))

    c.append(new_markdown_cell(
"""## 2. Watch π run out of room

Let's print π two ways and see *exactly* where the computer stops. The first line
is the value your machine actually stores. The second is the true value of π,
copied from someone who computed it the careful way."""))
    c.append(new_code_cell(
"""import math

stored = f"{math.pi:.48f}"            # what your computer holds, to 48 decimals
true_pi = "3.141592653589793238462643383279502884197169399375"

print("computer stores: ", stored)
print("true value of π: ", true_pi)
print()
# find the first place where they disagree
for i, (a, b) in enumerate(zip(stored, true_pi)):
    if a != b:
        print(f"They agree for {i-2} digits after the dot, then the stored value")
        print("turns to noise — that's where the computer's 'boxes' ran out.")
        break"""))

    c.append(new_markdown_cell(
"""The stored value tracks π for about **15–16 digits**, and then everything past
that is garbage the machine invented to fill the decimals you asked for. It only
ever had room for a sketch."""))

    c.append(new_markdown_cell(
"""## 3. Even ⅓ loses its tail

It's not just the irrationals. The humble fraction $\\tfrac13 = 0.3333\\ldots$ never
ends either, so the computer can't hold it whole:"""))
    c.append(new_code_cell(
'''print(f"1/3 = {1/3:.30f}")
print("...the 3's were supposed to go on forever. They stop because the boxes did.")'''))

    c.append(new_markdown_cell(
"""## What just happened

> **Our number line is perfect and infinite. The computer's number line is a finite
> grid of dots.** Most real numbers — π, ⅓, even plain $0.1$ — fall *between* the
> dots, so the computer quietly snaps each one to the nearest dot it can hold. It
> isn't lying to you. It's working with a very good **sketch** of the real numbers,
> never the real thing.

The careful, infinite reasoning you're learning in the book isn't the clumsy
version of what a computer does — it's the **exact** version the machine spends all
its effort trying to imitate.

**Try this:** change `0.1 + 0.2` to `0.5 + 0.25` and run it. Why does *that* one come
out exactly right? (Hint: what are $0.5$ and $0.25$ in binary — do *they* end?)"""))
    nb = new_notebook(cells=c)
    write(nb, "notebook_2_1_finite_precision.ipynb")


# =====================================================================
# Notebook 5.1 — "Growth, decay, and the curve that decides" [PREDICT-FIRST]
# =====================================================================
def nb_5_1():
    c = []
    c.append(new_markdown_cell(
f"""# Growth, decay, and the curve that decides
### Chapter 5 · exponentials, the S-curve, the sigmoid · **[PREDICT-FIRST]**

{badge('notebook_5_1_growth_decay_sigmoid.ipynb')}

**What you'll see:** drag the base of $b^x$ and watch growth *flip* into decay; race
a runaway exponential against the S-curve that bends to a ceiling; and meet the
**sigmoid**, the decision curve of an artificial neuron.

This is a **predict-first** notebook. Each time you see 🔮, *say your guess out loud
before you run the cell.* Guessing then checking is how the parameter gets into your
bones."""))
    c.append(new_code_cell(
"""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider"""))

    c.append(new_markdown_cell(
"""## 1. One knob flips growth into decay

🔮 **Predict first:** the slider sets the base $b$ in $b^{\\,x}$. Right now it starts
above 1. *Before you slide $b$ below 1, predict which way the curve will tilt.* Will
it still rise to the right, or fall?"""))
    c.append(new_code_cell(
'''def show_base(b=2.0):
    x = np.linspace(-4, 4, 400)
    plt.figure(figsize=(7, 4))
    plt.plot(x, b**x, color="#1A6FB0", lw=2.5)
    plt.axhline(0, color="#999", lw=0.8)
    plt.axvline(0, color="#999", lw=0.8)
    plt.title(f"$b^x$  with  b = {b:.2f}   " +
              ("(growth)" if b > 1 else "(decay)" if b < 1 else "(flat)"))
    plt.ylim(-1, 16); plt.xlabel("x"); plt.show()

interact(show_base, b=FloatSlider(min=0.3, max=3.0, step=0.05, value=2.0));'''))
    c.append(new_markdown_cell(
"""Did it match your guess? At exactly $b=1$ the curve goes **flat** — every power of
1 is 1. Above 1 it grows; below 1 it decays. *Same machine, base flipped.*"""))

    c.append(new_markdown_cell(
"""## 2. The exponential's lie: nothing grows forever

A pure exponential (dashed) shoots to infinity. But in any *finite* world — a
population, a market, an epidemic — growth runs out of room and bends into an
**S-curve** (solid) that levels off at a ceiling.

🔮 **Predict first:** the slider raises the **ceiling**. Before you drag it up,
predict: does raising the ceiling change where the two curves *start* (on the left),
or only where the S-curve ends up (on the right)?"""))
    c.append(new_code_cell(
'''def show_scurve(ceiling=10.0):
    x = np.linspace(0, 10, 400)
    pure = 0.4 * np.exp(0.7 * x)                 # the runaway "model"
    logistic = ceiling / (1 + np.exp(-1.1*(x-5)))  # the "reality"
    plt.figure(figsize=(7, 4))
    plt.plot(x, np.minimum(pure, ceiling*1.6), "--", color="#999", lw=2, label="pure exponential (the model)")
    plt.plot(x, logistic, color="#1A6FB0", lw=2.6, label="S-curve (reality)")
    plt.axhline(ceiling, color="#E8833A", ls=":", lw=1.6, label="ceiling")
    plt.legend(); plt.xlabel("time"); plt.title("The ceiling always bites"); plt.show()

interact(show_scurve, ceiling=FloatSlider(min=4, max=16, step=1, value=10));'''))
    c.append(new_markdown_cell(
"""The two curves **start out identical** — the early, dangerous phase nobody sees
coming looks exactly exponential. They only part ways once the ceiling starts to
bite. *The real question is never \"how fast does it grow?\" but \"where is the
ceiling, and when?\"*"""))

    c.append(new_markdown_cell(
"""## 3. The sigmoid: a curve that decides

Build this little machine from the decay $e^{-x}$:
$$\\sigma(x) = \\frac{1}{1 + e^{-x}}$$

🔮 **Predict first — before you run the next cell, guess all three:**
- $\\sigma(0) = ?$
- $\\sigma(\\text{a big positive number}) \\to ?$
- $\\sigma(\\text{a big negative number}) \\to ?$

Write your three guesses down, *then* run it."""))
    c.append(new_code_cell(
'''def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-8, 8, 400)
plt.figure(figsize=(7, 4))
plt.plot(x, sigmoid(x), color="#1A6FB0", lw=2.6)
plt.axhline(0, color="#999", ls="--", lw=1); plt.axhline(1, color="#999", ls="--", lw=1)
plt.axhline(0.5, color="#E8833A", ls=":", lw=1.2)
plt.title(r"$\\sigma(x) = 1/(1+e^{-x})$"); plt.xlabel("x"); plt.show()

print("σ(0)      =", round(sigmoid(0), 4), "  <- exactly one half: 'unsure'")
print("σ(10)     =", round(sigmoid(10), 6), " <- basically 1: 'yes'")
print("σ(-10)    =", round(sigmoid(-10), 6), " <- basically 0: 'no'")'''))
    c.append(new_markdown_cell(
"""## What just happened

The sigmoid takes **any** input on the whole number line — from minus infinity to
plus infinity — and gently squashes it into the range between $0$ and $1$, passing
through $\\tfrac12$ at the center. That's exactly how an artificial neuron *decides*:
it turns a runaway input of any size into a bounded answer between $0$ (no) and $1$
(yes), with $\\tfrac12$ as "unsure."

The curve that tames an epidemic and the curve that lets a neural network make up
its mind are the **same curve** — and you just built it from $e^{-x}$, a reciprocal,
and a $+1$. Everything in the modern machine is made of pieces you already have."""))
    nb = new_notebook(cells=c)
    write(nb, "notebook_5_1_growth_decay_sigmoid.ipynb")


# =====================================================================
# Notebook 7.1 — "Iteration: solving what you can't solve directly" [PREDICT-FIRST]
# =====================================================================
def nb_7_1():
    c = []
    c.append(new_markdown_cell(
f"""# Iteration: solving what you can't solve directly
### Chapter 7 · iteration & convergence · **[PREDICT-FIRST]**

{badge('notebook_7_1_iteration_sqrt2.ipynb')}

**What you'll see:** three machines fed their own output, over and over. One crawls to
zero, one runs off to infinity — and one performs a small miracle: no matter where
you start, it always finds $\\sqrt2$. By the end you'll have built a square-root
algorithm with four lines of code.

**Predict-first:** when you see 🔮, guess before you run."""))
    c.append(new_code_cell(
"""import numpy as np
import matplotlib.pyplot as plt

def iterate(machine, start, steps):
    \"\"\"Feed a machine its own output, `steps` times, recording the path.\"\"\"
    x = start
    path = [x]
    for _ in range(steps):
        x = machine(x)
        path.append(x)
    return path"""))

    c.append(new_markdown_cell(
"""## 1. Two simple machines: one settles, one escapes

Iterating **"halve it"** from 32, and **"add 3"** from 0. Watch the long-run
behavior — that's the whole point of iteration."""))
    c.append(new_code_cell(
'''halve = lambda x: x / 2
add3  = lambda x: x + 3

print("halve, from 32:", [round(v, 4) for v in iterate(halve, 32, 8)])
print("add 3, from 0: ", iterate(add3, 0, 8))'''))
    c.append(new_markdown_cell(
"""Halving **crawls toward 0** and never quite arrives — we call $0$ an *attractor*.
Adding 3 just **runs off** forever. Same idea (feed the output back in), opposite
fates — decided entirely by the machine."""))

    c.append(new_markdown_cell(
"""## 2. The √2-finder — a real miracle

Here is the machine: take the average of $x$ and $\\tfrac{2}{x}$,
$$f(x) = \\tfrac12\\left(x + \\tfrac{2}{x}\\right).$$

🔮 **Predict first:** type *any* positive starting number you like into `start`
below — 1, or 100, or 0.01, your choice. **Predict where it ends up before you run
it.** Will different starts land in different places?"""))
    c.append(new_code_cell(
'''sqrt2_finder = lambda x: 0.5 * (x + 2/x)

start = 100.0       # <-- change me to ANY positive number you like
path = iterate(sqrt2_finder, start, 6)

print(f"starting from {start}:")
for i, v in enumerate(path):
    print(f"  step {i}:  {v:.12f}")
print(f"\\n  √2 (the truth): {np.sqrt(2):.12f}")'''))
    c.append(new_markdown_cell(
"""However wild your starting number, the machine **homes in on $\\sqrt2$ in just a
handful of steps.** Let's watch it converge:"""))
    c.append(new_code_cell(
'''for s in [1, 5, 50, 0.1]:
    path = iterate(sqrt2_finder, s, 6)
    plt.plot(range(len(path)), path, "o-", label=f"start = {s}")
plt.axhline(np.sqrt(2), color="#E8833A", ls="--", label="√2")
plt.ylim(0, 6); plt.xlabel("step"); plt.ylabel("value")
plt.title("Every start lands on √2"); plt.legend(); plt.show()'''))

    c.append(new_markdown_cell(
"""## 3. You just built a square-root algorithm

Swap the `2` for any number `N` and the same machine finds $\\sqrt N$. Try it:"""))
    c.append(new_code_cell(
'''def root_finder(N):
    machine = lambda x: 0.5 * (x + N/x)
    return iterate(machine, 1.0, 8)[-1]

for N in [9, 2, 1000, 7]:
    print(f"my machine says √{N} = {root_finder(N):.10f}   (numpy: {np.sqrt(N):.10f})")'''))
    c.append(new_markdown_cell(
"""## What just happened

> **Iteration is how you *solve* things you can't solve directly.** You can't write
> $\\sqrt2$ as a fraction — but you can write a simple machine whose repeated
> application *converges* to it, as close as you like.

Typing *any* start and always landing on $\\sqrt2$ is an experiment, not a fact — it
had to be played with. And this is no toy: it's a 2000-year-old method, the ancestor
of **Newton's method** (calculus) and **gradient descent** — the algorithm that
trains every neural network. The training of every AI you've ever used is one
machine, iterated. You just ran the seed of it."""))
    nb = new_notebook(cells=c)
    write(nb, "notebook_7_1_iteration_sqrt2.ipynb")


# =====================================================================
# Notebook 7.2 — "Order into chaos: the logistic map"  [PREDICT-FIRST]  (flagship)
# =====================================================================
def nb_7_2():
    c = []
    c.append(new_markdown_cell(
f"""# Order into chaos: the logistic map
### Chapter 7 · chaos, bifurcation, the butterfly effect · **[PREDICT-FIRST]**

{badge('notebook_7_2_logistic_map_chaos.ipynb')}

**What you'll see:** the most important notebook in this book. One absurdly simple
rule — $f(x) = r\\,x\\,(1-x)$ — fed its own output. Turn a single knob $r$ and watch a
calm, settled system **split, split again, and dissolve into chaos**. Then generate
the famous bifurcation diagram, and finally watch two nearly-identical starts explode
into different futures: the **butterfly effect**.

**Predict-first.** Do the experiment *before* you read the meaning at the bottom."""))
    c.append(new_code_cell(
"""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def logistic_path(r, x0, n):
    x = x0
    path = [x]
    for _ in range(n):
        x = r * x * (1 - x)
        path.append(x)
    return path"""))

    c.append(new_markdown_cell(
"""## 1. Turn the knob

🔮 **Predict first:** at $r=2$, predict whether the population *settles* to one value.
Then raise $r$ past $3$ and predict what "settling" *becomes* — does it stay one
value, or do something new? Drag the slider slowly and watch the time series."""))
    c.append(new_code_cell(
'''def show_timeseries(r=2.0):
    path = logistic_path(r, 0.3, 50)
    plt.figure(figsize=(8, 3.5))
    plt.plot(path, "o-", color="#1A6FB0", ms=4, lw=1.2)
    plt.ylim(0, 1); plt.xlabel("year"); plt.ylabel("population")
    plt.title(f"r = {r:.2f}"); plt.show()

interact(show_timeseries, r=FloatSlider(min=1.0, max=4.0, step=0.01, value=2.0));'''))
    c.append(new_markdown_cell(
"""Watch the journey as you raise $r$: **settles** → **2-cycle** (bounces between two
values) → **4-cycle** → and past about $r=3.57$, **chaos** — jumping around forever
with no pattern, even though the rule is utterly fixed and simple."""))

    c.append(new_markdown_cell(
"""## 2. The bifurcation diagram (the iconic image)

For each value of $r$, throw away the first few hundred steps (the transient) and
plot the values it *settles into*. This single picture shows the whole
period-doubling cascade at once — the famous "fig tree."

*(This takes a couple of seconds to compute — it's iterating thousands of times.)*"""))
    c.append(new_code_cell(
'''rs = np.linspace(2.5, 4.0, 2000)
R, X = [], []
for r in rs:
    x = 0.5
    for _ in range(300):          # let transients die out
        x = r * x * (1 - x)
    for _ in range(120):          # record the attractor
        x = r * x * (1 - x)
        R.append(r); X.append(x)

plt.figure(figsize=(9, 5))
plt.plot(R, X, ",", color="#1A6FB0", alpha=0.25)
plt.title("Bifurcation diagram: the road from order to chaos")
plt.xlabel("r"); plt.ylabel("long-run population")
plt.axvline(3.57, color="#999", ls=":"); plt.show()'''))
    c.append(new_markdown_cell(
"""One line splits to two, to four, to eight — faster and faster — then shatters into
the chaotic spray. The white gaps inside the chaos are "windows" where order briefly
returns. **This image is impossible to draw by hand and unforgettable on a screen.**
Zoom in by changing `rs = np.linspace(3.4, 4.0, 2000)` and run again."""))

    c.append(new_markdown_cell(
"""## 3. The butterfly effect

🔮 **Predict first:** two runs at $r=3.9$, starting a hair apart — $0.300$ and
$0.301$. **Predict whether starting a hair apart matters.** Will they stay together,
or drift?"""))
    c.append(new_code_cell(
'''a = logistic_path(3.9, 0.300, 45)
b = logistic_path(3.9, 0.301, 45)
plt.figure(figsize=(9, 3.8))
plt.plot(a, "-", color="#1A6FB0", lw=1.6, label="start 0.300")
plt.plot(b, "-", color="#E8833A", lw=1.6, label="start 0.301")
plt.xlabel("year"); plt.ylabel("population"); plt.legend()
plt.title("A hair apart — then worlds apart"); plt.show()'''))
    c.append(new_markdown_cell(
"""They track almost perfectly for a while... and then, around step 10–15, they
**explode apart** and have nothing to do with each other. A difference of $0.001$ —
invisible — became total disagreement. That's why weather can't be forecast far
ahead: not because the rules are unknown, but because they're *chaotic*."""))

    c.append(new_markdown_cell(
"""## Why this matters (read it now, after you've played)

Look at the *shape* of what happened. As you slowly turned one knob, the system held
steady, held steady — and then, at a sharp threshold, **abruptly reorganized** into
something qualitatively new. Calm, then suddenly a 2-cycle. Order, then suddenly
chaos.

That pattern — *a smooth change in a setting producing a sudden jump in behavior* —
is called a **phase transition**, and once you have eyes for it you see it
everywhere: water cooling degree by degree and then, at one temperature, abruptly
freezing; and — this is the live frontier — an artificial intelligence that is
trained and trained showing no sign of a skill, and then, rather suddenly,
*acquiring* it.

You just watched a simple rule reorganize itself all at once. Many researchers
suspect this is the shape of how AI models suddenly acquire new abilities as they
grow. Nobody fully understands it yet — and a kid iterating $r\\,x(1-x)$ is touching
the same mathematics."""))
    nb = new_notebook(cells=c)
    write(nb, "notebook_7_2_logistic_map_chaos.ipynb")


# =====================================================================
# Notebook 8.1 — "Multiplication is rotation; roots of unity" [PREDICT-FIRST]
# =====================================================================
def nb_8_1():
    c = []
    c.append(new_markdown_cell(
f"""# Multiplication is rotation; roots of unity on the circle
### Chapter 8 · the complex plane, rotation, roots of unity · **[PREDICT-FIRST]**

{badge('notebook_8_1_complex_rotation_roots.ipynb')}

**What you'll see:** complex numbers as *arrows* in a plane — and watch multiplication
literally **turn** them (distances multiply, angles add, exactly as you proved on
paper). Then watch the $n$-th roots of unity snap into the corners of a perfect
$n$-sided polygon.

**Predict-first:** guess before you run each 🔮 cell."""))
    c.append(new_code_cell(
"""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider

def draw_arrow(ax, z, color, label=None):
    ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2))
    if label:
        ax.text(z.real*1.07, z.imag*1.07, label, color=color, fontsize=12)"""))

    c.append(new_markdown_cell(
"""## 1. Multiplication turns the arrow

We'll multiply a fixed number $z = 2 + i$ by a second number you control with
sliders: its **distance** from the origin and its **angle**.

🔮 **Predict first:** set the second number's angle to **90°** and its distance to
**1**. *Before you run it*, predict where the product's arrow will point — and whether
it will be longer, shorter, or the same length as the original."""))
    c.append(new_code_cell(
'''def multiply_demo(distance=1.0, angle_deg=90.0):
    z = 2 + 1j                                   # the fixed arrow
    theta = np.radians(angle_deg)
    w = distance * (np.cos(theta) + 1j*np.sin(theta))  # the arrow you control
    product = z * w

    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    draw_arrow(ax, z, "#999", "z = 2+i")
    draw_arrow(ax, product, "#1A6FB0", "z × w")
    lim = 4
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_aspect("equal")
    ax.axhline(0, color="#ccc", lw=0.8); ax.axvline(0, color="#ccc", lw=0.8)
    ax.set_title(f"multiply by w: distance {distance:.1f}, angle {angle_deg:.0f}°")
    plt.show()
    print(f"original distance {abs(z):.2f}, angle {np.degrees(np.angle(z)):.0f}°")
    print(f"product  distance {abs(product):.2f}, angle {np.degrees(np.angle(product)):.0f}°")

interact(multiply_demo,
         distance=FloatSlider(min=0.3, max=2.0, step=0.1, value=1.0),
         angle_deg=FloatSlider(min=0, max=360, step=15, value=90));'''))
    c.append(new_markdown_cell(
"""Read the two printed lines: when you multiply, the **distances multiply** and the
**angles add** — exactly the rule you proved. Multiplying by something at angle 90°
and distance 1 is a pure **quarter-turn**, no stretching. *Multiplication and turning
are the same act.*"""))

    c.append(new_markdown_cell(
"""## 2. The roots of unity form a polygon

The $n$-th **roots of unity** are the $n$ solutions of $x^n = 1$. On paper you found
they sit at evenly spaced angles $\\tfrac{2\\pi k}{n}$ around the unit circle.

🔮 **Predict first:** before you set $n = 6$, predict **how many points** you'll see
and **what shape** they'll make."""))
    c.append(new_code_cell(
'''def roots_of_unity(n=3):
    k = np.arange(n)
    roots = np.exp(2j * np.pi * k / n)           # the n-th roots of 1

    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    circle = np.exp(1j * np.linspace(0, 2*np.pi, 300))
    ax.plot(circle.real, circle.imag, color="#ccc", lw=1)
    # connect them into a polygon
    poly = np.append(roots, roots[0])
    ax.plot(poly.real, poly.imag, color="#1A6FB0", lw=1.8)
    ax.plot(roots.real, roots.imag, "o", color="#1A6FB0", ms=10)
    ax.plot([1], [0], "o", color="#E8833A", ms=11)   # the ordinary real root x=1
    ax.text(1.08, 0.05, "x = 1", color="#E8833A")
    ax.set_aspect("equal"); ax.set_xlim(-1.4, 1.5); ax.set_ylim(-1.4, 1.4)
    ax.axhline(0, color="#eee", lw=0.8); ax.axvline(0, color="#eee", lw=0.8)
    ax.set_title(f"the {n} roots of unity")
    plt.show()
    for r in roots:
        print(f"  angle {np.degrees(np.angle(r)) % 360:6.1f}°   ->   {r.real:+.3f} {r.imag:+.3f}i")

interact(roots_of_unity, n=IntSlider(min=2, max=12, step=1, value=3));'''))
    c.append(new_markdown_cell(
"""## What just happened

You *proved* on paper that "multiplication adds angles" and that "the roots of unity
form a regular polygon." Here you watched the arrows **actually rotate** and the
polygon **actually form** — and you could test values of $n$ you'd never compute by
hand.

For any $n$, the roots are the $n$ corners of a regular $n$-gon on the unit circle,
with one corner always sitting on the ordinary real root $x=1$. Chapter 4's promise —
that $x^n - 1$ factors into roots arranged on a circle — computed with your own
hands. The walker, the rotation, and the polygon were a complex number all along."""))
    nb = new_notebook(cells=c)
    write(nb, "notebook_8_1_complex_rotation_roots.ipynb")


for f in (nb_2_1, nb_5_1, nb_7_1, nb_7_2, nb_8_1):
    f()
print("All 5 notebooks generated.")

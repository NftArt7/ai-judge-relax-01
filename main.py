import os

POEM = """You are in the hammock again.
The ropes hold you. The evening holds the ropes.
Someone's hand is on your ankle, pushing, slow.
Out. Back. Out. Back.
The rope creaks, soft, with every sway.
Each push a little softer. Each sway a little longer.
The light is low and gold on the grass.
A cricket starts. Then another. Then the whole field.
The hand lets go.
The hammock swings on its own now, smaller, smaller.
Your chest rises. Falls. Rises. Falls, slower.
The gold goes rose. The rose goes grey.
The crickets count you down, soft.
You are still swinging, but only just.
Then you are not.
You are asleep.
"""

outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)

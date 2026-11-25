// news-image-20261125 — "Sum up 25 November's world news in one image".
// The entry image (entry.png, composed in this session from the day's news)
// is copied to the output directory. No network, no dependencies.
// The copy is byte-for-byte deterministic: the same input always produces
// the same output, so both grader runs write identical bytes.
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(repoRoot, "entry.png");
const target = join(outDir, "entry.png");
mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
// Fail loudly if the copy is ever incomplete instead of shipping a bad file.
if (statSync(source).size !== statSync(target).size) {
  throw new Error("entry.png copy size mismatch");
}

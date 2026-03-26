import path from "path";
import { pathToFileURL } from "url";
import os from "os";
import fs from "fs/promises";

const testDir = path.join(os.tmpdir(), "bun-import-test2");
await fs.rm(testDir, { recursive: true, force: true });
await fs.mkdir(testDir, { recursive: true });

console.log("Test dir:", testDir);

// Create a test file that imports an external package
await Bun.write(path.join(testDir, "test.ts"), `
import { say } from 'cowsay'
export default say({ text: "hello" })
`);

// Create package.json
await Bun.write(path.join(testDir, "package.json"), JSON.stringify({
  name: "test-pkg",
  dependencies: {
    "cowsay": "^1.6.0"
  }
}));

// Try to import it without installing dependencies
const match = path.join(testDir, "test.ts");
const url = pathToFileURL(match).href;
console.log("URL:", url);

try {
  const mod = await import(url);
  console.log("Success:", mod);
} catch (e) {
  console.error("Error:", e.message);
}

import path from "path";
import { pathToFileURL } from "url";
import os from "os";

const testDir = path.join(os.tmpdir(), "bun-import-test");
console.log("Test dir:", testDir);

// Create a test file
await Bun.write(path.join(testDir, "test.ts"), `
export default "hello from test file"
`);

// Try to import it
const match = path.join(testDir, "test.ts");
const url = pathToFileURL(match).href;
console.log("URL:", url);
console.log("CWD:", process.cwd());

try {
  const mod = await import(url);
  console.log("Success:", mod);
} catch (e) {
  console.error("Error:", e.message);
}

import { describe, test, expect } from "bun:test"
import path from "path"
import fs from "fs/promises"
import { tmpdir } from "./test/fixture/fixture"
import { Instance } from "./src/project/instance"
import { Config } from "./src/config/config"

test("debug: check directories", async () => {
  await using tmp = await tmpdir({
    init: async (dir) => {
      const cruxcliDir = path.join(dir, ".cruxcli")
      await fs.mkdir(cruxcliDir, { recursive: true })
      
      const toolsDir = path.join(cruxcliDir, "tools")
      await fs.mkdir(toolsDir, { recursive: true })
      
      await Bun.write(
        path.join(cruxcliDir, "package.json"),
        JSON.stringify({
          name: "custom-tools",
          dependencies: {
            "cowsay": "^1.6.0",
          },
        }),
      )
      
      console.log("Created .cruxcli in:", cruxcliDir)
    },
  })
  
  await Instance.provide({
    directory: tmp.path,
    fn: async () => {
      const dirs = await Config.directories()
      console.log("Config.directories():", dirs)
      
      const hasCruxcli = dirs.some(d => d.endsWith(".cruxcli") && d.startsWith(tmp.path))
      console.log("Has cruxcli in temp dir:", hasCruxcli)
      
      expect(hasCruxcli).toBe(true)
    },
  })
})

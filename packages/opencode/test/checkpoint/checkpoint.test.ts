import { describe, test, expect } from "bun:test"
import { Checkpoint } from "../../src/checkpoint"
import { tmpdir } from "../fixture/fixture"
import { Instance } from "../../src/project/instance"
import * as fs from "fs/promises"
import path from "path"

describe("checkpoint", () => {
  test("create and list", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        await fs.writeFile(path.join(tmp.path, "file.txt"), "hello")
        const cp = await Checkpoint.create("test-label")
        expect(cp).toBeDefined()
        expect(cp!.label).toBe("test-label")
        expect(cp!.hash).toBeTruthy()
        expect(cp!.auto).toBe(false)

        const items = await Checkpoint.list()
        expect(items.length).toBe(1)
        expect(items[0].id).toBe(cp!.id)
      },
    })
  })

  test("restore reverts changes", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        const file = path.join(tmp.path, "data.txt")
        await fs.writeFile(file, "before")
        const cp = await Checkpoint.create("before-change")
        expect(cp).toBeDefined()

        await fs.writeFile(file, "after")
        const content = await fs.readFile(file, "utf8")
        expect(content).toBe("after")

        const ok = await Checkpoint.restore(cp!.id)
        expect(ok).toBe(true)
        const restored = await fs.readFile(file, "utf8")
        expect(restored).toBe("before")
      },
    })
  })

  test("restore returns false for unknown id", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        const ok = await Checkpoint.restore("nonexistent")
        expect(ok).toBe(false)
      },
    })
  })

  test("remove deletes checkpoint", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        await fs.writeFile(path.join(tmp.path, "f.txt"), "x")
        const cp = await Checkpoint.create()
        expect(cp).toBeDefined()

        const ok = await Checkpoint.remove(cp!.id)
        expect(ok).toBe(true)

        const items = await Checkpoint.list()
        expect(items.length).toBe(0)
      },
    })
  })

  test("remove returns false for unknown id", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        const ok = await Checkpoint.remove("nonexistent")
        expect(ok).toBe(false)
      },
    })
  })

  test("diff shows changes since checkpoint", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        await fs.writeFile(path.join(tmp.path, "a.txt"), "original")
        const cp = await Checkpoint.create()
        expect(cp).toBeDefined()

        await fs.writeFile(path.join(tmp.path, "a.txt"), "modified")
        const result = await Checkpoint.diff(cp!.id)
        expect(result).toContain("original")
        expect(result).toContain("modified")
      },
    })
  })

  test("diff returns empty for unknown id", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        const result = await Checkpoint.diff("nonexistent")
        expect(result).toBe("")
      },
    })
  })

  test("auto checkpoints are labeled correctly", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        await fs.writeFile(path.join(tmp.path, "f.txt"), "x")
        const cp = await Checkpoint.create("auto-edit-123")
        expect(cp).toBeDefined()
        expect(cp!.auto).toBe(true)
      },
    })
  })

  test("list returns empty when no checkpoints", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        const items = await Checkpoint.list()
        expect(items).toEqual([])
      },
    })
  })

  test("list orders by time descending", async () => {
    await using tmp = await tmpdir({ git: true })
    await Instance.provide({
      directory: tmp.path,
      fn: async () => {
        await fs.writeFile(path.join(tmp.path, "f.txt"), "1")
        const first = await Checkpoint.create("first")
        await fs.writeFile(path.join(tmp.path, "f.txt"), "2")
        const second = await Checkpoint.create("second")

        const items = await Checkpoint.list()
        expect(items.length).toBe(2)
        expect(items[0].id).toBe(second!.id)
        expect(items[1].id).toBe(first!.id)
      },
    })
  })
})

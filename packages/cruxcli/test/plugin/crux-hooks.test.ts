import { describe, test, expect } from "bun:test"
import { CruxHooks } from "../../src/plugin/crux-hooks"

describe("crux-hooks", () => {
  describe("correction detection", () => {
    test("detects 'no, actually'", () => {
      expect(CruxHooks.detectCorrection("no, actually I want it the other way")).toBe(true)
    })

    test("detects 'instead, use'", () => {
      expect(CruxHooks.detectCorrection("instead, use a different approach")).toBe(true)
    })

    test("detects 'that's not right'", () => {
      expect(CruxHooks.detectCorrection("that's not right, the function should return a string")).toBe(true)
    })

    test("detects 'don't do'", () => {
      expect(CruxHooks.detectCorrection("don't do that, it breaks the tests")).toBe(true)
    })

    test("detects 'wrong should'", () => {
      expect(CruxHooks.detectCorrection("that's wrong, it should use async/await")).toBe(true)
    })

    test("detects 'actually, the'", () => {
      expect(CruxHooks.detectCorrection("actually, the file is in a different directory")).toBe(true)
    })

    test("detects 'I meant'", () => {
      expect(CruxHooks.detectCorrection("I meant the other file")).toBe(true)
    })

    test("detects 'please revert'", () => {
      expect(CruxHooks.detectCorrection("please revert that change")).toBe(true)
    })

    test("detects 'not what I asked'", () => {
      expect(CruxHooks.detectCorrection("that's not what I asked for")).toBe(true)
    })

    test("detects 'undo that'", () => {
      expect(CruxHooks.detectCorrection("undo that last edit")).toBe(true)
    })

    test("does NOT detect normal text", () => {
      expect(CruxHooks.detectCorrection("please add a new function to handle auth")).toBe(false)
    })

    test("does NOT detect code discussion", () => {
      expect(CruxHooks.detectCorrection("what does the build script do?")).toBe(false)
    })

    test("does NOT detect empty string", () => {
      expect(CruxHooks.detectCorrection("")).toBe(false)
    })
  })
})

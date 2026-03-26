import { Snapshot } from "../snapshot"
import { Storage } from "../storage/storage"
import { Instance } from "../project/instance"
import { Log } from "../util/log"
import { ulid } from "ulid"

const log = Log.create({ service: "checkpoint" })
const MAX = 50

export namespace Checkpoint {
  export interface Info {
    id: string
    hash: string
    label: string
    time: number
    auto: boolean
  }

  async function key() {
    return ["checkpoint", Instance.project.id]
  }

  export async function list(): Promise<Info[]> {
    try {
      const items = await Storage.read<Info[]>(await key())
      if (!items) return []
      return items.sort((a, b) => b.time - a.time)
    } catch (err) {
      if (err instanceof Storage.NotFoundError) return []
      throw err
    }
  }

  export async function create(label?: string): Promise<Info | undefined> {
    const hash = await Snapshot.track()
    if (!hash) return
    const info: Info = {
      id: ulid(),
      hash,
      label: label ?? "",
      time: Date.now(),
      auto: label?.startsWith("auto-") ?? false,
    }
    const items = await list()
    items.unshift(info)
    if (items.length > MAX) {
      const auto = items.filter((x) => x.auto)
      const manual = items.filter((x) => !x.auto)
      const pruned = [...manual, ...auto].slice(0, MAX)
      await Storage.write(await key(), pruned)
      log.info("pruned", { kept: pruned.length, removed: items.length - pruned.length })
    } else {
      await Storage.write(await key(), items)
    }
    log.info("created", { id: info.id, label: info.label, hash })
    return info
  }

  export async function restore(id: string): Promise<boolean> {
    const items = await list()
    const found = items.find((x) => x.id === id)
    if (!found) {
      log.warn("not found", { id })
      return false
    }
    await Snapshot.restore(found.hash)
    log.info("restored", { id, hash: found.hash })
    return true
  }

  export async function remove(id: string): Promise<boolean> {
    const items = await list()
    const idx = items.findIndex((x) => x.id === id)
    if (idx === -1) return false
    items.splice(idx, 1)
    await Storage.write(await key(), items)
    log.info("removed", { id })
    return true
  }

  export async function diff(id: string): Promise<string> {
    const items = await list()
    const found = items.find((x) => x.id === id)
    if (!found) return ""
    return Snapshot.diff(found.hash)
  }

  export async function patch(id: string) {
    const items = await list()
    const found = items.find((x) => x.id === id)
    if (!found) return { hash: "", files: [] }
    return Snapshot.patch(found.hash)
  }
}

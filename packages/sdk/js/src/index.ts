export * from "./client.js"
export * from "./server.js"

import { createCruxcliClient } from "./client.js"
import { createCruxcliServer } from "./server.js"
import type { ServerOptions } from "./server.js"

export async function createCruxcli(options?: ServerOptions) {
  const server = await createCruxcliServer({
    ...options,
  })

  const client = createCruxcliClient({
    baseUrl: server.url,
  })

  return {
    client,
    server,
  }
}

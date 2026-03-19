import type { Configuration } from "electron-builder"

const channel = (() => {
  const raw = process.env.CRUXCLI_CHANNEL
  if (raw === "dev" || raw === "beta" || raw === "prod") return raw
  return "dev"
})()

const getBase = (): Configuration => ({
  artifactName: "cruxcli-electron-${os}-${arch}.${ext}",
  directories: {
    output: "dist",
    buildResources: "resources",
  },
  files: ["out/**/*", "resources/**/*"],
  extraResources: [
    {
      from: "resources/",
      to: "",
      filter: ["cruxcli-cli*"],
    },
    {
      from: "native/",
      to: "native/",
      filter: ["index.js", "index.d.ts", "build/Release/mac_window.node", "swift-build/**"],
    },
  ],
  mac: {
    category: "public.app-category.developer-tools",
    icon: `resources/icons/icon.icns`,
    hardenedRuntime: true,
    gatekeeperAssess: false,
    entitlements: "resources/entitlements.plist",
    entitlementsInherit: "resources/entitlements.plist",
    notarize: true,
    target: ["dmg", "zip"],
  },
  dmg: {
    sign: true,
  },
  protocols: {
    name: "CruxCLI",
    schemes: ["cruxcli"],
  },
  win: {
    icon: `resources/icons/icon.ico`,
    target: ["nsis"],
  },
  nsis: {
    oneClick: false,
    allowToChangeInstallationDirectory: true,
    installerIcon: `resources/icons/icon.ico`,
    installerHeaderIcon: `resources/icons/icon.ico`,
  },
  linux: {
    icon: `resources/icons`,
    category: "Development",
    target: ["AppImage", "deb", "rpm"],
  },
})

function getConfig() {
  const base = getBase()

  switch (channel) {
    case "dev": {
      return {
        ...base,
        appId: "ai.cruxcli.desktop.dev",
        productName: "CruxCLI Dev",
        rpm: { packageName: "cruxcli-dev" },
      }
    }
    case "beta": {
      return {
        ...base,
        appId: "ai.cruxcli.desktop.beta",
        productName: "CruxCLI Beta",
        protocols: { name: "CruxCLI Beta", schemes: ["cruxcli"] },
        publish: { provider: "github", owner: "anomalyco", repo: "cruxcli-beta", channel: "latest" },
        rpm: { packageName: "cruxcli-beta" },
      }
    }
    case "prod": {
      return {
        ...base,
        appId: "ai.cruxcli.desktop",
        productName: "CruxCLI",
        protocols: { name: "CruxCLI", schemes: ["cruxcli"] },
        publish: { provider: "github", owner: "anomalyco", repo: "cruxcli", channel: "latest" },
        rpm: { packageName: "cruxcli" },
      }
    }
  }
}

export default getConfig()

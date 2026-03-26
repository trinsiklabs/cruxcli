const stage = process.env.SST_STAGE || "dev"

export default {
  url: stage === "production" ? "https://cruxvibe.io" : `https://${stage}.cruxvibe.io`,
  console: stage === "production" ? "https://cruxvibe.io/auth" : `https://${stage}.cruxvibe.io/auth`,
  email: "contact@anoma.ly",
  socialCard: "https://social-cards.sst.dev",
  github: "https://github.com/trinsiklabs/cruxcli",
  discord: "https://opencode.ai/discord",
  headerLinks: [
    { name: "app.header.home", url: "/" },
    { name: "app.header.docs", url: "/docs/" },
  ],
}

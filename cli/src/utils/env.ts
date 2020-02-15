import { resolve } from "path";
import { config } from "dotenv";
config({ path: resolve(__dirname, "../../.env") })

export const TEST_TOKEN = process.env.TEST_TOKEN;
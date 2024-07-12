import { MongoClient } from "mongodb";

const connectionString = process.env.MONGO_URI || "mongodb://mongo:27017/sample_training";

const client = new MongoClient(connectionString);

let conn;
try {
  conn = await client.connect();
} catch(e) {
  console.error(e);
}

let db = conn.db("sample_training");

export default db;
// secure_code.js

const express = require("express");
const bodyParser = require("body-parser");
const libxmljs = require("libxmljs");
const multer = require("multer");
const path = require("path");
const fs = require("fs");

const app = express();
const PORT = process.env.PORT || 3000;

// Constants
const ALLOWED_CONTENT_TYPES = ["application/json", "application/xml"];
const DISALLOWED_EXTENSIONS = [".admin", ".env", ".xml", ".json"];
const FILENAME_SAFE_CHARS = /[^a-zA-Z0-9.\-_]/g;

app.use(bodyParser.json());
app.use(bodyParser.text({ type: "application/xml" }));

const storage = multer.memoryStorage();
const upload = multer({ storage });

/**
 * File Upload Handler
 */
app.post("/ufo/upload", upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  const filename = req.file.originalname;
  const ext = path.extname(filename).toLowerCase();

  if (DISALLOWED_EXTENSIONS.includes(ext)) {
    return res.status(400).send("File type not allowed.");
  }

  const sanitizedFilename = path.basename(filename).replace(FILENAME_SAFE_CHARS, "_");
  const filePath = path.join(__dirname, sanitizedFilename);

  try {
    fs.writeFileSync(filePath, req.file.buffer);
    return res.status(200).send("File uploaded successfully.");
  } catch (err) {
    console.error("File write error:", err.message);
    return res.status(500).send("Internal server error.");
  }
});

/**
 * UFO Data Handler (JSON/XML)
 */
app.post("/ufo", (req, res) => {
  const contentType = req.headers["content-type"];

  if (!ALLOWED_CONTENT_TYPES.includes(contentType)) {
    return res.status(405).send("Unsupported content type");
  }

  if (contentType === "application/json") {
    console.log("Received JSON data");
    return res.status(200).json({
      ufo: "Received JSON data from an unknown planet.",
    });
  }

  if (contentType === "application/xml") {
    const rawXml = req.body;

    // Block all DTD/DOCTYPE to prevent XXE and entity expansion attacks
    if (/<!DOCTYPE/i.test(rawXml)) {
      return res.status(400).send("Invalid XML: DOCTYPE is not allowed.");
    }

    try {
      const xmlDoc = libxmljs.parseXml(rawXml, {
        replaceEntities: false,
        recover: true,
        nonet: true,
      });

      const extractedContent = [];
      xmlDoc.root().childNodes().forEach((node) => {
        if (node.type() === "element") {
          extractedContent.push(node.text());
        }
      });

      return res.status(200).type("text/plain").send(extractedContent.join(" "));
    } catch (err) {
      console.error("XML parsing error:", err.message);
      return res.status(400).send("Invalid XML: " + err.message);
    }
  }
});

// Start server
const server = app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = server;

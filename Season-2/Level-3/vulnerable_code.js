const express = require("express");
const bodyParser = require("body-parser");
const libxmljs = require("libxmljs");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.text({ type: "application/xml" }));

const storage = multer.memoryStorage();
const upload = multer({ storage });

app.post("/ufo/upload", upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  // Block dangerous file extensions
  const filename = req.file.originalname;
  const disallowedExtensions = [".admin", ".env", ".xml", ".json"];
  const ext = path.extname(filename).toLowerCase();

  if (disallowedExtensions.includes(ext)) {
    return res.status(400).send("File type not allowed.");
  }

  // Sanitize filename (basic)
  const safeName = path.basename(filename).replace(/[^a-zA-Z0-9.\-_]/g, "_");

  const uploadedFilePath = path.join(__dirname, safeName);
  fs.writeFileSync(uploadedFilePath, req.file.buffer);

  res.status(200).send("File uploaded successfully.");
});

app.post("/ufo", (req, res) => {
  const contentType = req.headers["content-type"];

  if (contentType === "application/json") {
    console.log("Received JSON data:", req.body);
    return res
      .status(200)
      .json({ ufo: "Received JSON data from an unknown planet." });
  }

  if (contentType === "application/xml") {
    try {
      // 🚨 Block all XMLs with DOCTYPE declarations to stop XXE
      if (/<!DOCTYPE/i.test(req.body)) {
        return res.status(400).send("Invalid XML: DOCTYPE is not allowed.");
      }

      // Prevent entity expansion and external access
      const xmlDoc = libxmljs.parseXml(req.body, {
        replaceEntities: false,
        recover: true,
        nonet: true,
      });

      console.log("Received XML data:", xmlDoc.toString());

      const extractedContent = [];
      xmlDoc
        .root()
        .childNodes()
        .forEach((node) => {
          if (node.type() === "element") {
            extractedContent.push(node.text());
          }
        });

      return res
        .status(200)
        .set("Content-Type", "text/plain")
        .send(extractedContent.join(" "));
    } catch (error) {
      console.error("XML parsing or validation error:", error.message);
      return res.status(400).send("Invalid XML: " + error.message);
    }
  }

  return res.status(405).send("Unsupported content type");
});

const PORT = process.env.PORT || 3000;
const server = app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = server;

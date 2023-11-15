[![Publish Docker Image](https://github.com/vements/substitute-server/actions/workflows/build-and-publish-image.yaml/badge.svg?branch=main&event=push)](https://github.com/vements/substitute-server/actions/workflows/build-and-publish-image.yaml)

## 🧪 Vements Substitute Server

The *substitute server* or *sub server* provides a basic, memory-based implementation of the [Vements REST API](https://github.com/vements/rest-api).  This server is used in development and used in CI/CD to provide a simple, fast, and reliable point for testing.

### 🎯 How It Works

The sub server is a simple Python+Flask server that provides a simplified API.  Refer to the [source](./subserver/__main__.py) for details.

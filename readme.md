## 🧪 Substitute Server

In this system, the *substitute server* or *sub server* provides a basic, memory-based implementation of the API.  This service is used in development and (will be) used in CI/CD to provide a simple, fast, and reliable server for testing the client libraries.

### 🎯 How It Works

The sub server is a simple Python+Flask server that provides a simplified API.  Refer to the [source](./subserver/__main__.py) for details.

### 🕹️ Ops

#### 🎛️ Dev Restart

When the [source files](./subserver/) changes, the changes can be applied with a container restart.  At the project root and with the `dc` shell alias:

```sh
$ dc restart substitute-server
```

#### 🎛️ Prod

TBD.

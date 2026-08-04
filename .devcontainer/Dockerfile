FROM mcr.microsoft.com/devcontainers/python:3.13

ARG TOKENSAVE_VERSION=7.8.1

# The cached Python 3.13 image can contain a stale Yarn apt source whose missing
# signing key breaks apt-get update before devcontainer features install.
RUN rm -f /etc/apt/sources.list.d/yarn.list

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl nodejs npm \
    && npm install -g @openai/codex \
    && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    arch="$(uname -m)"; \
    case "${arch}" in \
        x86_64) target_arch="x86_64" ;; \
        aarch64|arm64) target_arch="aarch64" ;; \
        *) echo "Unsupported tokensave architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    curl -fsSL "https://github.com/aovestdipaperino/tokensave/releases/download/v${TOKENSAVE_VERSION}/tokensave-v${TOKENSAVE_VERSION}-${target_arch}-linux.tar.gz" \
        | tar -xz -C /usr/local/bin tokensave; \
    chmod +x /usr/local/bin/tokensave; \
    tokensave --version

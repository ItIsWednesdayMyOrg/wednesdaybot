# Wednesday Bot

A Mastodon bot that posts quotes on Wednesdays.

## Setup

This project uses [mise](https://mise.jdx.dev/) for Python version management and [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install mise if you haven't already
curl https://mise.run | sh

# Install Python and dependencies
mise install
mise run install-dev
```

## Development

```bash
# Run tests
mise run test

# Format code
mise run format

# Lint code
mise run lint
```

## Deployment

Uses [AWS SAM](https://aws.amazon.com/serverless/sam/) for deployment.

```bash
# Build the SAM application
mise run build

# Deploy (runs sam build then sam deploy --guided)
mise run deploy
```

## Environment Variables

- `MASTODON_ACCESS_TOKEN` - Mastodon API access token
- `MASTODON_BASE_URL` - Mastodon instance base URL (e.g., `https://mastodon.social`)
- `FAKE_WEDNESDAY` - Set to any value to pretend it's Wednesday (for testing)

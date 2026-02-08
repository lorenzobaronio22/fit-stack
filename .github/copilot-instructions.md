# AI Coding Agent Instructions for fit-stack

> **Status**: Early-stage project. Update this file as architecture and patterns emerge.

## Project Overview

**fit-stack** is a web application for tracking gym training sessions with a focus on simplicity and ease of use. Users can log workouts, track progress, and manage their fitness journey with minimal friction.

**Technology Stack**:
- **Frontend**: Vue.js (web application)
- **Backend**: Python (REST API)
- **Testing**: Unit tests in frontend/backend, E2E testing in dedicated project using playwrite framework
- **CI/CD**: GitHub Actions

---

## Architecture & Components

**Monorepo Structure**:
```
fit-stack/
├── frontend/        # Vue.js web application
│   ├── src/         # Application code
│   └── tests/       # Unit/integration tests
├── backend/         # Python REST API
│   ├── app/         # Application code
│   └── tests/       # Unit tests
├── e2e/             # End-to-end tests
├── docs/            # Documentation
└── .github/         # CI/CD pipelines
```

**Architecture**: More detailed component organization and data flows will emerge during development. AI-first planning approach will be used to inform architectural decisions.

---

## Development Workflows

### Build & Run

[TODO: Document build and run approach as project develops]

### Testing

[TODO: Document testing approach as project develops]

### CI/CD Pipeline
All build, test, and deployment workflows are automated via GitHub Actions. See `.github/workflows/` for pipeline definitions.

### Debugging
[TODO: Document debugging approach as project develops]

---

## Project Conventions & Patterns

- **File Organization**: Monorepo structure keeps frontend, backend, tests, and docs organized by domain
- **Naming**: [TODO: Document naming conventions as patterns emerge in code]
- **Code Style**: [TODO: Add linting/formatting rules as development begins]
- **Error Handling**: [TODO: Document error handling and logging patterns once implemented]
- **Configuration**: Environment-specific configuration managed via `.env` files and GitHub Secrets for CI/CD

---

## Critical Integration Points

- **External Services**: [TODO: Document third-party APIs, authentication, rate limits]
- **Data Persistence**: [TODO: Database schema patterns, migrations, query conventions]
- **Inter-module Communication**: [TODO: Message passing, events, or dependency injection patterns]

---

## Development Approach

- **AI-First Planning**: Use AI agents for planning and architectural decisions before implementation
- **Iterative Development**: Architectural details emerge through development; start simple and iterate
- **Automation First**: All builds, tests, and deployments are automated via GitHub Actions - no manual steps

---

## Key Files to Reference

| File/Directory | Purpose |
|---|---|
| `frontend/` | Vue.js web application |
| `backend/` | Python REST API |
| `e2e/` | End-to-end test suite |
| `docs/` | Project documentation |
| `.github/workflows/` | CI/CD pipeline definitions |

---

## Getting Help

For project-specific questions, refer to:
- `docs/` - Project documentation
- `.github/workflows/` - CI/CD pipeline configurations

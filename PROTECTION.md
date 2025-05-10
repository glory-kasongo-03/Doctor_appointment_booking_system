# Branch Protection Rules – Doctor Appointment Booking System

To ensure the stability, reliability, and maintainability of our **Doctor Appointment Booking System**, we enforce strict branch protection rules on the `main` branch.

## Enforced Rules on `main`

- **Require pull request reviews before merging**
  - All code changes must go through a pull request (PR).
  - At least **1 reviewer** must approve the PR before merging.
  - This ensures that new code is reviewed for quality, correctness, and architectural alignment with our system design.

- **Require status checks to pass before merging**
  - Our project uses **GitHub Actions CI** to run automated tests.
  - PRs must pass all tests in the workflow (e.g., `fastapi-ci.yml`) before they can be merged.
  - This ensures all routes, services, and logic remain reliable and bug-free.

- **Disallow direct pushes to `main`**
  - Developers are **not allowed to push directly** to the `main` branch.
  - All contributions must be made via feature branches and go through PRs.

- **Include administrators**  
  - These protections apply to administrators as well, ensuring consistent enforcement.

## Why These Rules Matter

- **Protects critical production-ready code**  
  Ensures the `main` branch is always stable and deployable.

- **Prevents bugs and regressions**  
  Automated CI tests catch errors in routes, business logic, and data handling early.

- **Improves code quality**  
  Code reviews foster knowledge sharing, catch issues early, and help enforce best practices.

- **Maintains accountability and traceability**  
  PRs provide a full audit trail of who changed what and why.

- **Supports professional development practices**  
  Mimics real-world software team workflows, preparing developers for collaborative environments.

---

These rules are essential for maintaining a clean and professional development pipeline.

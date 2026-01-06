# 📂 Git Fundamentals Practice

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](https://github.com/yourusername/git-fundamentals-practice/releases/tag/v1.0.0)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/git-fundamentals-practice/actions)

A professional practice repository demonstrating industry-standard Git and GitHub workflows, including structured commits, comprehensive ignore rules, documentation, and contribution guidelines.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Credits](#credits)
- [Contact](#contact)
- [License](#license)
- [Changelog](#changelog)

## Project Overview

This repository serves as a hands-on exercise to master Git fundamentals while adhering to real-world best practices used in professional software development teams. It includes:

- A comprehensive `.gitignore`
- Conventional commit messages
- Proper project structure
- Professional documentation
- GitHub templates and workflows

Perfect for learning, portfolio building, or interview preparation.

## Features

- MIT Licensed open-source project
- Structured directories for source code, tests, and documentation
- Detailed `.gitignore` with commented sections
- Conventional Commits compliance
- GitHub Issue Template
- Complete changelog
- Setup guide in `docs/`

## Project Structure

```
git-fundamentals-practice/
├── .github/
│   └── ISSUE_TEMPLATE.md          # GitHub issue template
├── docs/
│   └── SETUP.md                      # Detailed setup instructions
├── src/                              # Source code (empty with .gitkeep)
│   └── .gitkeep
├── tests/                            # Test files (empty with .gitkeep)
│   └── .gitkeep
├── .gitignore                        # Comprehensive ignore rules
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── README.md                         # This README file
```

## Installation

No dependencies are required — this is a Git practice project.

1. Clone the repository:
   ```bash
   git clone https://github.com/JuniorSillo/git-fundamentals-practice.git
   ```

2. Navigate into the project directory:
   ```bash
   cd git-fundamentals-practice
   ```

3. Explore the structure and start practicing Git commands!

For detailed setup steps, see [`docs/SETUP.md`](docs/SETUP.md).

## Usage

This repository is designed for practicing core Git operations. Here are some recommended examples:

### 1. Create and switch to a new feature branch
```bash
git checkout -b feat/new-feature
```

### 2. Make changes and commit using Conventional Commits
```bash
git add .
git commit -m "feat: add new practice script"
# or
git commit -m "docs: update contribution guidelines"
# or
git commit -m "chore: update .gitignore for Python"
```

### 3. Push branch and open a Pull Request
```bash
git push origin feat/new-feature
```
Then visit GitHub to create a PR with a clear description.

### 4. View commit history
```bash
git log --oneline --graph --decorate
```

Feel free to experiment with branching, merging, rebasing, stashing, and resolving conflicts!

## Contributing

Contributions are highly encouraged! Please follow these steps:

1. Fork this repository
2. Create a descriptive branch:
   ```bash
   git checkout -b feat/JuniorSillo
   ```
3. Make your changes
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/)
5. Push and open a Pull Request
6. Reference any related issues

Please see [`.github/ISSUE_TEMPLATE.md`](.github/ISSUE_TEMPLATE.md) when reporting bugs or requesting features.

## Code of Conduct

This project adheres to a respectful and inclusive community. Be kind, patient, and professional in all interactions.

## Credits

**Created and maintained by**  
[Moeketsi Junior Sillo](https://github.com/JuniorSillo)  

This project was built as a learning exercise to demonstrate professional Git practices.

## Contact

For questions, suggestions, or collaboration:  
✉️ sillojunior8@gmail.com 
💼 [Moeketsi Junior Sillo](https://linkedin.com/in/meoketsijuniorsillo) (optional)

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## Changelog

All notable changes are documented in [`CHANGELOG.md`](CHANGELOG.md).
```

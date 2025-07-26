# Contributing to AWS Ground Station Well Architected Guide

Thank you for your interest in contributing to the AWS Ground Station Well Architected Guide! This project aims to help AWS Solutions Architects conduct effective Well Architected Framework reviews for Ground Station workloads.

## How to Contribute

### Reporting Issues

If you find bugs, have suggestions for improvements, or want to request new features:

1. **Search existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear, descriptive title
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Relevant context (AWS region, Ground Station use case, etc.)

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following our guidelines below
4. **Test your changes** with real or sample workloads
5. **Commit with clear messages**:
   ```bash
   git commit -m "Add: New question for satellite data encryption"
   ```
6. **Push to your fork** and **create a pull request**

### Types of Contributions Welcome

#### Documentation Improvements
- Clarifying existing instructions
- Adding examples and use cases
- Fixing typos and formatting
- Improving readability and organization

#### Custom Lens Enhancements
- Adding new questions for emerging Ground Station patterns
- Improving risk assessment rules
- Enhancing improvement plans with specific AWS services
- Adding industry-specific variations

#### Templates and Tools
- Improving report templates
- Adding automation scripts
- Creating new checklists for specific scenarios
- Developing integration tools

#### Best Practices and Patterns
- Documenting new architecture patterns
- Adding troubleshooting guides
- Sharing lessons learned from real reviews
- Contributing regulatory compliance guidance

## Contribution Guidelines

### Code Style and Standards

#### Documentation
- Use clear, concise language
- Follow markdown best practices
- Include code examples where helpful
- Maintain consistent formatting

#### JSON Files (Custom Lens)
- Follow the AWS Well Architected custom lens schema
- Use descriptive IDs and titles
- Include helpful resources with valid URLs
- Test risk rules logic thoroughly

#### Templates
- Keep templates generic but comprehensive
- Include placeholder text with clear instructions
- Maintain professional formatting
- Ensure templates are customizable

### Content Guidelines

#### Technical Accuracy
- Verify all AWS service references and capabilities
- Test procedures and instructions
- Include current pricing and service availability
- Reference official AWS documentation

#### Ground Station Specificity
- Focus on satellite communication use cases
- Address mission-critical operational requirements
- Consider regulatory and compliance aspects
- Include real-world scenarios and examples

#### Well Architected Alignment
- Follow the five-pillar framework structure
- Maintain consistency with AWS Well Architected principles
- Use standard terminology and concepts
- Align with current Well Architected best practices

### Review Process

1. **Automated Checks**: PRs will be checked for:
   - Markdown formatting
   - Link validity
   - JSON schema compliance
   - Spelling and grammar

2. **Peer Review**: All contributions will be reviewed by:
   - AWS Solutions Architects with Ground Station experience
   - Well Architected Framework experts
   - Technical writers for clarity and consistency

3. **Testing**: Changes will be tested with:
   - Sample Ground Station workloads
   - Real customer scenarios (anonymized)
   - Different industry verticals

### Getting Help

- **Questions about contributing**: Open an issue with the "question" label
- **Technical discussions**: Use GitHub Discussions
- **AWS-specific questions**: Reference official AWS documentation
- **Urgent issues**: Contact the maintainers directly

## Development Setup

### Prerequisites
- Git
- Text editor with markdown support
- AWS CLI (for testing custom lens import)
- Access to AWS Well Architected Tool (for testing)

### Local Development
1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/aws-ground-station-well-architected-guide.git
   ```
2. Create a branch for your changes
3. Make changes using your preferred editor
4. Test custom lens changes by importing into Well Architected Tool
5. Validate markdown formatting and links

### Testing Custom Lens Changes
1. Import the modified lens into AWS Well Architected Tool
2. Create a test workload
3. Verify all questions display correctly
4. Test risk assessment rules with different answer combinations
5. Validate improvement plans and helpful resources

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Annual contributor acknowledgments

## Code of Conduct

### Our Standards
- **Be respectful** and inclusive in all interactions
- **Be constructive** in feedback and criticism
- **Focus on the content**, not the person
- **Help others learn** and grow
- **Maintain professionalism** in all communications

### Unacceptable Behavior
- Harassment, discrimination, or offensive language
- Personal attacks or inflammatory comments
- Sharing confidential customer information
- Spam or off-topic discussions

### Enforcement
Violations of the code of conduct should be reported to the project maintainers. All reports will be investigated promptly and fairly.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, please:
1. Check existing issues and discussions
2. Review this contributing guide
3. Open a new issue with the "question" label
4. Contact the maintainers if needed

Thank you for helping make this guide better for the AWS community!

---

**Maintainers:**
- AWS Solutions Architecture Team
- Ground Station Specialists
- Well Architected Framework Experts

**Last Updated:** January 2025

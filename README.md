# Domain Expiry Checker with Slack Notifications


## Overview

The **Domain Expiry Checker with Slack Notifications** is a custom GitHub Action designed to monitor the expiry dates of domains and send notifications to a specified Slack channel if any domains are expiring within the next 30 days. This action is particularly useful for organizations and developers who need to ensure that their domain names are renewed in a timely manner to prevent service disruptions.

## Features

- **Multiple Domain Support**: Monitor multiple domains at once by providing a comma-separated list.
- **Slack Notifications**: Sends alerts to a Slack channel when a domain is approaching its expiry date (within 30 days).
- **Docker-Based**: Runs in a Docker container, ensuring consistent execution regardless of the environment.
- **Organization-Wide Reusability**: Can be used across multiple repositories within an organization, even when hosted in a private repository.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Workflow Example](#workflow-example)
- [Configuration](#configuration)
- [Security Considerations](#security-considerations)

## Getting Started

### Prerequisites

To use this action, you'll need the following:

- A GitHub repository where you can define workflows.
- A Slack Webhook URL for sending notifications.
- A personal access token (PAT) with `repo` access if you're using the action from a private repository.

### Installation

This action can be installed by cloning or forking the repository, or it can be referenced directly in your GitHub Actions workflows if it's hosted in a public or private repository.

## Usage

### Inputs

- **`domains`**: A comma-separated list of domains to check. This input is required.
- **`slack_webhook`**: The Slack Webhook URL for sending notifications. This input is required.

### Outputs

There are no outputs from this action. The action's purpose is to send a notification to Slack if any domains are expiring soon.

## Workflow Example

Here’s an example of how to use the `Domain Expiry Checker with Slack Notifications` in a GitHub Actions workflow:

```yaml
name: Check Domain Expiry

on:
  schedule:
    - cron: '0 0 * * *'  # Runs every day at midnight
  workflow_dispatch:  # Allows manual triggering

jobs:
  check_expiry:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Checkout private action repo
      uses: actions/checkout@v3
      with:
        repository: your-org/private-action-repo
        token: ${{ secrets.ACTIONS_PAT }}

    - name: Check domain expiry
      uses: your-org/private-action-repo@main
      with:
        domains: ${{ secrets.DOMAIN_NAME_LIST }}  # A comma-separated list of domains
        slack_webhook: ${{ secrets.SLACK_WEBHOOK_URL }}

```

### Configuration

1.  **Set Up Slack Webhook**:
    
    *   Create a new Incoming Webhook in your Slack workspace.
        
    *   Copy the Webhook URL and add it to your GitHub repository secrets as SLACK\_WEBHOOK\_URL.
        
2.  **Personal Access Token (PAT)**:
    
    *   Generate a PAT with repo scope from your GitHub account.
        
    *   Add the PAT to your GitHub repository secrets as ACTIONS\_PAT.
        
3.  **Domain List**:
    
    *   Add the domains you want to monitor as a comma-separated string in your GitHub secrets, named DOMAINS.


Security Considerations
-----------------------

*   **Secrets Management**: Store your Slack Webhook URL and PAT securely using GitHub Secrets. Avoid hardcoding sensitive information.
    
*   **Access Control**: Ensure that the PAT used has the minimum necessary permissions, and regularly rotate tokens to maintain security.
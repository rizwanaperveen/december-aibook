#!/bin/bash

# Deployment script for Embodied AI Systems Book to GitHub Pages

set -e  # Exit on any error

echo "Starting deployment to GitHub Pages..."

# Navigate to the frontend directory
cd frontend/my-aibook

# Build the Docusaurus site
echo "Building the Docusaurus site..."
npm install
npm run build

# Navigate back to the root
cd ../..

# Configure git user
git config --global user.name "GitHub Actions"
git config --global user.email "actions@github.com"

# Deploy to GitHub Pages
echo "Deploying to GitHub Pages..."
npx docusaurus deploy

echo "Deployment completed successfully!"
const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

// Recursively get all markdown files in a directory
function getAllMarkdownFiles(dirPath, arrayOfFiles = []) {
  const files = fs.readdirSync(dirPath);

  files.forEach((file) => {
    const filePath = path.join(dirPath, file);
    if (fs.statSync(filePath).isDirectory()) {
      arrayOfFiles = getAllMarkdownFiles(filePath, arrayOfFiles);
    } else if (file.endsWith('.md')) {
      arrayOfFiles.push(filePath);
    }
  });

  return arrayOfFiles;
}

// Process all markdown files in the docs directory
function processDocs() {
  const docsPath = path.join(__dirname, '../docs');
  const output = [];

  // Get all markdown files recursively
  const allFiles = getAllMarkdownFiles(docsPath);

  for (const filePath of allFiles) {
    const content = fs.readFileSync(filePath, 'utf8');
    const relativePath = path.relative(docsPath, filePath);
    const file = path.basename(filePath);

    // Parse frontmatter and content
    const { data, content: markdownContent } = matter(content);

    // Extract title from frontmatter or from the first heading
    let title = data.title || '';
    if (!title) {
      const match = markdownContent.match(/^#\s+(.*)/m);
      if (match) {
        title = match[1];
      } else {
        title = file.replace('.md', '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
      }
    }

    // Determine module based on directory path and filename
    let module = 'Introduction';
    if (relativePath.includes('module-1')) {
      module = 'Module 1: Robotic Nervous System (ROS 2)';
    } else if (relativePath.includes('module-2')) {
      module = 'Module 2: Digital Twin (Gazebo + Unity)';
    } else if (relativePath.includes('module-3')) {
      module = 'Module 3: The AI-Robot Brain (NVIDIA Isaac)';
    } else if (relativePath.includes('module-4')) {
      module = 'Module 4: Vision-Language-Action (VLA)';
    } else if (file.includes('ros2') || file.includes('basics')) {
      module = 'Module 1: Robotic Nervous System (ROS 2)';
    } else if (file.includes('digital') || file.includes('twin')) {
      module = 'Module 2: Digital Twin (Gazebo + Unity)';
    }

    // Extract chapter from filename
    const chapterMatch = file.match(/\d+\.\d+-(.*)/);
    let chapter = chapterMatch ? chapterMatch[1].replace(/-/g, ' ') : file.replace('.md', '');

    output.push({
      id: relativePath.replace('.md', '').replace(/\\/g, '/'),
      title: title,
      content: markdownContent,
      module: module,
      chapter: chapter,
      path: `/docs/${relativePath.replace('.md', '').replace(/\\/g, '/')}`
    });
  }

  // Write the processed content to a JSON file
  const outputPath = path.join(__dirname, '../static/book-content.json');
  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));

  console.log(`Processed ${output.length} documentation files`);
}

processDocs();
const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

// Process all markdown files in the docs directory
function processDocs() {
  const docsPath = path.join(__dirname, '../docs');
  const output = [];

  const files = fs.readdirSync(docsPath);

  for (const file of files) {
    if (file.endsWith('.md')) {
      const filePath = path.join(docsPath, file);
      const content = fs.readFileSync(filePath, 'utf8');

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

      // Determine module based on filename
      let module = 'Introduction';
      if (file.includes('ros2') || file.includes('basics')) {
        module = 'Module 1: Robotic Nervous System (ROS 2)';
      } else if (file.includes('digital') || file.includes('twin')) {
        module = 'Module 2: Digital Twin (Gazebo + Unity)';
      }

      output.push({
        id: file.replace('.md', ''),
        title: title,
        content: markdownContent,
        module: module,
        path: `/docs/${file.replace('.md', '')}`
      });
    }
  }

  // Write the processed content to a JSON file
  const outputPath = path.join(__dirname, '../static/book-content.json');
  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));

  console.log(`Processed ${output.length} documentation files`);
}

processDocs();
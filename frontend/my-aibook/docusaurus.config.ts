import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here

const config: Config = {
  title: 'Embodied AI Systems Book',
  tagline: 'Learn about Robotic Nervous Systems and Digital Twins',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // ✅ VERCEL PRODUCTION URL
  url: 'https://localhost:3000',

  // ✅ Vercel always uses root
  baseUrl: '/',

  // ❌ GitHub Pages specific config REMOVED
  // organizationName
  // projectName
  // deploymentBranch

  trailingSlash: false,
  onBrokenLinks: 'warn',

  staticDirectories: ['static'],

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/rizwanaperveen/december-aibook/tree/main/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/rizwanaperveen/december-aibook/tree/main/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Embodied AI Systems',
      logo: {
        alt: 'Embodied AI Systems Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Book',
        },
        {to: '/chat', label: 'AI Assistant', position: 'left'},
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/rizwanaperveen/december-aibook',
          label: 'GitHub',
          position: 'right',
        },
        {to: '/login', label: 'Login', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Book Content',
          items: [
            { label: 'Introduction', to: '/docs/intro' },
            { label: 'ROS 2 Basics', to: '/docs/ros2-basics' },
            { label: 'Digital Twins', to: '/docs/digital-twins' },
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/rizwanaperveen/december-aibook',
            },
            {
              label: 'Docusaurus',
              href: 'https://docusaurus.io',
            },
          ],
        },
        {
          title: 'More',
          items: [{ label: 'Blog', to: '/blog' }],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Embodied AI Systems Book.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;

const { generateMarkdown } = require('../lib/markdownGenerator');
const fs = require('fs');

const bp = JSON.parse(fs.readFileSync('data/blueprints.json'))['6_maths'];

const tests = [
  {},
  { setName: 'MIXED SET' },
  { setName: 'mixed set' },
  { setName: 'CUSTOM SET' },
  { setName: 'custom' },
  { setName: 'Sample Paper' },
  { setName: 'Set A' },
  { setName: 'SET – B' },
  { setName: '   ' }
];

tests.forEach((meta, idx) => {
  const md = generateMarkdown(bp, [], meta);
  const titleLine = md.split('\n').find(l => l.startsWith('## '));
  console.log(`Test ${idx + 1}: [${meta.setName || ''}] -> "${titleLine}"`);
});

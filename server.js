const express = require('express');
const path = require('path');
const fs = require('fs');
const { generateMarkdown } = require('./lib/markdownGenerator');

const app = express();
const PORT = process.env.PORT || 3000;

// Setup Pug View Engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// Middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
app.use(express.static(path.join(__dirname, 'public')));

// Load Database
const BLUEPRINTS_PATH = path.join(__dirname, 'data', 'blueprints.json');
const QUESTIONS_PATH = path.join(__dirname, 'data', 'questions.json');
const SAVED_PAPERS_PATH = path.join(__dirname, 'data', 'saved_papers.json');

function getBlueprints() {
  return JSON.parse(fs.readFileSync(BLUEPRINTS_PATH, 'utf-8'));
}

function getQuestions(subjectId) {
  const all = JSON.parse(fs.readFileSync(QUESTIONS_PATH, 'utf-8'));
  return subjectId ? (all[subjectId] || []) : all;
}

function getSavedPapers() {
  if (!fs.existsSync(SAVED_PAPERS_PATH)) {
    fs.writeFileSync(SAVED_PAPERS_PATH, '[]', 'utf-8');
  }
  return JSON.parse(fs.readFileSync(SAVED_PAPERS_PATH, 'utf-8'));
}

function savePapers(papers) {
  fs.writeFileSync(SAVED_PAPERS_PATH, JSON.stringify(papers, null, 2), 'utf-8');
}

// Routes
app.get('/', (req, res) => {
  const blueprints = getBlueprints();
  const subjects = Object.values(blueprints);
  res.render('index', {
    subjects,
    initialSubject: subjects[0]
  });
});

// API: Get all subjects & blueprints
app.get('/api/subjects', (req, res) => {
  res.json(getBlueprints());
});

// API: Get questions for a subject
app.get('/api/questions/:subjectId', (req, res) => {
  const { subjectId } = req.params;
  const questions = getQuestions(subjectId);
  const blueprints = getBlueprints();
  const bp = blueprints[subjectId];
  if (!bp) {
    return res.status(404).json({ error: 'Subject not found' });
  }
  res.json({
    blueprint: bp,
    questions: questions
  });
});

// API: Generate Markdown from chosen question IDs
app.post('/api/generate-markdown', (req, res) => {
  const { subjectId, questionIds, customMeta } = req.body;
  const blueprints = getBlueprints();
  const bp = blueprints[subjectId];
  if (!bp) {
    return res.status(400).json({ error: 'Invalid subject' });
  }

  const allQuestions = getQuestions(subjectId);
  const qMap = new Map(allQuestions.map(q => [q.id, q]));
  const selected = (questionIds || []).map(id => qMap.get(id)).filter(Boolean);

  const markdown = generateMarkdown(bp, selected, customMeta, allQuestions);
  res.json({ markdown, count: selected.length });
});

// API: Save custom paper
app.post('/api/save-paper', (req, res) => {
  const { title, subjectId, questionIds, customMeta } = req.body;
  const papers = getSavedPapers();
  const newPaper = {
    id: 'paper_' + Date.now(),
    title: title || 'Custom Paper ' + new Date().toLocaleDateString(),
    subjectId,
    questionIds,
    customMeta: customMeta || {},
    createdAt: new Date().toISOString()
  };
  papers.unshift(newPaper);
  savePapers(papers);
  res.json({ success: true, paper: newPaper });
});

// API: List saved papers
app.get('/api/saved-papers', (req, res) => {
  res.json(getSavedPapers());
});

// API: Delete saved paper
app.delete('/api/saved-papers/:id', (req, res) => {
  const { id } = req.params;
  let papers = getSavedPapers();
  papers = papers.filter(p => p.id !== id);
  savePapers(papers);
  res.json({ success: true });
});

// Print View (HTML for Browser Print / PDF Export)
app.post('/print', (req, res) => {
  let { subjectId, questionIds, customMeta } = req.body;
  if (typeof questionIds === 'string') {
    try { questionIds = JSON.parse(questionIds); } catch (e) {}
  }
  if (typeof customMeta === 'string') {
    try { customMeta = JSON.parse(customMeta); } catch (e) {}
  }

  const blueprints = getBlueprints();
  const bp = blueprints[subjectId];
  if (!bp) {
    return res.status(400).send('Subject not found');
  }

  const allQuestions = getQuestions(subjectId);
  const qMap = new Map(allQuestions.map(q => [q.id, q]));
  const selected = (questionIds || []).map(id => qMap.get(id)).filter(Boolean);
  const markdown = generateMarkdown(bp, selected, customMeta, allQuestions);

  res.render('print', {
    blueprint: bp,
    markdown,
    customMeta: customMeta || {},
    title: (customMeta && customMeta.setName) ? `${bp.name} - ${customMeta.setName}` : bp.name
  });
});

// Print Saved Paper by ID
app.get('/print/:id', (req, res) => {
  const { id } = req.params;
  const papers = getSavedPapers();
  const paper = papers.find(p => p.id === id);
  if (!paper) {
    return res.status(404).send('Saved paper not found');
  }

  const blueprints = getBlueprints();
  const bp = blueprints[paper.subjectId];
  if (!bp) {
    return res.status(400).send('Subject not found');
  }

  const allQuestions = getQuestions(paper.subjectId);
  const qMap = new Map(allQuestions.map(q => [q.id, q]));
  const selected = (paper.questionIds || []).map(qid => qMap.get(qid)).filter(Boolean);
  const markdown = generateMarkdown(bp, selected, paper.customMeta, allQuestions);

  res.render('print', {
    blueprint: bp,
    markdown,
    customMeta: paper.customMeta || {},
    title: paper.title || bp.name
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

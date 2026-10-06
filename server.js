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

function saveQuestions(allQuestions) {
  fs.writeFileSync(QUESTIONS_PATH, JSON.stringify(allQuestions, null, 2), 'utf-8');
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

// API: Create new subject / class blueprint
app.post('/api/subjects', (req, res) => {
  const { id, name, class: className, subject, time, maxMarks, isScience, pattern, sections } = req.body;
  if (!name || !className || !subject) {
    return res.status(400).json({ error: 'Missing required fields (name, class, subject)' });
  }

  const blueprints = getBlueprints();
  const rawId = (id || `${className}_${subject}`).toLowerCase().replace(/[^a-z0-9_]/g, '_').replace(/_+/g, '_').trim();
  const subjectId = rawId || `sub_${Date.now()}`;

  let defaultSections = sections;
  if (!Array.isArray(defaultSections) || defaultSections.length === 0) {
    if (pattern === 'science' || isScience) {
      defaultSections = [
        { key: "sec_1", title: "### SECTION 1 / खंड 1", subTitle: "Tick (✓) the correct answer in answer sheet / उत्तर पुस्तिका में सही उत्तर पर सही (✓) का निशान लगाएँ", marksEach: 1, requiredCount: 5, totalMarks: 5 },
        { key: "sec_2", title: "### SECTION 2 / खंड 2", subTitle: "Fill in the blanks / रिक्त स्थानों की पूर्ति कीजिए", marksEach: 1, requiredCount: 5, totalMarks: 5 },
        { key: "sec_3", title: "### SECTION 3 / खंड 3", subTitle: "State whether the given statements are True (T) or False (F) / बताएँ कि निम्नलिखित कथन सत्य (T) हैं या असत्य (F)", marksEach: 1, requiredCount: 5, totalMarks: 5 },
        { key: "sec_4", title: "### SECTION 4 / खंड 4", subTitle: "Very Short Answer type questions / अति लघु उत्तरीय प्रश्न", marksEach: 2, requiredCount: 5, totalMarks: 10 },
        { key: "sec_5", title: "### SECTION 5 / खंड 5", subTitle: "Short Answer type questions / लघु उत्तरीय प्रश्न", marksEach: 3, requiredCount: 5, totalMarks: 15 },
        { key: "sec_6", title: "### SECTION 6 / खंड 6", subTitle: "Long Answer type questions / दीर्घ उत्तरीय प्रश्न", marksEach: 5, requiredCount: 2, totalMarks: 10 }
      ];
    } else if (pattern === 'language') {
      defaultSections = [
        { key: "sec_a", title: "### SECTION 'A' / खंड 'क'", subTitle: "Reading & Comprehension / अपठित बोध", marksEach: 1, requiredCount: 10, totalMarks: 10 },
        { key: "sec_b", title: "### SECTION 'B' / खंड 'ख'", subTitle: "Writing Skills / रचनात्मक लेखन", marksEach: 5, requiredCount: 2, totalMarks: 10 },
        { key: "sec_c", title: "### SECTION 'C' / खंड 'ग'", subTitle: "Grammar & Vocabulary / व्यावहारिक व्याकरण", marksEach: 2, requiredCount: 5, totalMarks: 10 },
        { key: "sec_d", title: "### SECTION 'D' / खंड 'घ'", subTitle: "Literature & Textual Questions / पाठ्यपुस्तक प्रश्नोत्तर", marksEach: 4, requiredCount: 5, totalMarks: 20 }
      ];
    } else {
      defaultSections = [
        { key: "sec_a", title: "### SECTION 'A' / खंड 'क'", subTitle: "Formulas & Core Concepts / सूत्र एवं मूल अवधारणाएँ", marksEach: 1, requiredCount: 5, totalMarks: 5 },
        { key: "sec_b", title: "### SECTION 'B' / खंड 'ख'", subTitle: "Multiple Choice & True/False / बहुविकल्पीय एवं सत्य-असत्य प्रश्न", marksEach: 1, requiredCount: 5, totalMarks: 5 },
        { key: "sec_c", title: "### SECTION 'C' / खंड 'ग'", subTitle: "Very Short Answer & Concepts / अति लघु उत्तरीय प्रश्न", marksEach: 2, requiredCount: 6, totalMarks: 12 },
        { key: "sec_d", title: "### SECTION 'D' / खंड 'घ'", subTitle: "Short Answer & Calculations / लघु उत्तरीय एवं क्रमबद्ध गणनाएँ", marksEach: 3, requiredCount: 4, totalMarks: 12 },
        { key: "sec_e", title: "### SECTION 'E' / खंड 'ङ'", subTitle: "Long Answer & Word Problems / दीर्घ उत्तरीय एवं व्यावहारिक समस्याएँ", marksEach: 4, requiredCount: 4, totalMarks: 16 }
      ];
    }
  }

  const newBp = {
    id: subjectId,
    name: name.trim(),
    class: className.trim(),
    subject: subject.trim(),
    time: time || "2½ HOURS",
    maxMarks: Number(maxMarks) || 50,
    isScience: Boolean(isScience || pattern === 'science'),
    schoolName: "NEW M.V.M. SENIOR SECONDARY SCHOOL, ALWAR",
    examTitle: "HALF YEARLY EXAMINATION: 2026 – 27",
    sections: defaultSections
  };

  blueprints[subjectId] = newBp;
  fs.writeFileSync(BLUEPRINTS_PATH, JSON.stringify(blueprints, null, 2), 'utf-8');

  const allQuestions = JSON.parse(fs.readFileSync(QUESTIONS_PATH, 'utf-8'));
  if (!allQuestions[subjectId]) {
    allQuestions[subjectId] = [];
    saveQuestions(allQuestions);
  }

  res.json({ success: true, subject: newBp });
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

// API: Create new custom question
app.post('/api/questions', (req, res) => {
  const { subjectId, sectionKey, chapter, marks, content, preview, set } = req.body;
  if (!subjectId || !sectionKey || !content) {
    return res.status(400).json({ error: 'Missing required question fields (subjectId, sectionKey, content)' });
  }

  const all = JSON.parse(fs.readFileSync(QUESTIONS_PATH, 'utf-8'));
  if (!all[subjectId]) {
    all[subjectId] = [];
  }

  const qId = 'custom_' + subjectId + '_' + Date.now() + '_' + Math.floor(Math.random() * 1000);
  const newQuestion = {
    id: qId,
    subjectId,
    sectionKey,
    set: set || 'Custom',
    orderInSet: all[subjectId].length + 1,
    originalNum: 'Custom Q',
    marks: Number(marks) || 1,
    hasOrChoice: false,
    preview: preview || (content.replace(/[*#]/g, '').trim().substring(0, 100) + '...'),
    content: content.trim(),
    chapter: chapter || 'General / Uncategorized'
  };

  all[subjectId].push(newQuestion);
  saveQuestions(all);
  res.json({ success: true, question: newQuestion });
});

// API: Update existing question
app.put('/api/questions/:subjectId/:id', (req, res) => {
  const { subjectId, id } = req.params;
  const { sectionKey, chapter, marks, content, preview, set } = req.body;
  const all = JSON.parse(fs.readFileSync(QUESTIONS_PATH, 'utf-8'));
  if (!all[subjectId]) {
    return res.status(404).json({ error: 'Subject not found' });
  }

  const idx = all[subjectId].findIndex(q => q.id === id);
  if (idx === -1) {
    return res.status(404).json({ error: 'Question not found' });
  }

  const existing = all[subjectId][idx];
  if (sectionKey) existing.sectionKey = sectionKey;
  if (chapter) existing.chapter = chapter;
  if (marks !== undefined) existing.marks = Number(marks) || existing.marks;
  if (content) existing.content = content.trim();
  if (preview) existing.preview = preview;
  if (set) existing.set = set;

  saveQuestions(all);
  res.json({ success: true, question: existing });
});

// API: Delete question
app.delete('/api/questions/:subjectId/:id', (req, res) => {
  const { subjectId, id } = req.params;
  const all = JSON.parse(fs.readFileSync(QUESTIONS_PATH, 'utf-8'));
  if (!all[subjectId]) {
    return res.status(404).json({ error: 'Subject not found' });
  }

  const initialLen = all[subjectId].length;
  all[subjectId] = all[subjectId].filter(q => q.id !== id);
  if (all[subjectId].length === initialLen) {
    return res.status(404).json({ error: 'Question not found' });
  }

  saveQuestions(all);
  res.json({ success: true });
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

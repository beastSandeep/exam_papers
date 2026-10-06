/**
 * Exam Paper Builder - Client Application Logic (Alpine.js)
 */

function paperApp() {
  return {
    // Subject & Blueprint State
    subjectsList: window.__INITIAL_SUBJECTS__ || [],
    selectedSubjectId: window.__INITIAL_SUBJECT__ ? window.__INITIAL_SUBJECT__.id : '6_maths',
    currentBlueprint: window.__INITIAL_SUBJECT__ || {},
    questions: [],
    activeSectionKey: '',
    selectedQuestionIds: [],
    orPairs: {},
    orPairsBySubject: {},
    customMarks: {},
    customMarksBySubject: {},
    pairingModalOpen: false,
    pairingPrimaryQuestionId: null,
    pairingChapterFilter: 'all',
    variationFilter: 'all',
    chapterFilter: 'all',
    previewModalOpen: false,
    savedPapersModalOpen: false,
    savedPapersList: [],
    savedPapersCount: 0,
    toastMessage: '',

    // Paper Saver & Layout Preferences
    printLayoutMode: 'compact', // 'standard' | 'compact' | 'twocolumn'
    
    // Class & Subject Management State
    selectedClassFilter: 'all',
    addSubjectModalOpen: false,
    newSubClass: '',
    newSubId: '',
    newSubName: '',
    newSubSubject: '',
    newSubMaxMarks: 50,
    newSubTime: '2½ HOURS',
    newSubPattern: 'maths',
    isSubmittingSubject: false,

    // Custom Question Creator & Archetype Studio State
    createQuestionModalOpen: false,
    isEditingQuestion: false,
    editingQuestionId: null,
    activeArchetype: 'mcq',
    lastFocusedInputId: 'input-q-english-mcq',
    newQuestionSubjectId: '',
    newQuestionSectionKey: '',
    newQuestionChapter: '',
    newQuestionCustomChapter: '',
    newQuestionMarks: 1,
    newQuestionSet: 'Custom',
    newQuestionEnglish: '',
    newQuestionHindi: '',
    newQuestionMcqOptions: [
      { en: '', hi: '' },
      { en: '', hi: '' },
      { en: '', hi: '' },
      { en: '', hi: '' }
    ],
    newQuestionTfStyle: 'standard',
    newQuestionLaParts: [
      { part: 'a', en: '', hi: '', marks: 2 },
      { part: 'b', en: '', hi: '', marks: 2 }
    ],
    newQuestionMatchPromptEn: 'Match the items in Column I with Column II:',
    newQuestionMatchPromptHi: 'स्तंभ I के कथनों का स्तंभ II से सही मिलान कीजिए:',
    newQuestionMatchPairs: [
      { col1En: '', col1Hi: '', col2En: '', col2Hi: '' },
      { col1En: '', col1Hi: '', col2En: '', col2Hi: '' },
      { col1En: '', col1Hi: '', col2En: '', col2Hi: '' },
      { col1En: '', col1Hi: '', col2En: '', col2Hi: '' }
    ],
    newQuestionRawContent: '',
    newQuestionAutoSelect: true,
    isSavingCustomQuestion: false,
    subjectChaptersCache: {},
    customMeta: {
      schoolName: 'NEW M.V.M. SENIOR SECONDARY SCHOOL, ALWAR',
      examTitle: 'HALF YEARLY EXAMINATION: 2026 – 27',
      setName: '',
      maxMarks: null,
      time: '2½ HOURS',
      includeInstructions: true
    },
    selectionsBySubject: {},
    metaBySubject: {},
    activeSectionBySubject: {},
    chapterFilterBySubject: {},
    variationFilterBySubject: {},
    visitedSubjects: {},

    // ==========================================
    // State Persistence (LocalStorage)
    // ==========================================
    persistState() {
      try {
        if (this.selectedSubjectId) {
          this.selectionsBySubject[this.selectedSubjectId] = [...this.selectedQuestionIds];
          this.metaBySubject[this.selectedSubjectId] = { ...this.customMeta };
          this.orPairsBySubject[this.selectedSubjectId] = { ...this.orPairs };
          this.customMarksBySubject[this.selectedSubjectId] = { ...this.customMarks };
          this.activeSectionBySubject[this.selectedSubjectId] = this.activeSectionKey;
          this.chapterFilterBySubject[this.selectedSubjectId] = this.chapterFilter;
          this.variationFilterBySubject[this.selectedSubjectId] = this.variationFilter;
          this.visitedSubjects[this.selectedSubjectId] = true;
        }

        localStorage.setItem('exam_builder_selections', JSON.stringify(this.selectionsBySubject));
        localStorage.setItem('exam_builder_meta', JSON.stringify(this.metaBySubject));
        localStorage.setItem('exam_builder_orpairs', JSON.stringify(this.orPairsBySubject));
        localStorage.setItem('exam_builder_custom_marks', JSON.stringify(this.customMarksBySubject));
        localStorage.setItem('exam_builder_active_sections', JSON.stringify(this.activeSectionBySubject));
        localStorage.setItem('exam_builder_chapter_filters', JSON.stringify(this.chapterFilterBySubject));
        localStorage.setItem('exam_builder_variation_filters', JSON.stringify(this.variationFilterBySubject));
        localStorage.setItem('exam_builder_visited', JSON.stringify(this.visitedSubjects));
        localStorage.setItem('exam_builder_class_filter', this.selectedClassFilter || 'all');
        localStorage.setItem('exam_builder_last_subject', this.selectedSubjectId);
        localStorage.setItem('exam_builder_print_layout', this.printLayoutMode);
      } catch (e) {
        console.warn('LocalStorage save error:', e);
      }
    },

    loadPersistedState() {
      try {
        const savedVisited = localStorage.getItem('exam_builder_visited');
        if (savedVisited) this.visitedSubjects = JSON.parse(savedVisited) || {};

        const savedSelections = localStorage.getItem('exam_builder_selections');
        if (savedSelections) this.selectionsBySubject = JSON.parse(savedSelections) || {};

        const savedMeta = localStorage.getItem('exam_builder_meta');
        if (savedMeta) {
          this.metaBySubject = JSON.parse(savedMeta) || {};
          Object.keys(this.metaBySubject).forEach(k => {
            if (this.metaBySubject[k] && this.metaBySubject[k].examTitle) {
              this.metaBySubject[k].examTitle = this.metaBySubject[k].examTitle.replace(/2025\s*[-–]\s*26/g, '2026 – 27');
            }
          });
        }
        if (this.customMeta.examTitle) {
          this.customMeta.examTitle = this.customMeta.examTitle.replace(/2025\s*[-–]\s*26/g, '2026 – 27');
        }

        const savedOrPairs = localStorage.getItem('exam_builder_orpairs');
        if (savedOrPairs) this.orPairsBySubject = JSON.parse(savedOrPairs) || {};

        const savedCustomMarks = localStorage.getItem('exam_builder_custom_marks');
        if (savedCustomMarks) this.customMarksBySubject = JSON.parse(savedCustomMarks) || {};

        const savedActiveSections = localStorage.getItem('exam_builder_active_sections');
        if (savedActiveSections) this.activeSectionBySubject = JSON.parse(savedActiveSections) || {};

        const savedChapterFilters = localStorage.getItem('exam_builder_chapter_filters');
        if (savedChapterFilters) this.chapterFilterBySubject = JSON.parse(savedChapterFilters) || {};

        const savedVariationFilters = localStorage.getItem('exam_builder_variation_filters');
        if (savedVariationFilters) this.variationFilterBySubject = JSON.parse(savedVariationFilters) || {};

        const savedClassFilter = localStorage.getItem('exam_builder_class_filter');
        if (savedClassFilter) this.selectedClassFilter = savedClassFilter;

        const savedLayout = localStorage.getItem('exam_builder_print_layout');
        if (savedLayout && ['standard', 'compact', 'twocolumn'].includes(savedLayout)) {
          this.printLayoutMode = savedLayout;
        }

        const lastSubject = localStorage.getItem('exam_builder_last_subject');
        if (lastSubject && this.subjectsList.some(s => s.id === lastSubject)) {
          this.selectedSubjectId = lastSubject;
          const bp = this.subjectsList.find(s => s.id === lastSubject);
          if (bp) this.currentBlueprint = bp;
        }
      } catch (e) {
        console.warn('Failed to load persisted state:', e);
      }
    },

    async init() {
      this.loadPersistedState();
      await this.loadQuestionsForSubject(this.selectedSubjectId);
      await this.fetchSavedPapers();

      const subId = this.selectedSubjectId;
      const hasStoredSelections = Array.isArray(this.selectionsBySubject[subId]);
      const hasBeenVisited = Boolean(this.visitedSubjects[subId]);

      if (hasStoredSelections || hasBeenVisited) {
        // Restore user's explicit selection even if empty array []
        this.selectedQuestionIds = hasStoredSelections ? [...this.selectionsBySubject[subId]] : [];
        if (this.metaBySubject[subId]) {
          this.customMeta = { ...this.customMeta, ...this.metaBySubject[subId] };
        }
        this.orPairs = this.orPairsBySubject[subId] ? { ...this.orPairsBySubject[subId] } : {};
        this.customMarks = this.customMarksBySubject[subId] ? { ...this.customMarksBySubject[subId] } : {};
        if (this.chapterFilterBySubject[subId]) this.chapterFilter = this.chapterFilterBySubject[subId];
        if (this.variationFilterBySubject[subId]) this.variationFilter = this.variationFilterBySubject[subId];
        if (this.activeSectionBySubject[subId]) {
          const secExists = (this.currentBlueprint.sections || []).some(s => s.key === this.activeSectionBySubject[subId]);
          if (secExists) this.activeSectionKey = this.activeSectionBySubject[subId];
        }
      } else {
        // First time ever visiting this subject: auto-fill Set A
        this.autoFillSet('Set A');
        this.visitedSubjects[subId] = true;
      }
      this.persistState();
    },

    async changeSubject(subjectId) {
      if (this.selectedSubjectId === subjectId) return;

      // 1. Save current state
      this.persistState();

      // 2. Switch subject
      this.selectedSubjectId = subjectId;
      const found = this.subjectsList.find(s => s.id === subjectId);
      if (found) {
        this.currentBlueprint = found;
      }

      // 3. Load question bank for target subject
      await this.loadQuestionsForSubject(subjectId);

      // 4. Restore state or initialize
      const hasStored = Array.isArray(this.selectionsBySubject[subjectId]);
      const hasVisited = Boolean(this.visitedSubjects[subjectId]);

      if (hasStored || hasVisited) {
        this.selectedQuestionIds = hasStored ? [...this.selectionsBySubject[subjectId]] : [];
        if (this.metaBySubject[subjectId]) {
          this.customMeta = { ...this.customMeta, ...this.metaBySubject[subjectId] };
        }
        this.orPairs = this.orPairsBySubject[subjectId] ? { ...this.orPairsBySubject[subjectId] } : {};
        this.customMarks = this.customMarksBySubject[subjectId] ? { ...this.customMarksBySubject[subjectId] } : {};
        this.chapterFilter = this.chapterFilterBySubject[subjectId] || 'all';
        this.variationFilter = this.variationFilterBySubject[subjectId] || 'all';
        if (this.activeSectionBySubject[subjectId]) {
          const exists = (this.currentBlueprint.sections || []).some(s => s.key === this.activeSectionBySubject[subjectId]);
          if (exists) this.activeSectionKey = this.activeSectionBySubject[subjectId];
        }
      } else {
        this.chapterFilter = 'all';
        this.variationFilter = 'all';
        this.autoFillSet('Set A');
        this.visitedSubjects[subjectId] = true;
      }

      // 5. Persist the switch
      this.persistState();
    },

    async loadQuestionsForSubject(subjectId) {
      try {
        const res = await fetch(`/api/questions/${subjectId}`);
        const data = await res.json();
        this.questions = data.questions || [];
        this.currentBlueprint = data.blueprint;
        if (this.currentBlueprint.sections && this.currentBlueprint.sections.length > 0) {
          const exists = this.currentBlueprint.sections.some(s => s.key === this.activeSectionKey);
          if (!exists) {
            this.activeSectionKey = this.currentBlueprint.sections[0].key;
          }
        }
      } catch (e) {
        console.error('Error loading questions:', e);
      }
    },

    getActiveSection() {
      if (!this.currentBlueprint.sections) return {};
      return this.currentBlueprint.sections.find(s => s.key === this.activeSectionKey) || this.currentBlueprint.sections[0] || {};
    },

    getAvailableChapters(subId) {
      const target = subId || (this.createQuestionModalOpen ? this.newQuestionSubjectId : this.selectedSubjectId);
      if (this.subjectChaptersCache && this.subjectChaptersCache[target] && this.subjectChaptersCache[target].length > 0) {
        return this.subjectChaptersCache[target];
      }
      const chs = new Set();
      this.questions.forEach(q => {
        if (q.chapter) chs.add(q.chapter);
      });
      return Array.from(chs).sort();
    },

    getFilteredQuestionsForActiveSection() {
      return this.questions.filter(q => {
        if (q.sectionKey !== this.activeSectionKey) return false;
        if (this.variationFilter !== 'all' && q.set !== this.variationFilter) return false;
        if (this.chapterFilter !== 'all' && q.chapter !== this.chapterFilter) return false;
        return true;
      });
    },

    getQuestionById(id) {
      return this.questions.find(q => q.id === id) || null;
    },

    getQuestionPreview(id) {
      const q = this.getQuestionById(id);
      if (!q) return id;
      if (q.preview) {
        return q.preview.length > 55 ? q.preview.substring(0, 52) + '...' : q.preview;
      }
      const clean = (q.content || '').replace(/[*_#`$]/g, '').trim();
      return clean.length > 55 ? clean.substring(0, 52) + '...' : clean;
    },

    isQuestionPairedAsPrimary(id) {
      return !!this.orPairs[id];
    },

    isQuestionPairedAsAlternative(id) {
      return Object.values(this.orPairs).includes(id);
    },

    getPrimaryQuestion(altId) {
      for (const [pri, alt] of Object.entries(this.orPairs)) {
        if (alt === altId) return this.getQuestionById(pri);
      }
      return null;
    },

    openPairingModal(primaryId) {
      this.pairingPrimaryQuestionId = primaryId;
      this.pairingChapterFilter = 'all';
      this.pairingModalOpen = true;
    },

    getOrCandidates() {
      if (!this.pairingPrimaryQuestionId) return [];
      const pri = this.getQuestionById(this.pairingPrimaryQuestionId);
      if (!pri) return [];

      return this.questions.filter(q => {
        if (q.id === this.pairingPrimaryQuestionId) return false;
        if (q.sectionKey !== pri.sectionKey && q.marks !== pri.marks) return false;
        if (this.isQuestionPairedAsAlternative(q.id) && this.orPairs[this.pairingPrimaryQuestionId] !== q.id) return false;
        if (this.pairingChapterFilter !== 'all' && q.chapter !== this.pairingChapterFilter) return false;
        return true;
      });
    },

    setOrPair(primaryId, altId) {
      if (!primaryId || !altId || primaryId === altId) return;

      delete this.orPairs[altId];
      for (const [k, v] of Object.entries(this.orPairs)) {
        if (v === altId) delete this.orPairs[k];
      }

      const altIdx = this.selectedQuestionIds.indexOf(altId);
      if (altIdx > -1) {
        this.selectedQuestionIds.splice(altIdx, 1);
      }

      this.orPairs[primaryId] = altId;
      this.pairingModalOpen = false;
      this.persistState();
      this.showToast('OR choice paired successfully!');
    },

    removeOrPair(primaryId) {
      if (this.orPairs[primaryId]) {
        delete this.orPairs[primaryId];
        this.persistState();
        this.showToast('OR pairing removed.');
      }
    },

    unlinkAsAlternative(altId) {
      for (const [k, v] of Object.entries(this.orPairs)) {
        if (v === altId) {
          delete this.orPairs[k];
        }
      }
      this.persistState();
      this.showToast('OR choice unlinked.');
    },

    toggleQuestion(id, sectionKey) {
      const idx = this.selectedQuestionIds.indexOf(id);
      if (idx > -1) {
        this.selectedQuestionIds.splice(idx, 1);
        if (this.orPairs[id]) {
          delete this.orPairs[id];
        }
      } else {
        if (this.isQuestionPairedAsAlternative(id)) {
          this.unlinkAsAlternative(id);
        }
        this.selectedQuestionIds.push(id);
      }
      this.persistState();
    },

    isQuestionSelected(id) {
      return this.selectedQuestionIds.includes(id);
    },

    getSectionSelectedCount(secKey) {
      return this.selectedQuestionIds.filter(id => {
        const q = this.questions.find(item => item.id === id);
        return q && q.sectionKey === secKey;
      }).length;
    },

    getQuestionMarks(id) {
      if (this.customMarks[id] !== undefined && this.customMarks[id] !== '') {
        return Number(this.customMarks[id]);
      }
      const q = this.getQuestionById(id);
      return q ? q.marks : 1;
    },

    setQuestionMarks(id, val) {
      const num = parseFloat(val);
      if (!isNaN(num) && num >= 0) {
        this.customMarks[id] = num;
      } else {
        delete this.customMarks[id];
      }
      this.persistState();
    },

    resetQuestionMarks(id) {
      delete this.customMarks[id];
      this.persistState();
      this.showToast('Reset to default marks.');
    },

    promptSetSectionMarks(secKey) {
      const sec = (this.currentBlueprint.sections || []).find(s => s.key === secKey);
      const currentDef = sec ? sec.marksEach : 1;
      const val = prompt(`Enter custom marks for ALL selected questions in Section ${secKey.replace('sec_', '').toUpperCase()}:`, currentDef);
      if (val === null) return;
      const num = parseFloat(val);
      if (isNaN(num) || num < 0) {
        alert('Please enter a valid positive number.');
        return;
      }
      this.setSectionAllMarks(secKey, num);
    },

    setSectionAllMarks(secKey, marks) {
      const secQuestions = this.selectedQuestionIds.filter(id => {
        const q = this.questions.find(item => item.id === id);
        return q && q.sectionKey === secKey;
      });
      secQuestions.forEach(id => {
        this.customMarks[id] = marks;
      });
      this.persistState();
      this.showToast(`Updated marks for ${secQuestions.length} question(s) in this section to ${marks}M.`);
    },

    getSectionTotalMarks(secKey) {
      let total = 0;
      const alternativeIds = new Set(Object.values(this.orPairs || {}));
      this.selectedQuestionIds.forEach(id => {
        if (alternativeIds.has(id)) return;
        const q = this.questions.find(item => item.id === id);
        if (q && q.sectionKey === secKey) {
          total += this.getQuestionMarks(id);
        }
      });
      return total;
    },

    getSectionShortTitle(sec) {
      if (!sec) return '';
      const secLetter = sec.key ? sec.key.replace('sec_', '').toUpperCase() : '';
      const sub = sec.subTitle ? sec.subTitle.split(' / ')[0] : (sec.title || '').replace(/###\s*/, '').split(' / ')[0];
      return `Sec ${secLetter}: ${sub}`;
    },

    getSectionBadgeClass(secKey) {
      const count = this.getSectionSelectedCount(secKey);
      if (count > 0) return 'bg-indigo-100 text-indigo-800 border border-indigo-200';
      return 'bg-slate-100 text-slate-500 border border-slate-200';
    },

    getSetBadgeClass(set) {
      if (set === 'Set A') return 'bg-emerald-100 text-emerald-800 border border-emerald-200';
      if (set === 'Set B') return 'bg-sky-100 text-sky-800 border border-sky-200';
      if (set === 'Set C') return 'bg-purple-100 text-purple-800 border border-purple-200';
      if (set === 'Textbook') return 'bg-teal-100 text-teal-800 border border-teal-300';
      if (set === 'Custom') return 'bg-rose-100 text-rose-800 border border-rose-300';
      return 'bg-amber-100 text-amber-800 border border-amber-300';
    },

    getTotalSelectedMarks() {
      let total = 0;
      const alternativeIds = new Set(Object.values(this.orPairs || {}));
      this.selectedQuestionIds.forEach(id => {
        if (alternativeIds.has(id)) return;
        total += this.getQuestionMarks(id);
      });
      return total;
    },

    calculateTotalMarks() {
      return this.getTotalSelectedMarks();
    },

    isPaperReady() {
      return this.selectedQuestionIds.length > 0;
    },

    isPaperComplete() {
      return this.selectedQuestionIds.length > 0;
    },

    selectSection(secKey) {
      this.activeSectionKey = secKey;
      if (this.selectedSubjectId) {
        this.activeSectionBySubject[this.selectedSubjectId] = secKey;
      }
      this.persistState();
    },

    persistFilterState() {
      if (this.selectedSubjectId) {
        this.chapterFilterBySubject[this.selectedSubjectId] = this.chapterFilter;
        this.variationFilterBySubject[this.selectedSubjectId] = this.variationFilter;
      }
      this.persistState();
    },

    getSectionPillClass(secKey) {
      const count = this.getSectionSelectedCount(secKey);
      if (count > 0) return 'bg-indigo-100 text-indigo-800 border border-indigo-200';
      return 'bg-slate-100 text-slate-500 border border-slate-200';
    },

    clearAllSelections() {
      if (this.selectedQuestionIds.length === 0) return;
      if (!confirm('Are you sure you want to clear all selected questions for this subject?')) return;
      this.selectedQuestionIds = [];
      this.orPairs = {};
      this.persistState();
      this.showToast('Cleared all selected questions.');
    },

    autoFillSet(setName) {
      this.selectedQuestionIds = [];
      this.orPairs = {};
      (this.currentBlueprint.sections || []).forEach(sec => {
        const matching = this.questions.filter(q => q.sectionKey === sec.key && q.set === setName && !q.id.endsWith('_alt'));
        matching.slice(0, sec.requiredCount).forEach(q => {
          this.selectedQuestionIds.push(q.id);
          if (q.defaultOrPartnerId && this.questions.some(x => x.id === q.defaultOrPartnerId)) {
            this.orPairs[q.id] = q.defaultOrPartnerId;
          }
        });
      });
      if (/^Set\s+[ABC]$/i.test(setName)) {
        const letter = setName.replace(/Set\s*/i, '').toUpperCase();
        this.customMeta.setName = `SET – ${letter}`;
      } else {
        this.customMeta.setName = '';
      }
      this.persistState();
      this.showToast(`Loaded ${setName} questions.`);
    },

    quickPickSection(secKey, setName) {
      const toRemove = this.selectedQuestionIds.filter(id => {
        const q = this.questions.find(item => item.id === id);
        return q && q.sectionKey === secKey;
      });
      toRemove.forEach(id => {
        delete this.orPairs[id];
      });
      this.selectedQuestionIds = this.selectedQuestionIds.filter(id => !toRemove.includes(id));

      const sec = (this.currentBlueprint.sections || []).find(s => s.key === secKey);
      if (sec) {
        const matching = this.questions.filter(q => q.sectionKey === secKey && q.set === setName && !q.id.endsWith('_alt'));
        matching.slice(0, sec.requiredCount).forEach(q => {
          this.selectedQuestionIds.push(q.id);
          if (q.defaultOrPartnerId && this.questions.some(x => x.id === q.defaultOrPartnerId)) {
            this.orPairs[q.id] = q.defaultOrPartnerId;
          }
        });
      }
      this.persistState();
      this.showToast(`Added ${sec ? sec.title : ''} questions from ${setName}.`);
    },

    clearActiveSection() {
      const toRemove = this.selectedQuestionIds.filter(id => {
        const q = this.questions.find(item => item.id === id);
        return q && q.sectionKey === this.activeSectionKey;
      });
      toRemove.forEach(id => {
        delete this.orPairs[id];
      });
      this.selectedQuestionIds = this.selectedQuestionIds.filter(id => !toRemove.includes(id));
      this.persistState();
    },

    randomizeSelection() {
      this.selectedQuestionIds = [];
      this.orPairs = {};
      (this.currentBlueprint.sections || []).forEach(sec => {
        const available = this.questions.filter(q => q.sectionKey === sec.key && !q.id.endsWith('_alt'));
        const shuffled = [...available].sort(() => 0.5 - Math.random());
        shuffled.slice(0, sec.requiredCount).forEach(q => {
          this.selectedQuestionIds.push(q.id);
          if (q.defaultOrPartnerId && this.questions.some(x => x.id === q.defaultOrPartnerId)) {
            this.orPairs[q.id] = q.defaultOrPartnerId;
          }
        });
      });
      this.customMeta.setName = '';
      this.persistState();
      this.showToast('Randomized mix of questions selected!');
    },

    formatMagicSquareTables(text) {
      if (!text) return '';
      const tableRegex = /\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|\r?\n\|\s*[-: ]+\s*\|\s*[-: ]+\s*\|\s*[-: ]+\s*\|\r?\n\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|\r?\n\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|/g;

      return text.replace(tableRegex, (match, r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3) => {
        const cleanCell = (cell) => {
          let c = (cell || '').trim();
          c = c.replace(/^\$|\$$/g, '').trim();
          if (c.includes('\\underline') || c.includes('hspace') || c.includes('___') || c === '' || c === '_' || c === '[ ]' || c === '[]') {
            return '<td class="blank-cell">&nbsp;</td>';
          }
          return `<td>${c}</td>`;
        };

        return `\n<table class="magic-square-table">\n  <tr>${cleanCell(r1c1)}${cleanCell(r1c2)}${cleanCell(r1c3)}</tr>\n  <tr>${cleanCell(r2c1)}${cleanCell(r2c2)}${cleanCell(r2c3)}</tr>\n  <tr>${cleanCell(r3c1)}${cleanCell(r3c2)}${cleanCell(r3c3)}</tr>\n</table>\n`;
      });
    },

    renderQuestionContent(markdown) {
      if (!markdown) return '';
      let cleaned = markdown.replace(/^\*\*(?:Q\d+\.|\([ivx]+\))\s*/, '');
      cleaned = cleaned.replace(/(_{2,})\s*\([^)\n]+\)/g, '$1');
      cleaned = cleaned.replace(/\([^)\n]+\)\s*(_{2,})/g, '$1');
      cleaned = cleaned.replace(/(_{2,}\s*[^.\n]*?)\s*\((?:जंग|दीर्घरोम|यशद लेपन|पारा|रूमेन|किशोरावस्था|कुचालक|चाल|समकोण|सममिति|द्विपद|एकपदी|त्रिपद)\)/g, '$1');
      cleaned = this.formatMagicSquareTables(cleaned);
      if (window.marked) {
        return marked.parse(cleaned);
      }
      return cleaned;
    },

    // ==========================================
    // Paper Saver Mode & Preview Controls
    // ==========================================
    setPrintLayoutMode(mode) {
      if (['standard', 'compact', 'twocolumn'].includes(mode)) {
        this.printLayoutMode = mode;
        this.persistState();
      }
    },

    async openPreview() {
      try {
        const res = await fetch('/api/generate-markdown', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            subjectId: this.selectedSubjectId,
            questionIds: this.selectedQuestionIds,
            customMeta: {
              ...this.customMeta,
              orPairs: this.orPairs,
              customMarks: this.customMarks,
              printLayoutMode: this.printLayoutMode
            }
          })
        });
        const data = await res.json();
        const md = data.markdown;
        this.previewModalOpen = true;

        this.$nextTick(() => {
          const el = document.getElementById('modal-paper-content');
          if (el && window.marked) {
            el.innerHTML = marked.parse(md);
            if (window.renderMathInElement) {
              renderMathInElement(el, {
                delimiters: [
                  { left: '$$', right: '$$', display: true },
                  { left: '$', right: '$', display: false }
                ],
                throwOnError: false
              });
            }
          }
        });
      } catch (e) {
        console.error('Error generating preview:', e);
      }
    },

    async downloadMarkdown() {
      try {
        const res = await fetch('/api/generate-markdown', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            subjectId: this.selectedSubjectId,
            questionIds: this.selectedQuestionIds,
            customMeta: { ...this.customMeta, orPairs: this.orPairs, customMarks: this.customMarks }
          })
        });
        const data = await res.json();
        const blob = new Blob([data.markdown], { type: 'text/markdown;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const safeName = (this.currentBlueprint.name || 'exam_paper').replace(/[^a-zA-Z0-9]/g, '_');
        const setSuffix = (this.customMeta.setName && !/^(mixed|custom|sample)/i.test(this.customMeta.setName))
          ? `_${this.customMeta.setName.replace(/[^a-zA-Z0-9]/g, '_')}`
          : '';
        const a = document.createElement('a');
        a.href = url;
        a.download = `${safeName}${setSuffix}.md`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        this.showToast('Markdown file downloaded!');
      } catch (e) {
        console.error('Download error:', e);
      }
    },

    async copyMarkdown() {
      try {
        const res = await fetch('/api/generate-markdown', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            subjectId: this.selectedSubjectId,
            questionIds: this.selectedQuestionIds,
            customMeta: { ...this.customMeta, orPairs: this.orPairs, customMarks: this.customMarks }
          })
        });
        const data = await res.json();
        await navigator.clipboard.writeText(data.markdown);
        this.showToast('Copied full Markdown to clipboard!');
      } catch (e) {
        console.error('Copy error:', e);
      }
    },

    printDirect() {
      const form = document.createElement('form');
      form.method = 'POST';
      form.action = '/print';
      form.target = '_blank';

      const sInput = document.createElement('input');
      sInput.type = 'hidden';
      sInput.name = 'subjectId';
      sInput.value = this.selectedSubjectId;
      form.appendChild(sInput);

      const qInput = document.createElement('input');
      qInput.type = 'hidden';
      qInput.name = 'questionIds';
      qInput.value = JSON.stringify(this.selectedQuestionIds);
      form.appendChild(qInput);

      const mInput = document.createElement('input');
      mInput.type = 'hidden';
      mInput.name = 'customMeta';
      mInput.value = JSON.stringify({
        ...this.customMeta,
        orPairs: this.orPairs,
        customMarks: this.customMarks,
        printLayoutMode: this.printLayoutMode
      });
      form.appendChild(mInput);

      document.body.appendChild(form);
      form.submit();
      document.body.removeChild(form);
    },

    async saveCurrentPaper() {
      const setStr = (this.customMeta.setName && !/^(mixed|custom|sample)/i.test(this.customMeta.setName)) ? ` - ${this.customMeta.setName}` : '';
      const defaultTitle = `${this.currentBlueprint.name}${setStr}`;
      const title = prompt('Enter a name for this paper configuration:', defaultTitle);
      if (!title) return;

      try {
        const res = await fetch('/api/save-paper', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            title,
            subjectId: this.selectedSubjectId,
            questionIds: this.selectedQuestionIds,
            customMeta: { ...this.customMeta, orPairs: this.orPairs, customMarks: this.customMarks }
          })
        });
        await res.json();
        this.showToast('Paper configuration saved!');
        this.fetchSavedPapers();
      } catch (e) {
        console.error('Save error:', e);
      }
    },

    async fetchSavedPapers() {
      try {
        const res = await fetch('/api/saved-papers');
        this.savedPapersList = await res.json();
        this.savedPapersCount = this.savedPapersList.length;
      } catch (e) {
        console.error(e);
      }
    },

    openSavedPapers() {
      this.fetchSavedPapers();
      this.savedPapersModalOpen = true;
    },

    async loadSavedPaper(item) {
      if (item.subjectId !== this.selectedSubjectId) {
        await this.changeSubject(item.subjectId);
      }
      this.selectedQuestionIds = item.questionIds || [];
      if (item.customMeta) {
        this.customMeta = { ...this.customMeta, ...item.customMeta };
        this.orPairs = item.customMeta.orPairs ? { ...item.customMeta.orPairs } : {};
        this.customMarks = item.customMeta.customMarks ? { ...item.customMeta.customMarks } : {};
      } else {
        this.orPairs = {};
        this.customMarks = {};
      }
      this.persistState();
      this.savedPapersModalOpen = false;
      this.showToast(`Loaded "${item.title}"`);
    },

    async deleteSavedPaper(id) {
      if (!confirm('Are you sure you want to delete this saved paper?')) return;
      try {
        await fetch(`/api/saved-papers/${id}`, { method: 'DELETE' });
        this.fetchSavedPapers();
        this.showToast('Paper deleted.');
      } catch (e) {
        console.error(e);
      }
    },

    // ==========================================
    // Class & Subject Hub Methods
    // ==========================================
    getUniqueClasses() {
      const set = new Set();
      (this.subjectsList || []).forEach(s => {
        if (s.class) set.add(String(s.class).trim());
      });
      return Array.from(set);
    },

    getSubjectCountForClass(cls) {
      return (this.subjectsList || []).filter(s => String(s.class).trim() === String(cls).trim()).length;
    },

    getFilteredSubjects() {
      if (this.selectedClassFilter === 'all') {
        return this.subjectsList || [];
      }
      return (this.subjectsList || []).filter(s => String(s.class).trim() === String(this.selectedClassFilter).trim());
    },

    setClassFilter(cls) {
      this.selectedClassFilter = cls;
      this.persistState();
    },

    openAddSubjectModal() {
      this.newSubClass = 'VIII';
      this.newSubId = '';
      this.newSubName = '';
      this.newSubSubject = '';
      this.newSubMaxMarks = 50;
      this.newSubTime = '2½ HOURS';
      this.newSubPattern = 'maths';
      this.addSubjectModalOpen = true;
    },

    async submitNewSubject() {
      if (!this.newSubClass || !this.newSubName || !this.newSubSubject) {
        alert('Please enter Class, Display Name, and Official Subject title.');
        return;
      }
      this.isSubmittingSubject = true;
      try {
        const payload = {
          id: this.newSubId ? this.newSubId.trim() : undefined,
          class: this.newSubClass.trim(),
          name: this.newSubName.trim(),
          subject: this.newSubSubject.trim(),
          maxMarks: this.newSubMaxMarks,
          time: this.newSubTime,
          pattern: this.newSubPattern
        };
        const res = await fetch('/api/subjects', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.success && data.subject) {
          const existingIdx = this.subjectsList.findIndex(s => s.id === data.subject.id);
          if (existingIdx !== -1) {
            this.subjectsList[existingIdx] = data.subject;
          } else {
            this.subjectsList.push(data.subject);
          }
          this.addSubjectModalOpen = false;
          this.selectedClassFilter = data.subject.class;
          await this.changeSubject(data.subject.id);
          this.showToast(`Subject "${data.subject.name}" added successfully!`);
        } else {
          alert(data.error || 'Failed to create subject.');
        }
      } catch (e) {
        console.error('Error creating subject:', e);
        alert('Error connecting to server.');
      } finally {
        this.isSubmittingSubject = false;
      }
    },

    // ==========================================
    // Custom Question Creator & Archetype Studio
    // ==========================================
    setArchetype(arch) {
      this.activeArchetype = arch;
      if (arch === 'la') {
        this.recalculateLaMarks();
      }
      this.updateCreateQuestionPreview();
    },

    detectArchetype(secKey, subId) {
      const sections = this.getSectionsForSubject(subId || this.newQuestionSubjectId);
      const sec = sections.find(s => s.key === secKey);
      if (!sec) return 'sa';

      const text = ((sec.title || '') + ' ' + (sec.subTitle || '')).toLowerCase();
      if (/tick|choice|mcq|बहुविकल्प/i.test(text) || secKey === 'sec_1' || secKey === 'sec_b') {
        return 'mcq';
      }
      if (/fill|blank|रिक्त/i.test(text) || secKey === 'sec_2') {
        return 'fib';
      }
      if (/true|false|सत्य|असत्य/i.test(text) || secKey === 'sec_3') {
        return 'tf';
      }
      if (/formula|definition|concept|मूल अवधारणा|सूत्र|परिभाषा/i.test(text) || secKey === 'sec_a') {
        return 'vsa';
      }
      if (/match|स्तंभ|मिलान/i.test(text)) {
        return 'match';
      }
      if (/long|दीर्घ|word problem|व्यावहारिक/i.test(text) || secKey === 'sec_e' || secKey === 'sec_6') {
        return 'la';
      }
      if (/short|लघु|calculation|गणना/i.test(text) || secKey === 'sec_d' || secKey === 'sec_5') {
        return 'sa';
      }
      return 'sa';
    },

    openCreateQuestionModal(defaultSectionKey) {
      this.isEditingQuestion = false;
      this.editingQuestionId = null;
      this.newQuestionSubjectId = this.selectedSubjectId;
      const currentSections = this.getSectionsForSubject(this.newQuestionSubjectId);
      this.newQuestionSectionKey = defaultSectionKey || (currentSections.length > 0 ? currentSections[0].key : '');
      this.newQuestionChapter = (this.chapterFilter !== 'all') ? this.chapterFilter : (this.getAvailableChapters()[0] || '');
      this.newQuestionCustomChapter = '';
      this.newQuestionMarks = this.getDefaultMarksForSection(this.newQuestionSubjectId, this.newQuestionSectionKey);
      this.newQuestionSet = 'Custom';
      this.activeArchetype = this.detectArchetype(this.newQuestionSectionKey, this.newQuestionSubjectId);
      this.newQuestionEnglish = '';
      this.newQuestionHindi = '';
      this.newQuestionMcqOptions = [
        { en: '', hi: '' },
        { en: '', hi: '' },
        { en: '', hi: '' },
        { en: '', hi: '' }
      ];
      this.newQuestionTfStyle = 'standard';
      this.newQuestionLaParts = [
        { part: 'a', en: '', hi: '', marks: 2 },
        { part: 'b', en: '', hi: '', marks: 2 }
      ];
      this.newQuestionMatchPromptEn = 'Match the items in Column I with Column II:';
      this.newQuestionMatchPromptHi = 'स्तंभ I के कथनों का स्तंभ II से सही मिलान कीजिए:';
      this.newQuestionMatchPairs = [
        { col1En: '', col1Hi: '', col2En: '', col2Hi: '' },
        { col1En: '', col1Hi: '', col2En: '', col2Hi: '' },
        { col1En: '', col1Hi: '', col2En: '', col2Hi: '' },
        { col1En: '', col1Hi: '', col2En: '', col2Hi: '' }
      ];
      this.newQuestionRawContent = '';
      this.newQuestionAutoSelect = true;
      if (this.activeArchetype === 'la') {
        this.recalculateLaMarks();
      }
      this.createQuestionModalOpen = true;
      this.$nextTick(() => {
        this.updateCreateQuestionPreview();
      });
    },

    openEditQuestionModal(q) {
      this.isEditingQuestion = true;
      this.editingQuestionId = q.id;
      this.newQuestionSubjectId = q.subjectId || this.selectedSubjectId;
      this.newQuestionSectionKey = q.sectionKey;
      this.newQuestionChapter = q.chapter || '';
      this.newQuestionCustomChapter = '';
      this.newQuestionMarks = this.getQuestionMarks(q.id);
      this.newQuestionSet = q.set || 'Custom';
      this.activeArchetype = 'raw';
      this.newQuestionRawContent = q.content || '';
      const lines = (q.content || '').split('\n').map(l => l.trim()).filter(Boolean);
      if (lines.length > 0) {
        this.newQuestionEnglish = lines[0].replace(/^\*\*|\*\*$/g, '');
        if (lines.length > 1 && !lines[1].startsWith('(') && !lines[1].startsWith('|')) {
          this.newQuestionHindi = lines[1].replace(/^\*\*|\*\*$/g, '');
        }
      }
      this.newQuestionAutoSelect = this.isQuestionSelected(q.id);
      this.createQuestionModalOpen = true;
      this.$nextTick(() => {
        this.updateCreateQuestionPreview();
      });
    },

    closeCreateQuestionModal() {
      this.createQuestionModalOpen = false;
      this.isEditingQuestion = false;
      this.editingQuestionId = null;
    },

    getSectionsForSubject(subId) {
      const bp = this.subjectsList.find(s => s.id === subId) || this.currentBlueprint;
      return bp ? (bp.sections || []) : [];
    },

    getDefaultMarksForSection(subId, secKey) {
      const sections = this.getSectionsForSubject(subId);
      const sec = sections.find(s => s.key === secKey);
      return sec ? (sec.marksEach || 1) : 1;
    },

    addMcqOption() {
      if (this.newQuestionMcqOptions.length >= 6) return;
      this.newQuestionMcqOptions.push({ en: '', hi: '' });
      this.updateCreateQuestionPreview();
    },

    removeMcqOption(idx) {
      if (this.newQuestionMcqOptions.length <= 2) return;
      this.newQuestionMcqOptions.splice(idx, 1);
      this.updateCreateQuestionPreview();
    },

    fillNumericOptions() {
      this.newQuestionMcqOptions = [
        { en: '1', hi: '1' },
        { en: '2', hi: '2' },
        { en: '3', hi: '3' },
        { en: '4', hi: '4' }
      ];
      this.updateCreateQuestionPreview();
    },

    applyPromptStarter(type) {
      const starters = {
        formula: { en: 'Write the formula to calculate: ', hi: 'निम्नलिखित को ज्ञात करने का सूत्र लिखिए: ' },
        definition: { en: 'Define the term: ', hi: 'निम्नलिखित पद की परिभाषा दीजिए: ' },
        si_unit: { en: 'State the SI unit and symbol of: ', hi: 'का SI मात्रक एवं संकेत लिखिए: ' },
        law: { en: 'State the law / principle of: ', hi: 'का नियम / सिद्धांत बताइए: ' },
        example: { en: 'Give two practical examples of: ', hi: 'के दो व्यावहारिक उदाहरण दीजिए: ' },
        solve: { en: 'Solve the following step by step: ', hi: 'निम्नलिखित को क्रमबद्ध हल कीजिए: ' },
        find_value: { en: 'Find the value of: ', hi: 'का मान ज्ञात कीजिए: ' },
        diff: { en: 'Differentiate between the following: ', hi: 'निम्नलिखित में अंतर स्पष्ट कीजिए: ' },
        reason: { en: 'Give reasons for the following: ', hi: 'निम्नलिखित के लिए कारण बताइए: ' },
        construction: { en: 'Construct / draw a neat sketch of: ', hi: 'स्वच्छ चित्र बनाइए / रचना कीजिए: ' }
      };
      const item = starters[type];
      if (!item) return;

      if (!this.newQuestionEnglish) {
        this.newQuestionEnglish = item.en;
      } else if (!this.newQuestionEnglish.startsWith(item.en)) {
        this.newQuestionEnglish = item.en + this.newQuestionEnglish;
      }

      if (!this.newQuestionHindi) {
        this.newQuestionHindi = item.hi;
      } else if (!this.newQuestionHindi.startsWith(item.hi)) {
        this.newQuestionHindi = item.hi + this.newQuestionHindi;
      }

      this.updateCreateQuestionPreview();
    },

    addLaPart() {
      const letters = ['a', 'b', 'c', 'd', 'e', 'f'];
      const nextLetter = letters[this.newQuestionLaParts.length] || String(this.newQuestionLaParts.length + 1);
      this.newQuestionLaParts.push({ part: nextLetter, en: '', hi: '', marks: 2 });
      this.recalculateLaMarks();
      this.updateCreateQuestionPreview();
    },

    removeLaPart(idx) {
      if (this.newQuestionLaParts.length <= 1) return;
      this.newQuestionLaParts.splice(idx, 1);
      this.recalculateLaMarks();
      this.updateCreateQuestionPreview();
    },

    recalculateLaMarks() {
      const total = this.newQuestionLaParts.reduce((sum, p) => sum + (Number(p.marks) || 0), 0);
      if (total > 0) {
        this.newQuestionMarks = total;
      }
    },

    addMatchPair() {
      if (this.newQuestionMatchPairs.length >= 6) return;
      this.newQuestionMatchPairs.push({ col1En: '', col1Hi: '', col2En: '', col2Hi: '' });
      this.updateCreateQuestionPreview();
    },

    removeMatchPair(idx) {
      if (this.newQuestionMatchPairs.length <= 2) return;
      this.newQuestionMatchPairs.splice(idx, 1);
      this.updateCreateQuestionPreview();
    },

    async onNewQuestionSubjectChange() {
      const sections = this.getSectionsForSubject(this.newQuestionSubjectId);
      if (sections.length > 0) {
        this.newQuestionSectionKey = sections[0].key;
        this.newQuestionMarks = sections[0].marksEach || 1;
        this.activeArchetype = this.detectArchetype(this.newQuestionSectionKey, this.newQuestionSubjectId);
      }
      this.newQuestionChapter = '';
      this.newQuestionCustomChapter = '';
      if (this.newQuestionSubjectId !== this.selectedSubjectId) {
        try {
          const res = await fetch(`/api/questions/${this.newQuestionSubjectId}`);
          const data = await res.json();
          const chs = new Set();
          (data.questions || []).forEach(q => { if (q.chapter) chs.add(q.chapter); });
          this.subjectChaptersCache = this.subjectChaptersCache || {};
          this.subjectChaptersCache[this.newQuestionSubjectId] = Array.from(chs).sort();
        } catch(e) {}
      }
      this.updateCreateQuestionPreview();
    },

    onNewQuestionSectionChange() {
      this.newQuestionMarks = this.getDefaultMarksForSection(this.newQuestionSubjectId, this.newQuestionSectionKey);
      this.activeArchetype = this.detectArchetype(this.newQuestionSectionKey, this.newQuestionSubjectId);
      if (this.activeArchetype === 'la') {
        this.recalculateLaMarks();
      }
      this.updateCreateQuestionPreview();
    },

    insertSymbolAtCursor(target, symbol) {
      let textarea;
      if (target === 'en') {
        textarea = document.getElementById('input-q-english-' + this.activeArchetype) || document.getElementById('input-q-english-mcq');
      } else if (target === 'hi') {
        textarea = document.getElementById('input-q-hindi-' + this.activeArchetype) || document.getElementById('input-q-hindi-mcq');
      } else {
        textarea = document.getElementById('input-q-raw');
      }
      if (!textarea) return;

      const start = textarea.selectionStart || 0;
      const end = textarea.selectionEnd || 0;
      const text = textarea.value;
      textarea.value = text.substring(0, start) + symbol + text.substring(end);

      if (target === 'en') {
        this.newQuestionEnglish = textarea.value;
      } else if (target === 'hi') {
        this.newQuestionHindi = textarea.value;
      } else {
        this.newQuestionRawContent = textarea.value;
      }

      textarea.dispatchEvent(new Event('input', { bubbles: true }));
      textarea.focus();
      const newPos = start + symbol.length;
      textarea.setSelectionRange(newPos, newPos);
      this.updateCreateQuestionPreview();
    },

    // Enhanced Math Symbol Insertion with LaTeX wrapping and Live Preview Sync
    insertMathSymbol(latexSnippet) {
      let textarea = null;
      if (this.activeArchetype === 'raw') {
        textarea = document.getElementById('input-q-raw');
      } else if (this.lastFocusedInputId) {
        textarea = document.getElementById(this.lastFocusedInputId);
      }
      
      if (!textarea) {
        textarea = document.getElementById('input-q-english-' + this.activeArchetype) ||
                   document.getElementById('input-q-english-mcq') ||
                   document.getElementById('input-q-raw');
      }
      if (!textarea) return;

      // Wrap in math delimiters if not already within $
      let insertText = latexSnippet;
      const start = textarea.selectionStart || 0;
      const end = textarea.selectionEnd || 0;
      const currentVal = textarea.value;

      // Check if we are already inside $...$
      const textBefore = currentVal.substring(0, start);
      const dollarCount = (textBefore.match(/\$/g) || []).length;
      const isInsideMath = dollarCount % 2 === 1;

      if (!isInsideMath) {
        insertText = `$${latexSnippet}$`;
      }

      textarea.value = currentVal.substring(0, start) + insertText + currentVal.substring(end);

      // Synchronize Alpine state directly
      if (textarea.id && textarea.id.includes('hindi')) {
        this.newQuestionHindi = textarea.value;
      } else if (textarea.id && textarea.id.includes('raw')) {
        this.newQuestionRawContent = textarea.value;
      } else {
        this.newQuestionEnglish = textarea.value;
      }

      // Notify Alpine of DOM value update
      textarea.dispatchEvent(new Event('input', { bubbles: true }));

      // Set cursor position right after insertion or inside braces if fraction
      textarea.focus();
      let newCursorPos = start + insertText.length;
      if (latexSnippet.includes('{a}')) {
        newCursorPos = start + insertText.indexOf('{a}') + 1;
      }
      textarea.setSelectionRange(newCursorPos, newCursorPos);

      // Force live preview update immediately
      this.updateCreateQuestionPreview();
    },

    getBuiltQuestionContent() {
      if (this.activeArchetype === 'raw') {
        return (this.newQuestionRawContent || '').trim();
      }

      const en = (this.newQuestionEnglish || '').trim();
      const hi = (this.newQuestionHindi || '').trim();

      // 1. MCQ
      if (this.activeArchetype === 'mcq') {
        let parts = [];
        if (en) parts.push(`**${en}**`);
        if (hi) parts.push(`**${hi}**`);
        const letters = ['a', 'b', 'c', 'd', 'e', 'f'];
        this.newQuestionMcqOptions.forEach((opt, idx) => {
          const optEn = (opt.en || '').trim();
          const optHi = (opt.hi || '').trim();
          if (optEn || optHi) {
            let optText = `(${letters[idx] || (idx + 1)}) `;
            if (optEn && optHi) {
              optText += `${optEn} / ${optHi}`;
            } else {
              optText += optEn || optHi;
            }
            parts.push(optText);
          }
        });
        return parts.join('  \n');
      }

      // 2. FIB
      if (this.activeArchetype === 'fib') {
        let parts = [];
        if (en) parts.push(`**${en}**`);
        if (hi) parts.push(`**${hi}**`);
        return parts.join('  \n');
      }

      // 3. TF
      if (this.activeArchetype === 'tf') {
        let parts = [];
        if (en) parts.push(`**${en}**`);
        if (hi) parts.push(`**${hi}**`);
        if (this.newQuestionTfStyle === 'standard') {
          parts.push('[ True / False ]  \n[ सत्य / असत्य ]');
        } else if (this.newQuestionTfStyle === 'with_reason') {
          parts.push('(State True/False with justification / सत्य अथवा असत्य लिखकर कारण बताइए)');
        } else if (this.newQuestionTfStyle === 'box') {
          parts.push('[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]');
        }
        return parts.join('  \n');
      }

      // 4. VSA
      if (this.activeArchetype === 'vsa') {
        let parts = [];
        if (en) parts.push(`**${en}**`);
        if (hi) parts.push(`**${hi}**`);
        return parts.join('  \n');
      }

      // 5. SA
      if (this.activeArchetype === 'sa') {
        let parts = [];
        if (en) parts.push(`**${en}**`);
        if (hi) parts.push(`**${hi}**`);
        return parts.join('  \n');
      }

      // 6. LA
      if (this.activeArchetype === 'la') {
        let parts = [];
        if (en) parts.push(`**${en}**`);
        if (hi) parts.push(`**${hi}**`);
        this.newQuestionLaParts.forEach(lp => {
          const pEn = (lp.en || '').trim();
          const pHi = (lp.hi || '').trim();
          const m = lp.marks ? ` [${lp.marks}M]` : '';
          if (pEn || pHi) {
            let line = `(${lp.part}) `;
            if (pEn && pHi) {
              line += `${pEn}${m}  \n     ${pHi}`;
            } else {
              line += `${pEn || pHi}${m}`;
            }
            parts.push(line);
          }
        });
        return parts.join('  \n');
      }

      // 7. Match
      if (this.activeArchetype === 'match') {
        let parts = [];
        const promptEn = (this.newQuestionMatchPromptEn || '').trim();
        const promptHi = (this.newQuestionMatchPromptHi || '').trim();
        if (promptEn) parts.push(`**${promptEn}**`);
        if (promptHi) parts.push(`**${promptHi}**`);
        parts.push('');
        parts.push('| Column I (स्तंभ I) | Column II (स्तंभ II) |');
        parts.push('| :--- | :--- |');
        const rom = ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)'];
        const col2Let = ['(A)', '(B)', '(C)', '(D)', '(E)', '(F)'];
        this.newQuestionMatchPairs.forEach((pair, idx) => {
          const c1 = `${rom[idx] || ''} ${(pair.col1En || '')}${pair.col1Hi ? ' / ' + pair.col1Hi : ''}`.trim();
          const c2 = `${col2Let[idx] || ''} ${(pair.col2En || '')}${pair.col2Hi ? ' / ' + pair.col2Hi : ''}`.trim();
          if (c1 || c2) {
            parts.push(`| ${c1} | ${c2} |`);
          }
        });
        return parts.join('  \n');
      }

      let parts = [];
      if (en) parts.push(`**${en}**`);
      if (hi) parts.push(`**${hi}**`);
      return parts.join('  \n');
    },

    updateCreateQuestionPreview() {
      const content = this.getBuiltQuestionContent();
      const el = document.getElementById('modal-create-q-preview');
      if (!el) return;

      if (!content) {
        el.innerHTML = '<span class="text-slate-400 italic text-xs">Preview will appear here in real time as you compose your question...</span>';
        return;
      }

      if (window.marked) {
        // Strip out answers in ()
        let clean = content.replace(/(_{2,})\s*\([^)\n]+\)/g, '$1');
        clean = clean.replace(/\([^)\n]+\)\s*(_{2,})/g, '$1');
        clean = this.formatMagicSquareTables(clean);
        el.innerHTML = marked.parse(clean);
        if (window.renderMathInElement) {
          renderMathInElement(el, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false }
            ],
            throwOnError: false
          });
        }
      } else {
        el.textContent = content;
      }
    },

    async saveCustomQuestion() {
      const content = this.getBuiltQuestionContent();
      if (!content) {
        alert('Please enter a question statement before saving.');
        return;
      }

      let finalChapter = this.newQuestionChapter;
      if (this.newQuestionChapter === '__custom__' || !finalChapter) {
        finalChapter = (this.newQuestionCustomChapter || '').trim() || 'General / Uncategorized';
      }

      const payload = {
        subjectId: this.newQuestionSubjectId,
        sectionKey: this.newQuestionSectionKey,
        chapter: finalChapter,
        marks: Number(this.newQuestionMarks) || 1,
        content: content,
        preview: (this.newQuestionEnglish || '').trim() || content.replace(/[*#]/g, '').trim().substring(0, 90) + '...',
        set: this.newQuestionSet || 'Custom'
      };

      this.isSavingCustomQuestion = true;
      try {
        let res, data;
        if (this.isEditingQuestion && this.editingQuestionId) {
          res = await fetch(`/api/questions/${this.newQuestionSubjectId}/${this.editingQuestionId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          data = await res.json();
          if (data.success && data.question) {
            const idx = this.questions.findIndex(q => q.id === this.editingQuestionId);
            if (idx !== -1) {
              this.questions[idx] = data.question;
            }
            this.persistState();
            this.showToast('Question updated successfully in question bank!');
          }
        } else {
          res = await fetch('/api/questions', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          data = await res.json();
          if (data.success && data.question) {
            if (this.newQuestionSubjectId === this.selectedSubjectId) {
              this.questions.push(data.question);
              if (this.newQuestionAutoSelect) {
                if (!this.selectedQuestionIds.includes(data.question.id)) {
                  this.selectedQuestionIds.push(data.question.id);
                }
              }
            } else {
              await this.changeSubject(this.newQuestionSubjectId);
              if (this.newQuestionAutoSelect && !this.selectedQuestionIds.includes(data.question.id)) {
                this.selectedQuestionIds.push(data.question.id);
              }
            }
            this.activeSectionKey = data.question.sectionKey;
            this.persistState();
            this.showToast('New question created and saved to question bank!');
          }
        }
        this.closeCreateQuestionModal();
      } catch (err) {
        console.error('Error saving custom question:', err);
        alert('Failed to save question. Please check server logs.');
      } finally {
        this.isSavingCustomQuestion = false;
      }
    },

    async deleteCustomQuestion(qId) {
      if (!confirm('Are you sure you want to permanently delete this custom question from the question bank?')) {
        return;
      }
      try {
        const res = await fetch(`/api/questions/${this.selectedSubjectId}/${qId}`, {
          method: 'DELETE'
        });
        const data = await res.json();
        if (data.success) {
          this.questions = this.questions.filter(q => q.id !== qId);
          this.selectedQuestionIds = this.selectedQuestionIds.filter(id => id !== qId);
          if (this.orPairs[qId]) delete this.orPairs[qId];
          if (this.customMarks[qId]) delete this.customMarks[qId];
          this.persistState();
          this.showToast('Question deleted from bank.');
        }
      } catch (err) {
        console.error('Error deleting question:', err);
        alert('Failed to delete question.');
      }
    },

    getSubjectName(sid) {
      const found = this.subjectsList.find(s => s.id === sid);
      return found ? found.name : sid;
    },

    showToast(msg) {
      this.toastMessage = msg;
      setTimeout(() => {
        if (this.toastMessage === msg) this.toastMessage = '';
      }, 3000);
    }
  };
}

// Global auto-render math listener
document.addEventListener('DOMContentLoaded', () => {
  const renderAllMath = () => {
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  };
  setTimeout(renderAllMath, 400);
  setInterval(renderAllMath, 2500);
});

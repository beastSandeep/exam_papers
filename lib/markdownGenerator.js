/**
 * Exam Paper Markdown & HTML Generator
 */

function formatMagicSquareTables(text) {
  if (!text) return '';

  // Match 3x3 table markdown pattern
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
}

function sanitizeQuestionBody(text) {
  let cleaned = (text || '').trim().replace(/^\*\*(?:Q\d+\.|\([ivx]+\))\s*/, '');
  if (!cleaned.startsWith('**') && !cleaned.startsWith('#') && !cleaned.startsWith('|') && !cleaned.startsWith('<')) {
    cleaned = `**${cleaned}`;
  }

  // Strip answers in () for fill in the blanks
  cleaned = cleaned.replace(/(_{2,})\s*\([^)\n]+\)/g, '$1');
  cleaned = cleaned.replace(/\([^)\n]+\)\s*(_{2,})/g, '$1');
  cleaned = cleaned.replace(/(_{2,}\s*[^.\n]*?)\s*\((?:जंग|दीर्घरोम|यशद लेपन|पारा|रूमेन|किशोरावस्था|कुचालक|चाल|समकोण|सममिति|द्विपद|एकपदी|त्रिपद)\)/g, '$1');

  // Convert magic square markdown tables to crisp grid table
  cleaned = formatMagicSquareTables(cleaned);

  return cleaned;
}

function generateMarkdown(blueprint, selectedQuestions = [], customMeta = {}, allQuestions = []) {
  const schoolName =
    customMeta.schoolName ||
    blueprint.schoolName ||
    "NEW M.V.M. SENIOR SECONDARY SCHOOL, ALWAR";
  const examTitle =
    customMeta.examTitle ||
    blueprint.examTitle ||
    "HALF YEARLY EXAMINATION: 2026 – 27";

  // Only include official set codes (e.g. SET – A, SET – B, SET – C)
  // Strictly omit developer / internal details like (MIXED SET), (CUSTOM SET), (Sample Paper)
  let setNameStr = "";
  if (customMeta.setName && typeof customMeta.setName === "string") {
    const trimmed = customMeta.setName.trim();
    const isDevDetail = /^(mixed set|custom set|sample paper|sample|drill|custom|all|none|undefined)$/i.test(trimmed);
    if (!isDevDetail && trimmed.length > 0) {
      if (/^set\s*[a-z0-9]$/i.test(trimmed)) {
        const letter = trimmed.replace(/set\s*/i, "").toUpperCase();
        setNameStr = ` (SET – ${letter})`;
      } else {
        setNameStr = ` (${trimmed})`;
      }
    }
  }

  // Question map and custom marks
  const qMap = new Map();
  if (Array.isArray(allQuestions)) {
    allQuestions.forEach((q) => qMap.set(q.id, q));
  }
  selectedQuestions.forEach((q) => qMap.set(q.id, q));

  const customMarks = customMeta.customMarks || {};
  const getQMarks = (q) => {
    if (customMarks[q.id] !== undefined && customMarks[q.id] !== "") {
      return Number(customMarks[q.id]);
    }
    return q.marks !== undefined ? q.marks : 1;
  };

  const orPairs = customMeta.orPairs || {};
  const orPartnerIds = new Set(Object.values(orPairs));

  // Primary questions exclude any questions acting as an alternative partner
  const primaryQuestions = selectedQuestions.filter(
    (q) => !orPartnerIds.has(q.id),
  );

  const className = customMeta.className || blueprint.class;
  const subjectName = customMeta.subjectName || blueprint.subject;
  const timeAllowed = customMeta.time || blueprint.time || "2½ HOURS";

  // Calculate dynamic maximum marks
  const computedTotalMarks = primaryQuestions.reduce((sum, q) => sum + getQMarks(q), 0);
  const maxMarks = customMeta.maxMarks
    ? customMeta.maxMarks
    : (computedTotalMarks > 0 ? computedTotalMarks : (blueprint.maxMarks || 50));

  let md = [];

  // Header
  md.push(`# ${schoolName}`);
  md.push("");
  md.push(`## ${examTitle}${setNameStr}`);
  md.push("");
  md.push(`**CLASS : ${className}**  `);
  md.push(`**SUBJECT : ${subjectName}**  `);
  md.push(`**TIME : ${timeAllowed}**  `);
  md.push(`**MAXIMUM MARKS (पूर्णांक) : ${maxMarks}**`);
  md.push("");
  md.push("---");
  md.push("");

  // General Instructions (Optional)
  if (customMeta.includeInstructions !== false && customMeta.showInstructions !== false) {
    md.push("### GENERAL INSTRUCTIONS / सामान्य निर्देश");
    md.push("");
    md.push("1. All questions are compulsory. / सभी प्रश्न अनिवार्य हैं।");

    if (blueprint.isScience) {
      md.push(
        "2. The question paper comprises sections with indicated marks against each. / प्रश्न पत्र में प्रत्येक प्रश्न के अंक उसके सम्मुख अंकित हैं।",
      );
      md.push(
        "3. The paper is bilingual (English and Hindi). / यह प्रश्न पत्र द्विभाषी (अंग्रेजी और हिन्दी) है।",
      );
    } else {
      md.push(
        "2. Section-wise question count and marks distribution: / खंडवार प्रश्न संख्या एवं अंक विभाजन:",
      );
      blueprint.sections.forEach(sec => {
        const secLetter = sec.key.replace("sec_", "").toUpperCase();
        const hindiLetter = { 'A': 'क', 'B': 'ख', 'C': 'ग', 'D': 'घ', 'E': 'ङ' }[secLetter] || secLetter;
        const sub = sec.subTitle || "";
        const parts = sub.split(" / ");
        const engSub = parts[0] || sub;
        const hinSub = parts[1] || "";

        const secQuestions = primaryQuestions.filter(q => q.sectionKey === sec.key);
        if (secQuestions.length === 0) return;
        const secTotalMarks = secQuestions.reduce((sum, q) => sum + getQMarks(q), 0);
        const count = secQuestions.length;
        const allSame = secQuestions.every(q => getQMarks(q) === getQMarks(secQuestions[0]));

        if (allSame) {
          const marksEach = getQMarks(secQuestions[0]);
          md.push(`   - **Section ${secLetter}**: ${count} ${engSub} of ${marksEach} mark${marksEach > 1 ? "s" : ""} each (${secTotalMarks} Marks).  `);
          if (hinSub) {
            md.push(`     **खंड '${hindiLetter}'**: ${count} ${hinSub}, प्रत्येक ${marksEach} अंक का (${secTotalMarks} अंक)।`);
          }
        } else {
          md.push(`   - **Section ${secLetter}**: ${count} ${engSub} (${secTotalMarks} Marks).  `);
          if (hinSub) {
            md.push(`     **खंड '${hindiLetter}'**: ${count} ${hinSub} (${secTotalMarks} अंक)।`);
          }
        }
      });
      if (Object.keys(orPairs).length > 0) {
        md.push(
          "3. Internal choice has been provided in questions where indicated. / जिन प्रश्नों में विकल्प दिए गए हैं, उनमें से किसी एक को हल करें।",
        );
      }
      md.push(
        "4. Use of calculators is strictly prohibited. / कैलकुलेटर का उपयोग पूर्णतः वर्जित है।",
      );
    }
    md.push("");
    md.push("---");
    md.push("");
  }

  // Sections
  let overallMathQIndex = 1;
  const romanNumbers = [
    "(i)",
    "(ii)",
    "(iii)",
    "(iv)",
    "(v)",
    "(vi)",
    "(vii)",
    "(viii)",
    "(ix)",
    "(x)",
    "(xi)",
    "(xii)",
    "(xiii)",
    "(xiv)",
    "(xv)"
  ];

  blueprint.sections.forEach((sec, sIdx) => {
    const secQuestions = primaryQuestions.filter(
      (q) => q.sectionKey === sec.key,
    );
    if (secQuestions.length === 0) return;

    md.push(sec.title);
    md.push("");
    if (sec.subTitle) {
      md.push(`#### ${sec.subTitle}`);
      md.push("");
    }

    const count = secQuestions.length;
    const secTotalMarks = secQuestions.reduce((sum, q) => sum + getQMarks(q), 0);
    const allSame = secQuestions.every(q => getQMarks(q) === getQMarks(secQuestions[0]));

    if (allSame) {
      const marksEach = getQMarks(secQuestions[0]);
      md.push(`**(${count} × ${marksEach} = ${secTotalMarks} Marks)**`);
    } else {
      md.push(`**(${count} Questions, Total: ${secTotalMarks} Marks)**`);
    }
    md.push("");

    secQuestions.forEach((q, qIdx) => {
      let content = q.content.trim();
      let qNumStr = "";

      if (blueprint.isScience) {
        qNumStr = romanNumbers[qIdx] || `(${qIdx + 1})`;
      } else {
        qNumStr = `Q${overallMathQIndex}.`;
        overallMathQIndex++;
      }

      // Clean out existing Q prefix from question body and strip answers in () for fill in the blanks
      let bodyContent = sanitizeQuestionBody(content);

      // Check if custom mark is different from section default
      const thisQMark = getQMarks(q);
      const isCustomMark = customMarks[q.id] !== undefined;

      // Question container with two columns: left = number, right = indented body
      md.push(`<div class="question-item" style="display: flex; align-items: flex-start; margin-bottom: 1.15rem;">`);
      md.push(`<span class="question-num" style="font-weight: 800; min-width: 2.85rem; max-width: 3.5rem; flex-shrink: 0; padding-top: 0.05rem;">${qNumStr}</span>`);
      md.push(`<div class="question-body" style="flex: 1 1 0%; min-width: 0;">`);
      md.push("");
      md.push(bodyContent);
      md.push("");
      md.push(`</div>`);
      md.push(`</div>`);
      md.push("");

      // Alternative Question
      const altId = orPairs[q.id];
      if (altId && qMap.has(altId)) {
        const altQ = qMap.get(altId);
        let altBody = sanitizeQuestionBody(altQ.content);

        // Horizontally centered OR divider
        md.push('<div align="center" class="or-divider" style="text-align: center; font-weight: bold; margin: 16px auto; letter-spacing: 0.06em; display: block; width: 100%;"><strong>OR / अथवा</strong></div>');
        md.push("");

        // Indented alternative question matching the primary body indentation
        md.push(`<div class="question-item" style="display: flex; align-items: flex-start; margin-bottom: 1.15rem;">`);
        md.push(`<span class="question-num" style="min-width: 2.85rem; max-width: 3.5rem; flex-shrink: 0;"></span>`);
        md.push(`<div class="question-body" style="flex: 1 1 0%; min-width: 0;">`);
        md.push("");
        md.push(altBody);
        md.push("");
        md.push(`</div>`);
        md.push(`</div>`);
        md.push("");
      }
    });

    if (sIdx < blueprint.sections.length - 1) {
      md.push("---");
      md.push("");
    }
  });

  return md.join("\n");
}

module.exports = { generateMarkdown };

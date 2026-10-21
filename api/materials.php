const state = {
  allSubjects: [],
  filters: {
    stream: 'all',
    search: '',
  },
};

const subjectList = document.getElementById('subjectList');
const streamFilter = document.getElementById('streamFilter');
const searchInput = document.getElementById('searchInput');
const studyStream = document.getElementById('studyStream');
const studyHours = document.getElementById('studyHours');
const studyPlanOutput = document.getElementById('studyPlanOutput');
const resourceList = document.getElementById('resourceList');
const subjectTemplate = document.getElementById('subjectTemplate');

async function loadData() {
  try {
    const response = await fetch('api/materials.php');
    if (!response.ok) {
      throw new Error('Failed to load data from API');
    }

    const json = await response.json();
    state.allSubjects = json.subjects || [];
    renderStreamOptions(json.streams || []);
    renderSubjects();
    renderResources(json.resources || []);
    updateStats(json);
  } catch (error) {
    subjectList.innerHTML = '<div class="empty-state">The subject data could not be loaded. Please ensure the PHP API is available.</div>';
    console.error(error);
  }
}

function updateStats(json) {
  const totalSubjects = json.subjects?.length || 0;
  const streamCount = json.streams?.length || 0;
  const topicCount = json.subjects?.reduce((sum, subject) => sum + (subject.units?.length || 0), 0) || 0;

  document.getElementById('stat-total-subjects').textContent = totalSubjects;
  document.getElementById('stat-streams').textContent = streamCount;
  document.getElementById('stat-topics').textContent = topicCount;
}

function renderStreamOptions(streams) {
  const options = ['<option value="all">All streams</option>'];
  streams.forEach((stream) => {
    options.push(`<option value="${stream.value}">${stream.label}</option>`);
  });

  streamFilter.innerHTML = options.join('');
  studyStream.innerHTML = `<option value="all">All</option>${streams
    .map((stream) => `<option value="${stream.value}">${stream.label}</option>`)
    .join('')}`;
}

function renderSubjects() {
  const filtered = state.allSubjects.filter((subject) => {
    const streamMatches = state.filters.stream === 'all' || subject.stream === state.filters.stream;
    const searchText = state.filters.search.trim().toLowerCase();
    const searchMatches =
      !searchText ||
      subject.name.toLowerCase().includes(searchText) ||
      subject.description.toLowerCase().includes(searchText) ||
      subject.units.some((unit) => unit.title.toLowerCase().includes(searchText));

    return streamMatches && searchMatches;
  });

  if (!filtered.length) {
    subjectList.innerHTML = '<div class="empty-state">No matching subjects or topics were found. Try a different search or stream filter.</div>';
    return;
  }

  subjectList.innerHTML = '';

  filtered.forEach((subject) => {
    const fragment = subjectTemplate.content.cloneNode(true);
    const article = fragment.querySelector('.subject-card');
    const stream = fragment.querySelector('.subject-stream');
    const title = fragment.querySelector('.subject-title');
    const description = fragment.querySelector('.subject-description');
    const focusList = fragment.querySelector('.focus-list');
    const unitPreview = fragment.querySelector('.unit-preview');

    stream.textContent = subject.streamLabel;
    title.textContent = subject.name;
    description.textContent = subject.description;

    subject.objectives.forEach((objective) => {
      const li = document.createElement('li');
      li.textContent = objective;
      focusList.appendChild(li);
    });

    const firstTwoUnits = subject.units.slice(0, 2);
    const unitHtml = document.createElement('div');
    const heading = document.createElement('h5');
    heading.textContent = 'Core teaching units';
    unitHtml.appendChild(heading);

    const unitList = document.createElement('ul');
    firstTwoUnits.forEach((unit) => {
      const li = document.createElement('li');
      li.textContent = unit.title;
      unitList.appendChild(li);
    });

    unitHtml.appendChild(unitList);
    unitPreview.appendChild(unitHtml);

    article.dataset.subject = subject.slug;
    subjectList.appendChild(fragment);
  });
}

function renderResources(resources) {
  if (!resources.length) {
    resourceList.innerHTML = '<div class="empty-state">No learning resources are available yet for this curriculum view.</div>';
    return;
  }

  resourceList.innerHTML = resources
    .map(
      (resource) => `
        <div class="resource-item">
          <h4>${resource.title}</h4>
          <p>${resource.description}</p>
        </div>
      `
    )
    .join('');
}

function generatePlan() {
  const selectedStream = studyStream.value;
  const hours = Number(studyHours.value) || 3;
  const relevantSubjects = state.allSubjects.filter((subject) => {
    if (selectedStream === 'all') return true;
    return subject.stream === selectedStream;
  });

  if (!relevantSubjects.length) {
    studyPlanOutput.innerHTML = '<p class="empty-state">No subject data is available for the selected stream.</p>';
    return;
  }

  const plan = [
    `Day 1: Review the conceptual foundations of ${relevantSubjects[0].name}. Study for ${hours} hours and complete one detailed summary.` ,
    `Day 2: Work on ${relevantSubjects[Math.min(1, relevantSubjects.length - 1)].name} by comparing examples, definitions, and short-answer practice.`,
    `Day 3: Analyze a major unit from ${relevantSubjects[Math.min(2, relevantSubjects.length - 1)].name} and write explanations in your own words.`,
    `Day 4: Complete timed practice questions and review errors for the chosen stream using official-style tasks and explanations.`,
    `Day 5: Consolidate your notes and create a concept map linking key ideas, definitions, and exam techniques.`,
    `Day 6: Focus on the most difficult subject by practicing short response and extended response questions.`,
    `Day 7: Full revision and self-assessment cycle: revisit weak areas and refresh your summary sheets.`,
  ];

  studyPlanOutput.innerHTML = `<ul class="study-plan">${plan.map((item) => `<li>${item}</li>`).join('')}</ul>`;
}

streamFilter.addEventListener('change', (event) => {
  state.filters.stream = event.target.value;
  renderSubjects();
});

searchInput.addEventListener('input', (event) => {
  state.filters.search = event.target.value;
  renderSubjects();
});

document.getElementById('generatePlanBtn').addEventListener('click', generatePlan);

loadData();

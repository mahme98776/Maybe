from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data'


def build_dataset():
    dataset = {
        'year': 2027,
        'updated': '2026-10-21',
        'streams': [
            {'value': 'science', 'label': 'Science'},
            {'value': 'literary', 'label': 'Literary'},
            {'value': 'commercial', 'label': 'Commercial'},
        ],
        'resources': [
            {
                'title': 'Concept-based learning',
                'description': 'Each lesson emphasizes understanding, distinctions, and application instead of isolated memorization.',
            },
            {
                'title': 'Assessment preparation',
                'description': 'Students are guided toward question analysis, expected answer structure, and typical exam language.',
            },
            {
                'title': 'Revision strategy',
                'description': 'The system recommends regular review loops, concept maps, and focused practice across the weakest units.',
            },
            {
                'title': 'Skill integration',
                'description': 'Reading, writing, scientific reasoning, and data interpretation are connected to every study cycle.',
            },
        ],
        'subjects': [
            {
                'slug': 'arabic-language',
                'name': 'Arabic Language',
                'stream': 'literary',
                'streamLabel': 'Literary',
                'description': 'Arabic Language develops expression, analytical reading, grammar, and literary appreciation. Students learn how to interpret texts accurately and write in a clear, disciplined academic style.',
                'objectives': [
                    'Understand meaning, style, and rhetorical intent in literary and non-literary texts.',
                    'Apply grammar and morphology in context rather than in isolated drills.',
                    'Prepare organized argumentative writing and response-based answers.',
                    'Develop close reading skills suitable for official exam-style questions.',
                ],
                'units': [
                    {'title': 'Text analysis and rhetoric'},
                    {'title': 'Grammar and sentence structure'},
                    {'title': 'Composition and writing style'},
                ],
            },
            {
                'slug': 'english-language',
                'name': 'English Language',
                'stream': 'science',
                'streamLabel': 'Science',
                'description': 'English is taught through reading comprehension, vocabulary development, grammar, and writing. It strengthens communication, interpretation, and formal reasoning across academic contexts.',
                'objectives': [
                    'Interpret reading passages critically and summarize key ideas accurately.',
                    'Use grammar and vocabulary in meaningful sentences and paragraphs.',
                    'Respond to exam writing tasks with coherence, precision, and structure.',
                    'Apply language skills in academic and practical contexts.',
                ],
                'units': [
                    {'title': 'Reading comprehension and inference'},
                    {'title': 'Grammar and sentence transformation'},
                    {'title': 'Writing and structured responses'},
                ],
            },
            {
                'slug': 'mathematics',
                'name': 'Mathematics',
                'stream': 'science',
                'streamLabel': 'Science',
                'description': 'Mathematics develops logical reasoning, abstraction, and symbolic comprehension. Students work through algebra, geometry, functions, and problem-solving models that require precision and explanation.',
                'objectives': [
                    'Understand mathematical ideas using definitions, proofs, and examples.',
                    'Solve analytical problems with clear steps and justification.',
                    'Connect algebraic and geometric reasoning across topics.',
                    'Use conceptual understanding to handle unfamiliar exam questions.',
                ],
                'units': [
                    {'title': 'Functions and graph interpretation'},
                    {'title': 'Algebraic manipulation'},
                    {'title': 'Geometry and trigonometry'},
                ],
            },
            {
                'slug': 'physics',
                'name': 'Physics',
                'stream': 'science',
                'streamLabel': 'Science',
                'description': 'Physics explains natural phenomena through models, laws, experiments, and calculations. Learners are expected to connect scientific theory with observation and quantitative reasoning.',
                'objectives': [
                    'Explain laws and principles with mathematical and verbal justification.',
                    'Interpret graphs and experimental data with precision.',
                    'Solve numerical problems by selecting correct formulas and units.',
                    'Relate scientific concepts to everyday physical systems.',
                ],
                'units': [
                    {'title': 'Motion and force'},
                    {'title': 'Energy and work'},
                    {'title': 'Electricity and circuits'},
                ],
            },
            {
                'slug': 'biology',
                'name': 'Biology',
                'stream': 'science',
                'streamLabel': 'Science',
                'description': 'Biology focuses on living systems, structure, function, and interaction. The subject promotes scientific understanding and accurate description of biological processes and systems.',
                'objectives': [
                    'Understand cell biology and organism function in context.',
                    'Analyze physiological processes and biological adaptations.',
                    'Interpret diagrams, experiments, and classification systems.',
                    'Use precise scientific vocabulary in explanations.',
                ],
                'units': [
                    {'title': 'Cell structure and life processes'},
                    {'title': 'Genetics and inheritance'},
                    {'title': 'Human systems and homeostasis'},
                ],
            },
            {
                'slug': 'history',
                'name': 'History',
                'stream': 'literary',
                'streamLabel': 'Literary',
                'description': 'History teaches learners to evaluate turning points, social change, and the relationship between events and human development. Students practice chronological understanding and evidence-based interpretation.',
                'objectives': [
                    'Trace major historical developments and conditions of change.',
                    'Use evidence and chronology when writing analytical answers.',
                    'Compare social, political, and cultural developments across periods.',
                    'Generate balanced arguments based on historical sources.',
                ],
                'units': [
                    {'title': 'Ancient civilizations and their legacies'},
                    {'title': 'Modern Arab and world history'},
                    {'title': 'Revolution, reform, and national identity'},
                ],
            },
            {
                'slug': 'economics',
                'name': 'Economics and Commerce',
                'stream': 'commercial',
                'streamLabel': 'Commercial',
                'description': 'Economics and Commerce develop understanding of markets, financial decision-making, production, and business systems. Students study how economic patterns shape institutions and daily life.',
                'objectives': [
                    'Explain the main economic principles behind supply, demand, and production.',
                    'Analyze commercial behavior and market structures.',
                    'Use graphs and numerical data to support economic interpretation.',
                    'Link business activity to practical decision-making scenarios.',
                ],
                'units': [
                    {'title': 'Supply, demand, and market equilibrium'},
                    {'title': 'Business organization and finance'},
                    {'title': 'Trade, income, and economic policy'},
                ],
            },
            {
                'slug': 'geography',
                'name': 'Geography',
                'stream': 'literary',
                'streamLabel': 'Literary',
                'description': 'Geography links physical space, human activity, and environmental change. It teaches spatial understanding and analysis of natural systems, populations, and economic geography.',
                'objectives': [
                    'Interpret maps, charts, and spatial patterns meaningfully.',
                    'Analyze human interaction with the environment.',
                    'Relate geographic features to social and economic outcomes.',
                    'Offer explanations supported by evidence and location-based reasoning.',
                ],
                'units': [
                    {'title': 'Natural landscapes and climate'},
                    {'title': 'Population and urban development'},
                    {'title': 'Resource use and sustainability'},
                ],
            },
        ],
    }

    DATA_DIR.mkdir(exist_ok=True)
    (DATA_DIR / 'egyptian_bacc_2027.json').write_text(json.dumps(dataset, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Generated data/egyptian_bacc_2027.json')


if __name__ == '__main__':
    build_dataset()

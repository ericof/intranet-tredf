// Schema do Bloco

export const blockSchema = (props) => {
  const availableMeasures = [
    ['sunrise', 'Nascer do Sol'],
    ['sunset', 'Por do Sol'],
  ];
  const defaultMeasure = 'sunset';
  return {
    title: 'Clima',
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['location', 'measure'],
      },
      {
        id: 'dados',
        title: 'Dados de exemplo',
        fields: ['weather'],
      },
    ],
    properties: {
      location: {
        title: 'Local',
        description: 'Local a exibir',
        widget: 'text',
      },
      weather: {
        title: 'Clima',
        description: 'Condição climática padrão',
        default: 'sun',
        widget: 'text',
      },
      measure: {
        title: 'Medida',
        description: 'O que exibir no bloco',
        choices: availableMeasures,
        default: defaultMeasure,
      },
    },
    required: ['location', 'measure'],
  };
};

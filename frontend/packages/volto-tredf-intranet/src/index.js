import AreaView from './components/Views/AreaView';
import PessoaView from './components/Views/PessoaView';
// Blocos
import AreaGridItem from './components/Blocks/Grid/AreaGridItem';
import PessoaGridItem from './components/Blocks/Grid/PessoaGridItem';

const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br'];
  config.settings.defaultLanguage = 'pt-br';
  config.settings.image_crop_aspect_ratios = [
    {
      label: '16:9',
      ratio: 16 / 9,
    },
    {
      label: '4:3',
      ratio: 4 / 3,
    },
    {
      label: '1:1',
      ratio: 1,
    },
  ];
  // Registra Visoes padrao para tipos de conteúdo
  config.views.contentTypesViews = {
    Area: AreaView,
    Pessoa: PessoaView,
    ...config.views.contentTypesViews,
  };

  // Blocos
  /// Grid
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: AreaGridItem,
    dependencies: 'Area',
  });
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: PessoaGridItem,
    dependencies: 'Pessoa',
  });

  return config;
};

export default applyConfig;

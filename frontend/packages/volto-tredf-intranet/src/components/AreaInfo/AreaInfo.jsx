import React from 'react';
import { Container } from '@plone/components';
import Icon from '@plone/volto/components/theme/Icon/Icon';
import houseSVG from '@plone/volto/icons/home.svg';

const AreaInfo = ({ content, icon }) => {
  return (
    <Container className="areaInfo">
      {icon && <Icon name={houseSVG} size="64px" className={'icon listitem'} />}
      <h2 className="title">{content.title}</h2>
      <p className="description">{content.description}</p>
    </Container>
  );
};

export default AreaInfo;

import React from 'react';
import { Container } from '@plone/components';

const AreaInfo = ({ content }) => {
  return (
    <Container className="areaInfo">
      <h2 className="title">{content.title}</h2>
      <p className="description">{content.description}</p>
    </Container>
  );
};

export default AreaInfo;

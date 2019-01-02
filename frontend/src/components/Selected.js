import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";

const SelectedImage = styled.img`
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
`;

const Selected = ({ photo }) => (
  <SelectedImage src={photo.src} alt={photo.photo_name} />
);

Selected.propTypes = {
  photo: PropTypes.shape({
    id: PropTypes.number.isRequired,
    src: PropTypes.string.isRequired,
    item_id: PropTypes.number.isRequired,
    photo_name: PropTypes.string.isRequired,
    item_name: PropTypes.string.isRequired
  })
};

export default Selected;

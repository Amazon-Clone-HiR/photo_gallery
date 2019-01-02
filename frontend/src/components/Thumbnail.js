import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";

const ThumbnailImage = styled.img`
  width: 100%;
  border: 1px solid #888;
  border-radius: 3px;
`;

const Thumbnail = ({ photo, onHover }) => (
  <ThumbnailImage src={photo.src} alt={photo.name} onMouseOver={onHover} />
);

Thumbnail.propTypes = {
  photo: PropTypes.shape({
    id: PropTypes.number.isRequired,
    src: PropTypes.string.isRequired,
    item_id: PropTypes.number.isRequired,
    photo_name: PropTypes.string.isRequired,
    item_name: PropTypes.string.isRequired
  }),
  index: PropTypes.number.isRequired
};

export default Thumbnail;

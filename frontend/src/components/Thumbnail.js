import React from "react";
import PropTypes from "prop-types";
import styled from "styled-components";

const ThumbnailImage = styled.img`
  width: 100%;
  border: 1px solid ${props => (props.selected ? "#e77600" : "#111")};
  border-radius: 3px;
  box-shadow: ${props => (props.selected ? "0 0 5px #e77600" : "none")};

  &:hover {
    cursor: pointer;
  }
`;

const Thumbnail = ({ photo, onHover, selected }) => (
  <ThumbnailImage
    src={photo.src}
    alt={photo.name}
    onMouseOver={onHover}
    selected={selected}
  />
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

import React, { useState, useEffect } from "react";
import axios from "axios";
import styled from "styled-components";

import Thumbnail from "./Thumbnail";
import Selected from "./Selected";

const Gallery = styled.div`
  display: grid;
  grid-template-columns: 1fr 6fr;
  grid-template-rows: 50vh;
  grid-column-gap: 10px;
  max-width: 50%;
`;

const ThumbnailContainer = styled.div`
  overflow-y: scroll;
`;

const SelectedContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  place-content: center;
`;

const App = () => {
  const [isLoading, toggleLoading] = useState(true);
  const [photos, setPhotos] = useState([]);
  const [selectedPhoto, setSelectedPhoto] = useState(null);

  useEffect(() => {
    axios("/api/items/4/")
      .then(({ data }) => {
        setPhotos(data);
        setSelectedPhoto(data[0]);
        toggleLoading(false);
      })
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <Gallery>
        <ThumbnailContainer>
          {photos.map((photo, i) => (
            <Thumbnail
              key={photo.id}
              index={i}
              photo={photo}
              onHover={() => setSelectedPhoto(photos[i])}
            />
          ))}
        </ThumbnailContainer>
        <SelectedContainer>
          {!isLoading && <Selected photo={selectedPhoto} />}
        </SelectedContainer>
      </Gallery>
    </div>
  );
};

export default App;

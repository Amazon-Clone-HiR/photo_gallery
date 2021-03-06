import React, { useState, useEffect } from "react";
import axios from "axios";
import styled from "styled-components";

import Thumbnail from "./Thumbnail";
import Selected from "./Selected";

const Gallery = styled.div`
  display: grid;
  grid-template-columns: 1fr 5fr;
  grid-template-rows: 50vh;
  grid-column-gap: 10px;
  max-width: 50%;
`;

const ThumbnailContainer = styled.div`
  overflow-y: scroll;
  padding: 0 5px;
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
    axios("/api/items/ecbe7295-0dc7-4066-bd3d-9db36e26d64e/")
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
              selected={selectedPhoto === photo}
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

import React, { useState } from 'react';
import { uploadFile } from '../services/api';

function UploadView() {
  const [file, setFile] = useState(null);

  const handleUpload = () => {
    if (!file) {
      alert('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    uploadFile(formData)
      .then((response) => alert(response.data.message))
      .catch((error) => console.error('Upload failed:', error));
  };

  return (
    <section>
      <h2>Upload Database</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </section>
  );
}

export default UploadView;

import React, { useState } from "react";
import axios from "axios";

import {
  DJANGO_SERVER_ADDRESS,
  FILE_UPLOAD_ROUTE,
  GET_MAIN_DF_ROUTE,
  GET_PC_DF_ROUTE,
  GET_LPC_DF_ROUTE,
  GET_PLASMALOGEN_DF_ROUTE,
  GET_RETENTION_RF_DF_ROUTE,
  GET_MEAN_AGG_RF_DF_ROUTE,
} from "./config";

const NOT_UPLOADED = "notUploaded";
const UPLOADING = "uploading";
const UPLOADED = "uploaded";
const FAILED = "failed";

const REQUIED_FILE_FORMAT =
  "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

const App = () => {
  const [uploadStatus, setUploadStatus] = useState(NOT_UPLOADED);
  const [formState, setFormState] = useState({ dataFile: null, dfID: null });

  const submitHandler = (e) => {
    e.preventDefault();

    if (
      formState.dataFile != null &&
      formState.dataFile.type === REQUIED_FILE_FORMAT &&
      uploadStatus != UPLOADING
    ) {
      const formData = new FormData();
      formData.append("dataFile", formState.dataFile, formState.dataFile.name);

      console.log("uploading", formState.dataFile);

      setUploadStatus(UPLOADING);

      axios
        .post(`${DJANGO_SERVER_ADDRESS}/${FILE_UPLOAD_ROUTE}`, formData)
        .then((res) => {
          if (res.data.df_id != undefined) {
            setUploadStatus(UPLOADED);
            setFormState((prevState) => ({
              ...prevState,
              dfID: res.data.df_id,
            }));
          } else {
            setUploadStatus(FAILED);
          }
        })
        .catch((err) => {
          console.error(err);
          setUploadStatus(FAILED);
        });
    }
  };

  const fileChangeHandler = (event) => {
    const file = event.target.files[0];
    setFormState((prevState) => ({
      ...prevState,
      dataFile: file,
    }));
  };

  const dowloadDFHandler = (associated_route) =>
    axios
      .get(`${DJANGO_SERVER_ADDRESS}/${associated_route}`, {
        params: { df_id: formState.dfID },
      })
      .then((res) => {
        console.log("downloaded df data", res.data, typeof res.data);
        const csvData = "data:text/csv;charset=utf-8," + res.data;
        window.open(encodeURI(csvData));
      });

  console.log("#", formState);

  return (
    <div className="App">
      <div>eluci-data file-handler</div>
      <form onSubmit={(e) => submitHandler(e)}>
        <input onChange={fileChangeHandler} type="file"></input>
        <input type="submit" name="upload"></input>
      </form>
      {uploadStatus === UPLOADED && (
        <div>
          <div>File upload was successful df-id {formState.dfID}</div>
          <div>
            <button onClick={() => dowloadDFHandler(GET_MAIN_DF_ROUTE)}>
              Main df
            </button>
            <button onClick={() => dowloadDFHandler(GET_PC_DF_ROUTE)}>
              pc df
            </button>
            <button onClick={() => dowloadDFHandler(GET_LPC_DF_ROUTE)}>
              lpc df
            </button>
            <button onClick={() => dowloadDFHandler(GET_PLASMALOGEN_DF_ROUTE)}>
              plasmalogen df
            </button>
            <button onClick={() => dowloadDFHandler(GET_RETENTION_RF_DF_ROUTE)}>
              retention rf df
            </button>
            <button onClick={() => dowloadDFHandler(GET_MEAN_AGG_RF_DF_ROUTE)}>
              mean agg rf df
            </button>
          </div>
        </div>
      )}
      {uploadStatus == FAILED && <div>last upload failed</div>}
    </div>
  );
};

export default App;

import React, { useState } from 'react';
import SearchForm from "../SearchForm";
import * as S from "./styles";
import PersonDetails from "../PersonDetails";
import axios from "axios";

const Main = () => {
  const [searchResult, setSearchResult] = useState(null);
  const [noResults, setNoResults] = useState(false);
  const [formValues, setFormValues] = useState(null);

  const handleSearch = async (formValues) => {
    console.log("Form Values:", formValues);
    setFormValues(formValues); // Save form values to state variable

    try {
      const response = await axios.post('http://127.0.0.1:5000/search', formValues);
      console.log("Search Result:", response.data); // Log the result
      setSearchResult(response.data);
      setNoResults(false);
    } catch (error) {
      console.error("There was an error!", error);
      setSearchResult(null);
      setNoResults(true);
    }
  };

  const handleClear = () => {
    setSearchResult(null);
    setNoResults(false);
    setFormValues(null);
  };

  return (
    <S.Main>
      <div>
        <SearchForm onSubmit={handleSearch} />
        <S.Results>
          {noResults && <div className="noResultsStyle">Nu s-a găsit nimic</div>}
          {searchResult && (
            <div>
              <button onClick={handleClear} className="clearButtonStyle">
                Clear
              </button>
              <PersonDetails person={searchResult} />
            </div>
          )}
        </S.Results>
      </div>
    </S.Main>
  );
};

export default Main;

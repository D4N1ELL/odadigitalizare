import React, { useState } from 'react';
import SearchForm from "../SearchForm";
import * as S from "./styles";
import PersonDetails from "../PersonDetails";
import axios from "axios";

const Main = () => {
  const [searchResult, setSearchResult] = useState([]);
  const [noResults, setNoResults] = useState(false);
  const [formValues, setFormValues] = useState(null);

  const handleSearch = async (formValues) => {
    console.log("Form Values:", formValues);
    setFormValues(formValues); // Save form values to state variable

    try {
      const response = await axios.post('http://127.0.0.1:5000/search', formValues);
      console.log("Search Result:", response.data); // Log the result

      let normalizedResult = response.data;
      if (!Array.isArray(normalizedResult)) {
        normalizedResult = [normalizedResult];
      }

      setSearchResult(normalizedResult);
      setNoResults(normalizedResult.length === 0);
    } catch (error) {
      console.error("There was an error!", error);
      setSearchResult([]);
      setNoResults(true);
    }
  };

  const handleClear = () => {
    setSearchResult([]);
    setNoResults(false);
    setFormValues(null);
  };

  return (
    <S.Main>
      <div>
        <SearchForm onSubmit={handleSearch} />
        <S.Results>
          {noResults && <div className="noResultsStyle">Nu s-a găsit nimic</div>}
          {searchResult.length > 0 && (
            <div>
              <button onClick={handleClear} className="clearButtonStyle">
                Clear
              </button>
              {searchResult.map((person, index) => (
                <PersonDetails key={index} person={person} />
              ))}
            </div>
          )}
        </S.Results>
      </div>
    </S.Main>
  );
};

export default Main;

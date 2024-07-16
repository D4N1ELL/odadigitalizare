import SearchForm from "../SearchForm";
import * as S from "./styles";
import { useState } from "react";
import PersonDetails from "../PersonDetails";

const Main = () => {
  const [searchResult, setSearchResult] = useState(null);

  const handleSearch = (formValues) => {
    // For demonstration purposes, we will use a static result
    const result = {
      username: "Persoana 5",
      surname: "Doe",
      application_date: ["18-07-2023", "18-09-2024"],
      idnp: "5555555555555",
      bday: "01/03/1995",
      age: 28,
      location: "or. Ialoveni",
      phone_number: "+37355555555",
      email: "test5@gmail.com",
      program: "Ecologizare IMM",
      operator: "O.Constantinova",
      confirmation_date: "2023-07-20T00:00:00",
      comment: "așteaptă instruire",
      statut: "lista de așteptare",
      instruction_participation: [
        "GR 2 - 0 ZILE",
        "GR 8 - 0 ZILE",
        "GR 13 - 0ZILE",
      ],
      certificate: "PEA/SB/632 din 13.10.2023",
      finance: "PARE 23/II-100 DIN 13.06.2023",
      final_statut: "NaN",
      exclusion: "NaN",
      notice: {
        "phone_call": ["01/03/1995", NaN, NaN],
        "email_call": [NaN, "01/04/1995", NaN],
        "sms_call": [NaN, NaN, "01/05/1995"],
        "viber_call": [NaN, NaN, "01/06/1995"],
        "response": ["Confirm", "Confirm", "Confirm"]

      },
    };
    setSearchResult(result);
  };

  const handleClear = () => {
    setSearchResult(null);
  };

  return (
    <S.Main>
      <div >
        <SearchForm onSubmit={handleSearch} />
        <S.Results>
        {searchResult && (
          <div >
            <button onClick={handleClear} className="clearButtonStyle">Clear</button>
            <PersonDetails person={searchResult} />
            <PersonDetails person={searchResult} />
          </div>
        )}

        </S.Results>
      </div>
    </S.Main>
  );
};

// const AppStyle = {
//   display: "flex",
//   flexDirection: "column",
//   alignItems: "center",
//   gap: "2em",
//   padding: "2em",
// };

// const resultsContainerStyle = {
//   display: "flex",
//   flexDirection: "column",
//   alignItems: "center",
//   gap: "1em",
//   width: "100%",
// };

// const clearButtonStyle = {
//   alignSelf: "flex-end",
//   padding: "10px 20px",
//   borderRadius: "25px",
//   border: "1px solid #0073e6",
//   backgroundColor: "#0073e6",
//   color: "#fff",
//   fontSize: "16px",
//   fontWeight: "bold",
//   cursor: "pointer",
//   transition: "background-color 0.3s, box-shadow 0.3s",
//   margin: "22px 0"
// };

export default Main;

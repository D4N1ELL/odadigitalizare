import Header from "./components/Header";
import Main from "./components/Main";
import ExcelExportButton from './components/ExcelExportButton'; // Import the newly created component

const data = [
  {
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
      phone_call: ["01/03/1995", NaN, NaN],
      email_call: [NaN, "01/04/1995", NaN],
      sms_call: [NaN, NaN, "01/05/1995"],
      viber_call: [NaN, NaN, "01/06/1995"],
      response: ["Confirm", "Confirm", "Confirm"],
    },
  },
  // Add more person objects here
];

function App() {
  
  return (
    <>
      <Header />
      <Main />
      <ExcelExportButton data={data} />    </>
  );
}

export default App;

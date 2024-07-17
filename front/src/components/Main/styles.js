import styled from "styled-components";

export const Main = styled.div`
  background-color: #213b8b;
  min-height: calc(100vh - 86.5px);
  & > div {
    max-width: 1400px;
    margin: 0 auto 0;
    padding-top: 72px;
  }
  .noResultsStyle {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #0073e6;
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
    padding: 10px 20px;
    border-radius: 15px;
    border: 1px solid #0073e6;
    background-color: #f0f4ff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    width: 100%;
    text-align: center;
  }
`;

export const Results = styled.div`
  margin-top: 32px;
  display: flex;
  flex-direction: column;
  gap: 1px;
  .clearButtonStyle{
    align-self: flex-end;
    padding: 10px 20px;
    border-radius: 25px;
    border: 1px solid #0073e6;
    background-color: #0073e6;
    color: #fff;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s, box-shadow 0.3s;
    margin: 22px 0;
  }
`;

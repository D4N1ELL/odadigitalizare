import styled from "styled-components";

export const Main = styled.div`
  background-color: #213b8b;
  min-height: calc(100vh - 86.5px);
  & > div {
    max-width: 1400px;
    margin: 0 auto 0;
    padding-top: 72px;
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

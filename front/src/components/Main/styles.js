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
`;

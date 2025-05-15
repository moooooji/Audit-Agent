# WrappedThreatPromptor

## langchain studio

#### 1. clone the project and relevant repositories.
```bashå
git clone https://github.com/StackAuditFlow/WrappedThreatPromptor.git &&
cd WrappedThreatPromptor/src/react_agent && git clone https://github.com/StackAuditFlow/Utils.git &&
cd Utils && git clone https://github.com/berachain/contracts.git && cd ../../../
```

#### 2. install dependencies  
** return project root directory **
```bash
make install
```

3.start langchain studio  
```bash
make run
```

## Audit Agent
** need gemini api key in .env file **
```bash
input dataset/berachain_docs_merged.md
```

image.png
# Setup Cypress Testing

- node must be installed in your system

```bash
node -v
npm -v # package manager for node
# create configuration file
# create folder cypress
mkdir cypressdemo
# move to the folder
cd cypressdemo
npm init -y # this will create package.json file
# install cypress
npm i cypress --save-dev # install only for dev scope (--save-dev)
# launch cypress
npx cypress open # will work only in windows
#  to run wsl just setup entire case by using above options
#  run in wsl using
npx cypress run
# this command will run testcase without opening browser (headless mode)
```

- it will open browser, you can see cypress screen
- select allow, continue
- select E2E testing
- it will show some default file named added to your project 
- conitnue -> select chrome browser -> click on start
- it will redirect you to browser screen for creating test

**Create Test Case**
- you will get default option availble
- suggestion code also will be there you can use

- basic.spec.js (test file)

```js
describe('Create Simple Test', () => {
  it('check thigs working fine', () => {
    cy.visit('https://example.cypress.io')
    cy.contains('type').click()
    cy.url().should('include', '/commands/actions') // test case

    cy.get('.action-email').type('sonam@email.com')
    cy.get('.action-email').should('have.value', 'sonam@email.com') //test case
  })
})
```
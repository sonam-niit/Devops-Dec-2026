describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://example.cypress.io')
    cy.contains('type').click()
    cy.url().should('include', '/commands/actions') // test case

    cy.get('.action-email').type('sonam@email.com')
    cy.get('.action-email').should('have.value', 'sonam@email.com') //test case
  })
})
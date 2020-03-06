describe('My First Test', function () {
  it('Visits the LinkIT website', function () {
    cy.visit('https://www.linkit.nl/')
    cy.contains('LINKIT')
    cy.contains('daagt je uit')
    cy.contains('ENG').click()
    cy.contains('challenges you')
  })
})

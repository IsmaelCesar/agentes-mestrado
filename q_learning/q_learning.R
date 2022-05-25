# modelo de transicao para as recomensas
T_up = matrix(0, 6, 6)
T_up[1, 3] = 1
T_up[2, 4] = 1
T_up[3, 5] = 1
T_up[4, 6] = 1
T_up[5, 5] = 1
T_up[6, 6] = 1

T_down = matrix(0, 6, 6)
T_down[1, 1]= 1
T_down[2, 2]= 1
T_down[3, 1]= 1
T_down[4, 2]= 1
T_down[5, 3]= 1
T_down[6, 4]= 1

T_left = matrix(0, 6, 6)
T_left[1, 1] = 1
T_left[2, 1] = 1
T_left[3, 3] = 1
T_left[4, 3] = 1
T_left[5, 5] = 1
T_left[6, 5] = 1

T_right = matrix(0, 6, 6)
T_right[1, 2] = 1
T_right[2, 2] = 1
T_right[3, 4] = 1
T_right[4, 4] = 1
T_right[5, 6] = 1
T_right[6, 6] = 1

# recompensas
rw = diag(-9, 6, 6)
rw <- rw - 1
rw[,6] <- 10
rw[6, 6] <- 0

# funcoes importantes
choose_action <- function(){
  # funcao para escolher uma acao aleatoriamente
  return(sample(4)[1])
}

q_update <- function(state, action, next_state, rw_matrix, q_matrix, alpha, gamma){
  computed_rw = rw[state, next_state]
  estimate = computed_rw + gamma*max(q_matrix[next_state,]) - q_matrix[state, action]
  value = q_matrix[state, action] + alpha*estimate
  return(value)
}

# inicializacao
alpha <- 0.5
gamma <- 1
q_matrix <- matrix(0, 6, 4)

actions_names = c("UP","DW","LF","RG")

for(i in 1:100){
  
  state = 1
  terminal = TRUE
  
  while(terminal){
    action = choose_action()
    
    # escolhendo modelo de transicao
    if(action == 1){ transition_model = T_up }
    if(action == 2){ transition_model = T_down }
    if(action == 3){ transition_model = T_left }
    if(action == 4){ transition_model = T_right }
    
    # Computando proximo estado
    state_row = transition_model[state,]
    next_state = which.max(state_row)
    
    #Printando acao
    print(c(state, actions_names[action], next_state))
    
    # atualizando qualidade da acao na q-matriz
    q_matrix[state, action] <- q_update(state, action, next_state, rw, q_matrix, alpha, gamma)
    
    state = next_state
    
    if(state == 6){ terminal = FALSE}
  }
}

print('Q-MATRIX')
print(q_matrix)

print('POLITICA:')
policy <- max.col(q_matrix)

s1 = paste(actions_names[policy[5]], "+10")
s2 = paste(actions_names[policy[3]], actions_names[policy[4]])
s3 = paste(actions_names[policy[1]], actions_names[policy[2]])
cat('\n', s1, '\n', s2, '\n', s3)

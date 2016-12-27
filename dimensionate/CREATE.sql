CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `db` AS
    SELECT 
        `issues`.`id` AS `id`,
        `issues`.`subject` AS `titulo`,
        `issues`.`description` AS `descricao`,
        `custom_values`.`value` AS `tamanho`
    FROM
        (`issues`
        JOIN `custom_values`)
    WHERE
        ((`custom_values`.`customized_id` = `issues`.`id`)
            AND (`custom_values`.`custom_field_id` = 85)
            AND (`custom_values`.`value` > 0))
    ORDER BY `custom_values`.`value`
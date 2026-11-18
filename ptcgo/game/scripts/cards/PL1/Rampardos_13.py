from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="d866a598-cdaa-5376-b9e5-442db982a94c",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name",
    display_name="Rampardos",
    searchable_by=["Rampardos", "Stage 2", "Rampardos"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Ability(
            title="Iron Skull",
            game_text="Rampardos's attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            effect=ignore_modifier_attack(ignore_resistance=True, ignore_target_effects=True),
        ),
        Attack(
            title="Head Smash",
            game_text="If the Defending Pok\u00e9mon would be Knocked Out by this attack, Rampardos does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Mold Breaker",
            game_text="Any damage done to Rampardos by attacks is reduced by 20 (after applying Weakness and Resistance) until the end of your next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)
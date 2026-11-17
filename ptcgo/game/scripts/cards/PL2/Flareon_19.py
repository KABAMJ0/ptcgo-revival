from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ea08e12-0e28-53a4-9a81-cb2e69863cca",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Undevelop",
            game_text="Once during your turn (before your attack), you may devolve Flareon and put Flareon into your hand. This power can't be used if Flareon is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Evolving Flare",
            game_text="If Flareon evolved from Eevee during this turn, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
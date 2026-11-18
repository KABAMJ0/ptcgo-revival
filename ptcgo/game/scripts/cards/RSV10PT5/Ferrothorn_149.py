from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea39d41e-8c68-5cff-a426-b9397daca85c",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Attack(
            title="Power Whip",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
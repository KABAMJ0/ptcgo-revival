from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30abd7a1-537b-5b98-b70e-bf57d206a6ed",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Vital Throw",
            game_text="You may do 40 damage plus 20 more damage. If you do, Machamp does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Hundred Furious Punches",
            game_text="Does 60 damage plus 10 more damage for each Fighting Energy attached to Machamp.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
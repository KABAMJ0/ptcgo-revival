from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e484696e-b0fb-583f-86cf-46ca09e182f3",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Short-Circuit Knuckle",
            game_text="If your opponent has any Water Pok\u00e9mon in play, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Electroslug",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
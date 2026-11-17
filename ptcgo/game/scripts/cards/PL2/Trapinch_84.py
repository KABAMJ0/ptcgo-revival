from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d13113a9-f720-5da5-b445-3eca64a58371",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=328,
    abilities=[
        Ability(
            title="Gather Sand",
            game_text="Once during your turn (before your attack), if Trapinch is your Active Pok\u00e9mon, you may search your discard pile for a basic Fighting card and attach it to Trapinch.",
            effect=unimplemented,
        ),
        Attack(
            title="Grind",
            game_text="Does 10 damage times the amount of Energy attached to Trapinch.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
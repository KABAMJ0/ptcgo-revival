from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca915fcb-f12c-5240-b07c-089283493c55",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeE4.Name",
    display_name="Gallade E4",
    searchable_by=["Gallade E4", "Basic", "SP", "GalladeE4"],
    subtypes=["Basic", "SP"],
    collector_number=20,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Chop Up",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Feint",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
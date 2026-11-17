from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="41e4eb33-3c80-598f-a340-10954d59a2f1",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to Wobbuffet by your opponent's Pok\u00e9mon-ex.",
            effect=unimplemented,
        ),
        Attack(
            title="Flip Over",
            game_text="Wobbuffet does 10 damage to itself, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
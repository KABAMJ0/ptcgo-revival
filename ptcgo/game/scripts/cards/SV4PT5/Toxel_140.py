from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="394aa2d4-e4ad-53a1-9798-5c7f4887f3e7",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    display_name="Toxel",
    searchable_by=["Toxel", "Basic", "Toxel"],
    subtypes=["Basic"],
    collector_number=140,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=848,
    abilities=[
        Attack(
            title="Slight Intrusion",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11615cec-df15-5167-82d9-70b64113c0a9",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic", "Future", "Miraidon"],
    subtypes=["Basic", "Future"],
    collector_number=92,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=1008,
    abilities=[
        Attack(
            title="Peak Acceleration",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to your Future Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Sparking Strike",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.PSYCHIC: 1},
            damage=160,
        ),
    ],
)
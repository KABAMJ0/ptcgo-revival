from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="882ab3e4-70e4-5efd-9b5f-a638e27e4f17",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon ex and Pok\u00e9mon V.",
            effect=unimplemented,
        ),
        Attack(
            title="Ghost Eye",
            game_text="Put 7 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)
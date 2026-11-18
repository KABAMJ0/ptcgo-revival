from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="56936fe7-4e2e-5db4-8a63-517bc3d02351",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet", "Basic", "Shuppet"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=353,
    abilities=[
        Attack(
            title="Disable",
            game_text="Flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Haunt",
            game_text="Put 1 damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)